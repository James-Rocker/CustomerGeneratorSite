from flask import Flask
from flask import request
import Generator

app = Flask(__name__)


def index():
    return "<h1>Hello World!</h1>"


@app.route("/index", endpoint=Generator.Customer)
def my_form_post():
    # text1 = request.form['text1']
    # text2 = request.form['text2']
    # plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1, text2)
    pass
    return


app.add_url_rule("/", "index", my_form_post)

if __name__ == "__main__":
    app.run()
