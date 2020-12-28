import os
from flask import render_template
from flask import Flask
from app import customer


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # the home page
    @app.route("/")
    def hello():
        return render_template('home.html', data=customer.build_new())
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
