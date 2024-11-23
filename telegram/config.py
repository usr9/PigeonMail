from dotenv import load_dotenv
import os

# Load environment variables from a file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

# Retrieve the bot token
TG_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Debugging: Print the token to verify it's loaded correctly
if TG_BOT_TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in the .env file!")