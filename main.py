from flask import Flask, render_template

app = Flask(__name__, template_folder='.', static_folder='dist')


@app.route("/")
def hello():
    return render_template('index.html')