import mss
import os
import os.path
import telebot
import pyautogui
import getpass
import time
from config import *

# телега
bot = telebot.TeleBot(token)
FILE_NAME = "screen.png"
USER_NAME = getpass.getuser()
mifitbombclicker = False

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.id not in adm:
        bot.send_message(message.chat.id, 'Вы не можете пользоваться этим ботом.')
    else:
        bot.send_message(message.chat.id, f'qq, {message.from_user.first_name}')

@bot.message_handler(commands=['screen'])
def screenshot(message):
	if message.chat.id not in adm:
		bot.send_message(message.chat.id, "Вы не можете пользоваться этим ботом.")
	else:
	    bot.send_message(message.chat.id, "Секунду...".format(message.from_user, bot.get_me()), parse_mode='HTML', reply_markup=None)
	    with mss.mss() as sct:
	    	sct.shot(output = FILE_NAME)
	    photo = open("screen.png", "rb")
	    bot.send_photo(message.chat.id, photo)
	    photo.close()
	    os.remove("screen.png")

@bot.message_handler(commands=['off'])
def offpc(message):
	if message.chat.id not in adm:
		bot.send_message(message.chat.id, "Вы не можете пользоваться этим ботом.")
	else:
	    bot.send_message(message.chat.id, "Секунду...".format(message.from_user, bot.get_me()), parse_mode='HTML', reply_markup=None)
	    os.system('shutdown -s -t 1')

@bot.message_handler(commands=['offtimer'])
def offtimerpc(message):
	if message.chat.id not in adm:
		bot.send_message(message.chat.id, "Вы не можете пользоваться этим ботом.")
	else:
	    bot.send_message(message.chat.id, "напиши количество секунд")
	    @bot.message_handler(content_types=['text'])
	    def inputofftimerpc(message):
	        timer = message.text
	        timer = str(timer)
	        bot.send_message(message.chat.id, "компьютер выключится через " + timer + " секунд")
	        os.system("shutdown -s -t " + timer)

@bot.message_handler(commands=['window'])
def minimizewindow(message):
	if message.chat.id not in adm:
		bot.send_message(message.chat.id, "Вы не можете пользоваться этим ботом.")
	else:
	    bot.send_message(message.chat.id, "Свернул все окна")
	    pyautogui.hotkey('winleft', 'd')

@bot.message_handler(commands=['play'])
def minimizewindow(message):
	if message.chat.id not in adm:
		bot.send_message(message.chat.id, "Вы не можете пользоваться этим ботом.")
	else:
	    bot.send_message(message.chat.id, "Мультимедиа остановлена/запущена")
	    pyautogui.press('playpause')

@bot.message_handler(commands=['mifitbomb'])
def mifitbomb(message):
	if message.chat.id not in adm:
		bot.send_message(message.chat.id, "Вы не можете пользоваться этим ботом.")
	else:
		global mifitbombclicker
		if mifitbombclicker == False:
			mifitbombclicker = True
			pyautogui.press('V')
			bot.send_message(message.chat.id, "MiFit бомба запущена!")
			return 1
		if mifitbombclicker == True:
			mifitbombclicker = False
			pyautogui.press('V')
			bot.send_message(message.chat.id, "MiFit бомба остановлена!")
			return 1

bot.polling()
