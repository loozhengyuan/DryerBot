import textwrap
from telegram import ChatAction, ParseMode


def start(bot, update):
    """
    Handles the entry point for the chatbot
    Returns a list of applicable commands
    """
    # Send chat action
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    # Retrieves user information
    user_id = update.message.from_user.id
    user_handle = update.message.from_user.username

    # Sends a text containing a list of applicable commands
    text = """
    Hello @{}!

    *General Commands*
    /start - Displays this menu
    /status - Provides a status of your dryers
    /about - More information about this bot

    *Dryer-specific Commands*
    /set - Sets the timer for dryer
    /end - End timer prematurely
    /report - Report a dryer is empty or full
    """.format(user_handle)
    bot.send_message(chat_id=update.message.chat_id, text=textwrap.dedent(text), parse_mode=ParseMode.MARKDOWN)


def status(bot, update):
    """
    Returns a status page of dryers and time left (if applicable)
    """
    # Send chat action
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    status_text = "There are no dryers in use currently."
    bot.send_message(chat_id=update.message.chat_id, text=status_text)

