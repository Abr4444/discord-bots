import os, json
from replit import db
from telegram import ChatAction
import qrcode
import logging
from random import randint
INPUT_TEXT = 0

from telegram import Update #upm package(python-telegram-bot)
from telegram import (
    Poll,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler,
    filters,
)
#upm package(python-telegram-bot)


from math import ceil
from flask import render_template
from flask import Flask
app = Flask(__name__)


def latest_key():
    ks = db.keys()
    if len(ks):
        return max(map(int, ks))
    else:
        return -1



def qr_command_handler(update, context):
  update.message.reply_text("Send me a message to turn into a qr")

  return INPUT_TEXT 


def help_command(update: Update, context: CallbackContext) -> None:
    htext = '''
Welcome
Send /fetch to retrieve the most recent message
Send /qr to create a qr with the message you input'''
    update.message.reply_text(htext)


def log(update: Update, context: CallbackContext) -> None:
    db[str(latest_key() + 1)] = update.message.text


def fetch(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(db.get(str(latest_key()), 'No Messages Yet.'))

def generate_qr(text):
  filename = text + '.jpg'
  img = qrcode.make(text)
  img.save(filename)
  return filename

def send_qr(filename, chat):
  chat.send_action(
    action=ChatAction.UPLOAD_PHOTO, timeout=None
  )
  pass
  
  chat.send_photo(photo=open(filename, 'rb'))
  os.unlink(filename)

def input_text(update, context):
  text = update.message.text

  print(text)
  filename = generate_qr(text)
  chat = update.message.chat
  print(chat)
  send_qr(filename, chat)
  return ConversationHandler.END
  
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



def xpMsg(update: Update, context: CallbackContext) -> None:
    user_id = update.message["reply_to_message"]["from_user"]["id"]

    if update.message["text"] == "+":
        write_to_file(user_id, 1)
        return update.message.reply_text(f"You have successfully awarded 1 reputation point to {update.message['reply_to_message']['from_user']['name']}")


#if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
def reaction(update: Update, context: CallbackContext) -> None:
    user_id = update.message["reply_to_message"]["from_user"]["id"]

    if user_id == update.message["from_user"]["id"]:
      return update.message.reply_text("Hey! You can't award reputation to yourself!")
    else:
      pass

    if update.message["text"] == "+":
        write_to_file(user_id, 1)
        return update.message.reply_text(f"You have successfully awarded 1 reputation point to {update.message['reply_to_message']['from_user']['name']}")
    if update.message["text"] == "🔥":
        write_to_file(user_id, 1)
        return update.message.reply_text(f"You have successfully awarded 1 reputation point to {update.message['reply_to_message']['from_user']['name']}")
    if update.message["text"] == "👍":
        write_to_file(user_id, 1)
        return update.message.reply_text(f"You have successfully awarded 1 reputation point to {update.message['reply_to_message']['from_user']['name']}")
    elif update.message["text"] == "-":
        write_to_file(user_id, -1)
        return update.message.reply_text(f"You have successfully revoked 1 reputation point from {update.message['reply_to_message']['from_user']['name']}")
    elif update.message["text"] == "👎":
        write_to_file(user_id, -1)
        return update.message.reply_text(f"You have successfully revoked 1 reputation point from {update.message['reply_to_message']['from_user']['name']}")
    elif update.message["text"] == "💩":
        write_to_file(user_id, -1)
        return update.message.reply_text(f"You have successfully revoked 1 reputation point from {update.message['reply_to_message']['from_user']['name']}")
    else:
        pass

def profile(update: Update, context: CallbackContext) -> None:
    rep = return_data(update.message["from_user"]["id"])[str(update.message["from_user"]["id"])]

    update.message.reply_text(f"{update.message['from_user']['name']} \nYour Reputation is: {rep} points")

def poll(update: Update, context: CallbackContext) -> None:
    """Sends a predefined poll"""
    questions = ["Good", "Really good", "Fantastic", "Great"]
    message = context.bot.send_poll(
        update.effective_chat.id,
        "How are you?",
        questions,
        is_anonymous=False,
        allows_multiple_answers=True,
    )
    # Save some info about the poll the bot_data for later use in receive_poll_answer
    payload = {
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    context.bot_data.update(payload)


def receive_poll_answer(update: Update, context: CallbackContext) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    poll_id = answer.poll_id
    try:
        questions = context.bot_data[poll_id]["questions"]
    # this means this poll answer update is from an old poll, we can't do our answering then
    except KeyError:
        return
    selected_options = answer.option_ids
    answer_string = ""
    for question_id in selected_options:
        if question_id != selected_options[-1]:
            answer_string += questions[question_id] + " and "
        else:
            answer_string += questions[question_id]
    context.bot.send_message(
        context.bot_data[poll_id]["chat_id"],
        f"{update.effective_user.mention_html()} feels {answer_string}!",
        parse_mode=ParseMode.HTML,
    )
    context.bot_data[poll_id]["answers"] += 1
    # Close poll after three participants voted
    if context.bot_data[poll_id]["answers"] == 3:
        context.bot.stop_poll(
            context.bot_data[poll_id]["chat_id"], context.bot_data[poll_id]["message_id"]
        )


def quiz(update: Update, context: CallbackContext) -> None:
    """Send a predefined poll"""
    questions = ["1", "2", "420", "69"]
    message = update.effective_message.reply_poll(
        "How many senioritas does blitz get?", questions, type=Poll.QUIZ, correct_option_id=2
    )
    # Save some info about the poll the bot_data for later use in receive_quiz_answer
    payload = {
        message.poll.id: {"chat_id": update.effective_chat.id, "message_id": message.message_id}
    }
    context.bot_data.update(payload)


def receive_quiz_answer(update: Update, context: CallbackContext) -> None:
    """Close quiz after three participants took it"""
    # the bot can receive closed poll updates we don't care about
    if update.poll.is_closed:
        return
    if update.poll.total_voter_count == 3:
        try:
            quiz_data = context.bot_data[update.poll.id]
        # this means this poll answer update is from an old poll, we can't stop it then
        except KeyError:
            return  
        context.bot.stop_poll(quiz_data["chat_id"], quiz_data["message_id"])


def preview(update: Update, context: CallbackContext) -> None:
    """Ask user to create a poll and display a preview of it"""
    # using this without a type lets the user chooses what he wants (quiz or poll)
    button = [[KeyboardButton("Press me!", request_poll=KeyboardButtonPollType())]]
    message = "Press the button to let the bot generate a preview for your poll"
    # using one_time_keyboard to hide the keyboard
    update.effective_message.reply_text(
        message, reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
    )


def receive_poll(update: Update, context: CallbackContext) -> None:
    """On receiving polls, reply to it by a closed poll copying the received poll"""
    actual_poll = update.effective_message.poll
    # Only need to set the question and options, since all other parameters don't matter for
    # a closed poll
    update.effective_message.reply_poll(
        question=actual_poll.question,
        options=[o.text for o in actual_poll.options],
        # with is_closed true, the poll/quiz is immediately closed
        is_closed=True,
        reply_markup=ReplyKeyboardRemove(),
    )

def website(chat):

  chat.send_action(
    action=ChatAction.UPLOAD_PHOTO, timeout=None
  )
  pass
  
  chat.send_photo('bby_QR.png')  
  os.unlink('bby_QR.png')

logging.basicConfig(
  level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

def welcomeMSG(update,context):
  bot = context.bot
  chatId = update.message.chat_id
  updateMsg = getattr(update, "message", None)
  for user in updateMsg.new_chat_members:
    userName = user.first_name 
  
  logger.info(f'{userName} has just joined')

  bot.sendMessage(
  chat_id = chatId,
  text=f'{userName} has just joined '
  )



def main():

    updater = Updater(os.getenv("TOKEN"))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", help_command))
    dp.add_handler(MessageHandler(filters.Filters.reply, reaction))
    dp.add_handler(CommandHandler("profile", profile))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('qr', qr_command_handler)], states = {INPUT_TEXT:[MessageHandler(Filters.text, input_text)]}, fallbacks = {}))
    dp.add_handler(CommandHandler("fetch", fetch))
    dp.add_handler(CommandHandler("website", website))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, log))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members,welcomeMSG))
    dp.add_handler(PollAnswerHandler(receive_poll_answer))
    dp.add_handler(CommandHandler('quiz', quiz))
    dp.add_handler(PollHandler(receive_quiz_answer))
    dp.add_handler(CommandHandler('preview', preview))
    dp.add_handler(MessageHandler(Filters.poll, receive_poll))
    updater.start_polling()

    #updater.idle()
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()