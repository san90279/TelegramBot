import os
import telegram
from flask import Flask, request


# 環境變數
token = os.getenv("TELEGRAM_BOT_TOKEN")
PORT = int(os.environ.get('PORT', '8443'))
bot = telegram.Bot(token)

app = Flask(__name__)


@app.route('/{}'.format(token), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)


    bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook("https://telegrambotforme.herokuapp.com/" + token)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)

