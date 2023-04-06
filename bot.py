from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
import os 
from db import LikeDB
TOKEN=os.environ.get("TOKEN")

like_db = LikeDB('db.json')

def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    chat_id = update.message.chat.id
    like_db.add_student(chat_id)
    # likeDB.add_student(str(chat_id))
    bot.sendMessage(chat_id,'Sen me picture!')

def photo(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    photo = update.message.photo[-1]["file_id"]

    
    like = like_db.all_likes()
    dislike = like_db.all_dislikes()
    btn1 = InlineKeyboardButton(text=f'\U0001F44D {like}', callback_data="like")
    btn2 = InlineKeyboardButton(text=f'\U0001F44E {dislike}', callback_data="dislike")

    keyboard = InlineKeyboardMarkup([[btn1, btn2]])
    bot.sendPhoto(chat_id = chat_id, photo=photo, reply_markup=keyboard)
# -1001683268337
def count_like_dislike(update, context):
    query = update.callback_query
    data = query.data
    
    chat_id = query.message.chat.id

    if data == 'like':
        like_db.add_like(chat_id)
    
    elif data == 'dislike':
        like_db.add_dislike(chat_id)

    like = like_db.all_likes()
    dislike = like_db.all_dislikes()

    btn1 = InlineKeyboardButton(text=f'\U0001F44D {like}', callback_data="like")
    btn2 = InlineKeyboardButton(text=f'\U0001F44E {dislike}', callback_data='dislike')

    keyboard = InlineKeyboardMarkup([[btn1, btn2]])
    query.edit_message_reply_markup(reply_markup=keyboard)

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.photo, photo))
dp.add_handler(CallbackQueryHandler(count_like_dislike))

updater.start_polling()
updater.idle()