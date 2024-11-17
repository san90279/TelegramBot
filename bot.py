import os
from telegram import Update
from telegram.ext import Application, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text("Hello! I am your bot.")

TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

application.run_polling()