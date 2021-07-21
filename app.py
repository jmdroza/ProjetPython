import script
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    res = script.function()
    return res

if __name__ == '__main__':
    app.run()


