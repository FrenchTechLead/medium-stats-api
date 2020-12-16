import os

import requests
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route('/')
def hello():
    return "HELLO"


@app.route('/api/stats', methods=['GET'])
def getJwt():
    story_url = request.args.get('story_url')
    c = requests.get(story_url).content.decode("utf-8")
    c = c.split("clapCount\":")[1]
    endIndex = c.index(",")
    claps = int(c[0:endIndex])
    c = c.split("responsesCount\":")[1]
    endIndex = c.index(",")
    comments = int(c[0:endIndex])
    return jsonify(comments=comments, claps=claps)


api = Api(app)
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
