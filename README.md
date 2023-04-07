## Telegram Bot to Roll Two Dice

This project is a dice game developed using Python programming language and the Telegram Bot API. This bot allows users to roll two dice with the `/roll_dice` command.

### Installation

To run this project, you can follow these steps:

1. Download or clone the project.
2. Open the console and use the `cd` command to go to the directory of your project.
3. Run the `python Bot.py` command to create the `config.json` file and follow the instructions on the screen.
4. Save your bot token to the `config.json` file.
5. Install the required Python modules by running the following command: `pip install python-telegram-bot / 13.7`.
6. Use the `python run.py` command to run the `run.py` file.

### Usage

After adding the bot to a chat or channel, users can use the `/roll_dice` command to roll two dice.

### Example

The following code snippet is a section of the `Bot.py` file that defines the `/roll_dice` command:

```python
import telegram
from telegram.ext import Updater, CommandHandler
import os
import json

# ...

# Defining the command
updater.dispatcher.add_handler(CommandHandler('roll_dice', roll_dice_handler))

# Starting the bot
updater.start_polling()

# Wait for the bot to start
print("Bot is starting. Please wait...")

# Send instructions to the user
print("Please add the bot to a chat/channel and make it an admin. You can then use the /roll_dice command to roll two dice.")

updater.idle()
## License

#
## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for more information.
