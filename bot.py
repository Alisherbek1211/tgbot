import logging

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🚖Buyurtma"),KeyboardButton("❌Bekor qilish")],
        [KeyboardButton("📊Hisobot"),KeyboardButton("📜Taklif")],
        [KeyboardButton("📌Kompaniya Haqida")]
    
    ]
    )
munu_buyurtma = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🚖Aksiya"),KeyboardButton("⚡️Tezkor")],
        [KeyboardButton("🐌Yetkazib berish"),KeyboardButton("✈️Komfort")],
        [KeyboardButton("◀️Orqaga")]
    
    ]
    )
text = """
Buyurtma turini tanlang

🚖Aksiya - Minimal summa 2000 so'm.5km gacha har km - 1000 so'm, qolgan km - 500 so'm.

⚡️Tezkor - 5 daqiqada kelishi ta'minlanadi.Minimal summa 5000 so'm.

🐌Yetkazib berish" - Minimal summa - 8000 so'm. 1km - 500 so'm

✈️Komfort" - Komfort mashina

"""

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Assalomu Alaykum {user.mention_markdown_v2()} \! \n Dostavka hizmatiga xush kelibsiz\!',
        reply_markup=menu,
        
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def buyurtma(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text=text,
        reply_markup=munu_buyurtma,
        
    )


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5470778624:AAHzp7Vp9Kod3wgFkvreaGDx7PqWnogM1ko")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text("🚖Buyurtma"),buyurtma))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()