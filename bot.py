import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters


# 載入 .env 檔案
load_dotenv()
environment = os.getenv("ENV")
token = os.getenv("TELEGRAM_BOT_TOKEN")
print(token)

async def start(update: Update, context):
    await update.message.reply_text("Hello! I am your bot.")
# 定義回聲處理函數
async def echo(update: Update, context):
    # 取得用戶發送的訊息
    user_message = update.message.text
    # 回應相同的訊息
    await update.message.reply_text(user_message)


application = Application.builder().token(token).build()
# 添加回聲處理器
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
application.add_handler(CommandHandler("start", start))
application.run_polling()

#if environment == "development":
#    application.run_polling()
#else:
#    application.run_webhook(url_path="https://telegrambotforme-a46e78381e82.herokuapp.com/")