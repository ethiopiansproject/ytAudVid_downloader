
import os
import pafy
from telebot import TeleBot,telebot,types
from telebot.util import user_link
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
bot = telebot.TeleBot(os.getenv("B-Token"),parse_mode="HTML")


markup = InlineKeyboardMarkup()
b1 = InlineKeyboardButton('🦧Official Channel🦧',url='t.me/DevelopersPage')
b2 = InlineKeyboardButton('🦅Official Group🦅',url='t.me/DevelopersChat')
markup.add(b1,b2)

@bot.message_handler(commands=['start'])
def welcome_msg(message):
    user = message.from_user
    bot.reply_to(message,f'Hello dear {user_link(user)} welcome to youtube audio downloader bot\n just send valid youtube link',reply_markup = markup)
  
    
@bot.message_handler(func = lambda m:True)
def audio_download(msg):
    downloader = pafy.new(msg.text)
    audio = downloader.audiostreams[0]
    fileName = f"{downloader.title}.mp3"
    audio.download(fileName)
    with open(fileName,"rb") as audio:
        bot.send_audio(msg.chat.id,audio,caption=f"{downloader.title}")
        os.remove(f"{downloader.title}.mp3")

bot.infinity_polling()
