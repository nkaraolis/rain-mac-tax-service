from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/rain-mac-price.json')
def hello_world():
    tax=50.99
    return jsonify(price=tax)


if __name__ == '__main__':
    app.run(port=9002)
