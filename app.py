import logging
import random
import sqlite3
import configparser
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from src.handlers import general, unknown, dryer
#from src.db import models


def main():
    # Import configuration from config.ini
    config = configparser.ConfigParser()
    config.read('src/cfg/config.ini')
    api_token = config['TELEGRAM']['TOKEN']

    # Initialise updater and dispatcher
    up = Updater(token=api_token)
    dp = up.dispatcher

    # Initialise logging module
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Conversation Handler - /start command
    dp.add_handler(
        CommandHandler('start', general.start)
    )

    # Conversation Handler - /status command
    dp.add_handler(
        CommandHandler('status', general.status)
    )

    # Conversation Handler - /set command
    dp.add_handler(
        ConversationHandler(
            entry_points = [
                CommandHandler('set', dryer.set),
            ],
            states = {
                1: [
                    MessageHandler(Filters.text, dryer.set),
                ],
            },
            fallbacks = [
                MessageHandler(Filters.text, unknown.text)
            ],
        )
    )

    # Unknown Handler - Commands
    dp.add_handler(
        MessageHandler(Filters.command, unknown.command)
    )

    # Unknown Handler - Text
    dp.add_handler(
        MessageHandler(Filters.text, unknown.text)
    )

    # Start the Bot
    up.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    up.idle()


if __name__ == "__main__":
    main()
