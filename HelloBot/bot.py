import re
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
    Бот может здороваться на разных языках.
    Список поддерживаемых приветствий:
    - привет - русский
    - hello - английский
    - hola - испанский
    - barev - армянский
    - salam - азербайджанский
    - ni hao - китайский
    """)

def ru(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("привет")

def en(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("hello")

def es(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("hola")

def ar(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("barev")

def az(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("salam")

def chi(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("ni hao")

def not_supported(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Приветствие {update.message.text} не подерживается.")

def get_greeting_filter(greeting: str) -> BaseFilter:
    return Filters.regex(re.compile(f"^{greeting}$", re.IGNORECASE)) & Filters.update.message

def main() -> None:
    updater = Updater("YOUR TOKEN")
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("привет"), ru))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("hello"), en))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("hola"), es))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("barev"), ar))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("salam"), az))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter("ni hao"), chi))
    updater.dispatcher.add_handler(MessageHandler(Filters.update.message & Filters.text, not_supported))
    updater.start_polling()
    print("Started")
    updater.idle()

if __name__ == "__main__":
    main()