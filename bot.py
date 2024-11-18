import os
from flask import Flask, request
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters


# 載入 .env 檔案
load_dotenv()
environment = os.getenv("ENV")
token = os.getenv("TELEGRAM_BOT_TOKEN")

# Flask Web 應用
app = Flask(__name__)

async def start(update: Update, context):
    await update.message.reply_text("Hello! I am your bot.")
# 定義回聲處理函數
async def echo(update: Update, context):
    # 取得用戶發送的訊息
    user_message = update.message.text
    # 回應相同的訊息
    await update.message.reply_text(user_message)

# Webhook 的路徑
@app.route(f"/{token}", methods=["POST"])
def webhook():
    """處理來自 Telegram 的 Webhook 請求"""
    json_data = request.get_json()
    update = Update.de_json(json_data, application.bot)
    application.update_queue.put_nowait(update)
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200

application = Application.builder().token(token).build()
# 添加回聲處理器
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
application.add_handler(CommandHandler("start", start))
#application.run_polling()

if environment == "development":
    application.run_polling()
else:
    application.run_webhook(url_path=f"{HEROKU_APP_URL}/{token}")
    # 啟動 Flask
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))