from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    obj = {
        "url":"pepi",
        "on":False
    }
    return obj