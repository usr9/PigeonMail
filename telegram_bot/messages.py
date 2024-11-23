help_message = """*PigeonMail* _(Alpha)_ 🐦
Not the most _efficient_ way to send messages on Telegram.
To use my service it is *required to have a username set in your Telegram account*. 
_If you don't have one, you can set it in the settings._

*How it works:*
1. Register yourself
2. Tell a friend to register
3. Add your friend
4. Tell your friend to add you
5. Send a message to your friend
6. Wait for the pigeon to deliver it 🐦

*Commands:*
/register - Register yourself in the system
/addfriend _<username>_ - Tell your friend to do the same with your username, boom, you're friends!
/send _<username> <message>_ - Send a message to your friend (who knows if they'll ever get it)
/friends - List all __your__ _friends_
/msgs - List all your *messages*
/help - Show this message

"""


send_message_success = """Message sent! 📬 The pigeon is flying"""
send_error_message = """Please provide a username and a message. Example: `/send username Hello friend`"""


request_location_message = """Please share your location with me. You can do this by clicking the paperclip icon in the chat and selecting 'Location'."""
thanks_for_location_message = """Thanks for sharing your location! 🌍"""
location_error_message = """I'm sorry, I couldn't get your location. Please try again."""