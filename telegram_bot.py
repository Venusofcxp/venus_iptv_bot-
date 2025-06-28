from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv
load_dotenv()

def start(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton("🔍 Buscar", callback_data='buscar')],
        [InlineKeyboardButton("🆕 Recentes", callback_data='recentes')],
        [InlineKeyboardButton("🎬 Quantidade", callback_data='quantidade')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)

def iniciar_bot():
    updater = Updater(os.getenv("TELEGRAM_TOKEN"))
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
