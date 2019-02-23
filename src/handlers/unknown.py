import random
from telegram import ChatAction


def text(bot, update):
    """
    Handles for any text that are unknown.
    """
    
    # Send chat action
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    
    # List of phrases/sentences with the same meaning
    text = [
        "Sorry, I can only handle slash commands for now!",
        "I really not sure what this means. You can refer to /start for more information.",
    ]
    
    # Sends a text with error message
    bot.send_message(chat_id=update.message.chat_id, text=random.choice(text))


def command(bot, update):
    """
    Handles for any commands that are unknown.
    """
    # Send chat action
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    
    # List of phrases/sentences with the same meaning
    text = [
        "Sorry, I didn't understand that command.",
        "I really not sure of this command.",
    ]
    
    # Sends a text with error message
    bot.send_message(chat_id=update.message.chat_id, text=random.choice(text))