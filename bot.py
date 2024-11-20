import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# 環境變數
token = os.getenv("TELEGRAM_BOT_TOKEN")

# 建立 Application
bot_app = Application.builder().token(token).build()

# Flask 應用
app = Flask(__name__)

# 指令處理函數
async def start(update: Update, context):
    await update.message.reply_text("歡迎使用這個機器人！")

async def echo(update: Update, context):
    await update.message.reply_text(f"你說了：{update.message.text}")

# 註冊處理器
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Webhook 處理
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.process_update(update)
    return "ok"

@app.route('/', methods=['GET'])
def index():
    return "ok"

if __name__ == "__main__":
    app.run()
