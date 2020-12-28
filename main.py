import Generator
from flask import render_template
from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route("/")
    def hello():
        return render_template('/json.html', data=Generator.build_customer())
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
