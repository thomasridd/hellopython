from flask import Flask
from flask import Response

from json import dumps

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello python server is running now'

@app.route("/rest", methods=['GET'])
def get_hello():

    # Message object
    msg = {"message":"Hello world!","greetings":["Happy October!","Simple REST rocks"]}

    # Return JSON response
    return Response(dumps(msg), mimetype="application/json")

if __name__ == "__main__":
    app.run()
