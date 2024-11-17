import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your bot.")

def main():
    TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
