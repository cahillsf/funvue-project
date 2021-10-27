from flask import Flask, jsonify, request
from flask_cors import CORS
from ddtrace import Pin, patch
import pymongo
from pprint import pprint
import sys
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
CORS(app, resources={r'/*': {'origins': '*'}})
client = pymongo.MongoClient('mongodb://flask-role:toor@localhost:27017/sitecontent?authSource=sitecontent')




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
    db = client['sitecontent']
    users = db.users
    user_cursor = users.find({ "handle": json_data['email'] })
    for index, document in enumerate(user_cursor):
        print(document, file=sys.stderr)
    print(json_data, file=sys.stderr)
    return "hello"


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)