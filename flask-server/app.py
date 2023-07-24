from flask import Flask, jsonify, request, Response, make_response
from flask_cors import CORS
from ddtrace import Pin, patch
import pymongo
from pprint import pprint
import sys
import jwt
import logging
import datetime
import os
import werkzeug
from ddtrace import config, patch_all, Pin, patch, tracer
#import ddtrace.profiling.auto
# from ddtrace.profiling.profiler import Profiler

config.env = "dev"      # the environment the application is in
config.service = "flask-server"  # name of your application
config.version = "0.0.1"  # version of your application
patch(logging=True)
patch_all()

# configuration
DEBUG = True
# prof = Profiler(
#     env="dev",  # if not specified, falls back to environment variable DD_ENV
#     service="flask-server",  # if not specified, falls back to environment variable DD_SERVICE
#     version="0.0.1",   # if not specified, falls back to environment variable DD_VERSION
# )
# prof.start()

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT)

# instantiate the app
app = Flask(__name__)
deployment = os.environ.get('DEPLOYMENT')
config_string = 'config.' + deployment + 'Config'
my_obj_instance = werkzeug.utils.import_string(config_string)()
app.config.from_object(my_obj_instance)

db_uri = str(app.config['DATABASE_URI'])
print(app.config['DATABASE_URI'], file=sys.stderr)
logging.info("db uri is {}".format(db_uri))
client = pymongo.MongoClient(db_uri)
# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, origins=["http://localhost:8080, http://localhost"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
# client = pymongo.MongoClient('mongodb://flask-role:toor@localhost:27017/sitecontent?authSource=sitecontent')


def encode_auth_token(usr_id):
    # https://www.bacancytechnology.com/blog/flask-jwt-authentication
    # secret_key is set via the above link secrets.token_hex(16)
    # FIXME: when containerizing, this will have to be dynamically generated
    print("encoding auth token", file=sys.stderr)
    secret_key = os.getenv('SECRET_KEY')
    print(secret_key, file=sys.stderr)
    try:
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5)
        payload = {
            'exp': exp,
            'iat': datetime.datetime.utcnow(),
            'sub': usr_id
        }
        # return a list of 2 items, the token and the exp date to set in the reponse header
        return [jwt.encode(
            payload,
            secret_key,
            algorithm='HS256'
        ), exp]
    except Exception as e:
        return e

# sanity check route
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/cards', methods=['GET'])
def all_cards():
    db = client['sitecontent']
    cards = db.cards
    cards_cursor = cards.find({})
    print("hello", file=sys.stderr)
    print(cards_cursor)
    cards_dict = {}
    for index, document in enumerate(cards_cursor):
        print(document, file=sys.stderr)
        cards_dict[index] = document
    print(type(cards_dict), file=sys.stderr)
    return (cards_dict)

@app.route('/api/userAuth', methods=['POST'])
def user_auth():
    try:
        db = client['sitecontent']
        # search user in users collection of sitecontent db
        result = list(db.users.find({ "handle": request.authorization.username }))
        logging.info("result from db.users.find is {}".format(result))
        # check password
        if not (request.authorization['password'] == result[0]['password']):
            print("strings dont match, erroring out", file=sys.stderr)
            return Response("{'Error':'User Not Found or Password Incorrect'}", status=400, mimetype='application/json')
        # encode the JWT with usr handle (email) as sub
        token = encode_auth_token(str(result[0]['handle']))
        print(token, file=sys.stderr)
        res = make_response("Success", 200)
        res.headers["Content-Type"] = "application/json"
        # print decoded token for debugging purposes
        print(jwt.decode(token[0],os.getenv('SECRET_KEY'), algorithms=["HS256"]), file=sys.stderr)
        #  set access token as httpoonly cookie
        res.set_cookie("access_token", value=token[0], expires=token[1], httponly=True)
        return res
    except Exception as e:
        # print(e, file=sys.stderr)
        logging.error("exception occurred in user auth: {}".format(e))
        return Response("{'Error':'User Not Found or Password Incorrect'}", status=400, mimetype='application/json')

#debug route to check if the access_token is being sent in client response
@app.route('/api/testRoute', methods=['POST', 'GET'])
def testRoute():
    data_str = request.data.decode('utf-8')
    cookies_list = data_str.split('; ')
    print(cookies_list)
    token = request.cookies.get('access_token')
    print(token, file=sys.stderr)
    return "OKAY", 200

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
    log = logging.getLogger(__name__)
    log.level = logging.DEBUG

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    # base_url = "/api"
    # mongo_client = "ps-mongo-service"