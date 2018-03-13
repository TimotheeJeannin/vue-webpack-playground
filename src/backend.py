from flask import Flask, render_template

app = Flask(__name__, template_folder='.', static_folder='../dist')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/page")
def page():
    return render_template('page.html')
