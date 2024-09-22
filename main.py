from config import *
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from random import randint
import sqlite3
bot = TeleBot(TOKEN)
hideBoard = types.ReplyKeyboardRemove() 



@bot.message_handler(commands=['start'])
def info(message):
    bot.send_message(message.chat.id,
"""
Вот команды которые могут тебе помочь:

/random - Показать случайного пользователся🧑‍💼
/ids "Id пользователя" - Также ты можешь ввести ID Пользователя и узнать информацию о нем!👾
....
""")




def senf_info(bot, message, row ):


     info = f"""
UserId: {row[0]}
Gender: {row[1]}
Age: {row[2]}
EstimatedSalary: {row[3]}
Purchased: {row[4]}
"""
     
@bot.message_handler(commands=['random'])
def random_match(message):
    con = sqlite3.connect("User_Data.db")
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM User_Database ORDER BY RANDOM() LIMIT 1")
        row = cur.fetchall()[0]
        cur.close()
    senf_info(bot, message, row)