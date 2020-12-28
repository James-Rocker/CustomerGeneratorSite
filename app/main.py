import json
from flask import render_template
from flask import Flask
from app import customer


# create and configure the app
app = Flask(__name__, instance_relative_config=True)


# the home page
@app.route("/")
def home_page():
    return render_template("home.html", jsonfile=json.dumps(customer.build_new()))


if __name__ == "__main__":
    app.run(debug=True)

