import script
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    res = script.function()
    print(res[0].capteur_id)
    return render_template("home.html", content = res, len = len(res))


if __name__ == '__main__':
    app.run()
