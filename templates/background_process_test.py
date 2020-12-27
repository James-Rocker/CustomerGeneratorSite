from flask import Flask
from flask import request
from flask import render_template
import Generator


app = Flask(__name__)


@app.route("/json")
def json():
    return render_template("json.html")


@app.route("/background_process_test")
def background_process_test():
    print("Hello")
    return "nothing"


if __name__ == "__main__":
    app.run()
