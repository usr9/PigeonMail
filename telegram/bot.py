import logging

from telegram import ForceReply, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

import config

from messages import (
    help_message, 
    send_error_message, 
    request_location_message, 
    thanks_for_location_message, 
    location_error_message, 
    send_message_success
    )

logging.basicConfig(
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s", level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.first_name}!\n{help_message}", parse_mode="Markdown")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(help_message, parse_mode="Markdown")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

## Command to add a friend
async def add_friend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add a friend to the user's friend list."""
    # The username of the friend is passed as the first argument
    friend_username = context.args[0]
    logger.debug(f"Friend username: {friend_username}")

    # Add the friend to the user's friend list
    #TODO implement this using the database

## Command to send a message
async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message to a friend."""

    # Check if the message is empty, if so break and return an error message to the user
    if len(context.args) < 2:
        await update.message.reply_text(send_error_message, parse_mode="Markdown")
        return

    # The usename of the friend is passed as the first argument
    friend_username = context.args[0]
    logger.debug(f"Friend username: {friend_username}")

    # Check if the friend is in the user's friend list, if not break and return an error message to the user
    #TODO implement this using the database


    # The message is passed as the rest of the arguments
    #! the space with cause formatting issues when users type with commas and other special characters
    message = " ".join(context.args[1:])
    logger.debug(f"Message: {message}")

    await update.message.reply_text(send_message_success)

## Command to list friends
async def list_friends(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List all friends of the user."""
    #TODO implement this using the database

## Command to list messages
async def list_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List all messages of the user."""
    #TODO implement this using the database

## Command to set your location
async def set_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user to send their location."""
    await update.message.reply_text(request_location_message)

## Message handler to capture the location
async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle location shared by the user."""
    if update.message.location:
        user_location = update.message.location
        latitude = user_location.latitude
        longitude = user_location.longitude

        # Log the location data
        logger.info(f"Received location: Latitude={latitude}, Longitude={longitude}")

        # TODO: Save location to a database or persistent storage

        await update.message.reply_text(thanks_for_location_message)
    else:
        await update.message.reply_text(location_error_message)


def main() -> None:

    application = Application.builder().token(config.TG_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    application.add_handler(CommandHandler("send", send))
    # application.add_handler(CommandHandler("addfriend", add_friend))
    # application.add_handler(CommandHandler("friends", list_friends))
    # application.add_handler(CommandHandler("msgs", list_messages))
    application.add_handler(CommandHandler("loc", set_location))

    # on non command i.e message - echo the message on Telegram
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Handler for location messages
    application.add_handler(MessageHandler(filters.LOCATION, handle_location))

    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == "__main__":

    main()