import json
from telegram import Bot

# Load credentials from the JSON file
def load_credentials():
    with open("telegram_credentials.json", "r") as file:
        credentials = json.load(file)
    return credentials["bot_token"], credentials["user_id"]

# Initialize the bot with loaded credentials
bot_token, user_id = load_credentials()
bot = Bot(token=bot_token)

# Function to send a message to yourself
def send_message_to_me(message):
    bot.send_message(chat_id=user_id, text=message)

# Example usage
if __name__ == '__main__':
    send_message_to_me
