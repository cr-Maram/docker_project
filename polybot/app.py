import flask
from flask import request
import os
from bot import ObjectDetectionBot, Bot

app = flask.Flask(__name__)

TELEGRAM_TOKEN_FILE = os.environ['TELEGRAM_TOKEN_FILE']
with open(TELEGRAM_TOKEN_FILE, "r") as f:
    TELEGRAM_TOKEN = f.read().rstrip()
TELEGRAM_APP_URL = os.environ['TELEGRAM_APP_URL']


@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.handle_message(req['message'])
    return 'Ok'


if __name__ == "__main__":
    bot = ObjectDetectionBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)

    app.run(host='0.0.0.0', port=8443)
