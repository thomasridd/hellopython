from flask import Flask
from json import dumps

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello python server is running now'

@app.route("/rest", methods=['GET'])
def get_hello():

    # Message object
    msg = {"message":"Hello world!","greetings":["Ho ho ho!","Simple REST rocks"]}

    # Return JSON response
    return dumps(msg)

if __name__ == "__main__":
    app.run()
