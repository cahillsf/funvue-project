from flask import Flask, jsonify
from flask_cors import CORS
from ddtrace import Pin, patch
# from flask_pymongo import PyMongo
import pymongo
from pprint import pprint
import sys

# configuration
DEBUG = True
patch(pymongo=True)

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# app.config["MONGO_URI"] = "mongodb://root:example@localhost:27017/sitecontent?authSource=admin"
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# mongo=PyMongo(app)
client = pymongo.MongoClient('mongodb://root:example@localhost:27017/sitecontent?authSource=admin')
# client = MongoClient('mongodb://localhost:27017/')


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
    # return jsonify({
    #     'status': 'success',
    #     'books': 'BOOKS',
    # })


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)