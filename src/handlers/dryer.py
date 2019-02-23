import sqlite3
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup


def set(bot, update):
    """
    Sets the timer for a specific machine
    """

    # Send chat action
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    # Retrieves user information
    user_id = update.message.from_user.id
    user_handle = update.message.from_user.username

    # TODO: Check if user is currently using any machine

    # Record to database
    # PASS

    # Activate notify timer
    # PASS

    # Handles arguments if presented
    if args:
        # Assign id of machine to variable
        machine_id = args[0]

        # TODO: Check if machine is availble and exists

        # Send message to user
        text = "Timer for {} is set!".format(machine_id)
        bot.send_message(chat_id=update.message.chat_id, text=text)
    
    # Else, look to registered lists
    else:
        # TODO: Dynamically retrieves machine friendly names

        # Generates keyboard layout
        reply_keyboard = [
            [
                InlineKeyboardButton("#ABC123", callback_data="Hello"),
                InlineKeyboardButton("#CDE456", callback_data="Hello"),
            ],
            [
                InlineKeyboardButton("#ABC123", callback_data="Hello"),
                InlineKeyboardButton("#CDE456", callback_data="Hello"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(reply_keyboard)

        # Sends message prompting for response
        text = "Please select the device below:"
        bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=reply_markup)
