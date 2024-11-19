import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# 環境變數
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 建立 Application
app = Application.builder().token(TOKEN).build()

# Flask 應用
flask_app = Flask(__name__)

# 指令處理函數
async def start(update: Update, context):
    await update.message.reply_text("歡迎使用這個機器人！")

async def echo(update: Update, context):
    await update.message.reply_text(f"你說了：{update.message.text}")

# 註冊處理器
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Webhook 處理
@flask_app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), app.bot)
    app.process_update(update)
    return "ok"

if __name__ == "__main__":
    flask_app.run(port=5000)
