import json
from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackContext, filters

def return_data(user_id):
    f = open("data.json", "r")
    data = json.load(f)
    f.close()

    if str(user_id) in data:
        return {str(user_id): data[str(user_id)]}
    else:
        return {str(user_id): 0}

def write_to_file(user_id, rep):
    f = open("data.json", "r")
    data = json.load(f)
    f.close()

    if str(user_id) in data:
        data[str(user_id)] = data[str(user_id)] + rep
    else:
        data[str(user_id)] = rep

    data = json.dumps(data)
    outfile = open("data.json", "w")
    outfile.write(data)
    outfile.close()

def reaction(update: Update, context: CallbackContext) -> None:
    user_id = update.message["reply_to_message"]["from_user"]["id"]

    if user_id == update.message["from_user"]["id"]:
      return update.message.reply_text("Hey! You can't award reputation to yourself!")

    if update.message["text"] == "+":
        write_to_file(user_id, 1)
        return update.message.reply_text(f"You have successfully awarded 1 reputation point to {update.message['reply_to_message']['from_user']['name']}")
    elif update.message["text"] == "-":
        write_to_file(user_id, -1)
        return update.message.reply_text(f"You have successfully revoked 1 reputation point from {update.message['reply_to_message']['from_user']['name']}")
    else:
        pass

def profile(update: Update, context: CallbackContext) -> None:
    rep = return_data(update.message["from_user"]["id"])[str(update.message["from_user"]["id"])]

    update.message.reply_text(f"{update.message['from_user']['name']} \nYour Reputation is: {rep} points")

updater = Updater("1936379187:AAG8mT7RZDFMMxIsFpKpedGblLY1w_t1uIQ")

updater.dispatcher.add_handler(MessageHandler(filters.Filters.reply, reaction))
updater.dispatcher.add_handler(CommandHandler("profile", profile))

updater.start_polling()
updater.idle()