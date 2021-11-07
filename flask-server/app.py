from flask import Flask, jsonify, request, Response, make_response
from flask_cors import CORS
from ddtrace import Pin, patch
import pymongo
from pprint import pprint
import sys
import jwt
import datetime
import os
#import ddtrace.profiling.auto
# from ddtrace.profiling.profiler import Profiler


# configuration
DEBUG = True
# prof = Profiler(
#     env="dev",  # if not specified, falls back to environment variable DD_ENV
#     service="flask-server",  # if not specified, falls back to environment variable DD_SERVICE
#     version="0.0.1",   # if not specified, falls back to environment variable DD_VERSION
# )
# prof.start()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, origins=["http://localhost:8080", "http://127.0.0.1:8080"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
client = pymongo.MongoClient('mongodb://flask-role:toor@localhost:27017/sitecontent?authSource=sitecontent')


def encode_auth_token(usr_id):
    # https://www.bacancytechnology.com/blog/flask-jwt-authentication
    # secret_key is set via the above link secrets.token_hex(16)
    # FIXME: when containerizing, this will have to be dynamically generated
    secret_key = os.getenv('SECRET_KEY')
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
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/cards', methods=['GET'])
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

@app.route('/userAuth', methods=['POST'])
def user_auth():
    json_data = request.json
    # pull out the credentials from the request- find user by handle
    # check password
    # FIXME: secure submission of password to server
    try:
        db = client['sitecontent']
        result = list(db.users.find({ "handle": json_data['email'] }))
        if not (json_data['password'] == result[0]['password']):
            return Response("{'Error':'User Not Found or Password Incorrect'}", status=400, mimetype='application/json')
        # encode the JWT with usr handle (email) as sub
        token = encode_auth_token(result[0]['handle'])
        res = make_response("Success", 200)
        res.headers["Content-Type"] = "application/json"
        # print decoded token for debugging purposes
        print(jwt.decode(token[0],os.getenv('SECRET_KEY'), algorithms=["HS256"]))
        print(result, file=sys.stderr)
        res.set_cookie("access_token", value=token[0], expires=token[1], httponly=True)
        print(res, file=sys.stderr)
        return res
    except Exception as e:
        print(e, file=sys.stderr)
        return Response("{'Error':'User Not Found or Password Incorrect'}", status=400, mimetype='application/json')

#debug route to check if the access_token is being sent in client response
@app.route('/testRoute', methods=['POST', 'GET'])
def testRoute():
    data_str = request.data.decode('utf-8')
    cookies_list = data_str.split('; ')
    print(cookies_list)
    token = request.cookies.get('access_token')
    print(token, file=sys.stderr)
    return "OKAY", 200

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)