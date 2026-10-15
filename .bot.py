import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
bot.reply_to(
message,
"هلا! 👋 أنا بوت مكافحة الإعلانات المزعجة. أعمل على تجهيز نفسي لحماية المجموعات."
)

@bot.message_handler(commands=['help'])
def help_command(message):
bot.reply_to(
message,
"أضفني إلى مجموعتك ومنحني صلاحية حذف الرسائل لتجربة مكافحة الإعلانات."
)

bot.infinity_polling()
