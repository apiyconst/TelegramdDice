import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater
import os
import json

# Function to get bot token from user input and save it in config.json file
def save_token():
    token = input("Please enter your bot token: ")
    with open('config.json', 'w') as f:
        json.dump({'TOKEN': token}, f)

# Check if config.json file exists
if not os.path.exists('config.json'):
    print("Config file is missing. Creating a new one...")
    save_token()

# Read bot token from config.json file
with open('config.json', 'r') as f:
    config = json.load(f)
TOKEN = config['TOKEN']

# Starting the telegram bot
bot = telegram.Bot(token=TOKEN)
updater = Updater(TOKEN)

# Function to respond to /roll_dice command
def roll_dice_handler(update, context):
    try:
        # Setting the name and path of the video to be captured
        output_path = "dice_roll.gif"
        # Updating the file path (You need to specify the directory name of Bot.py here.)
        os.system(f"python {os.path.dirname(os.path.abspath(__file__))}/dice.py {output_path}")
        # Sending the video to the user
        with open(output_path, 'rb') as gif_file:
            update.message.reply_animation(gif_file, timeout=100)
        # Deleting the video
        os.remove(output_path)
    except:
        update.message.reply_text("An error occurred. Please try again later.")

# Defining the command
updater.dispatcher.add_handler(CommandHandler('roll_dice', roll_dice_handler))

# Starting the bot
updater.start_polling()

# Wait for the bot to start
print("Bot is starting. Please wait...")

# Send instructions to the user
print("Please add the bot to a chat/channel and make it an admin. You can then use the /roll_dice command to roll two dice.")

updater.idle()
