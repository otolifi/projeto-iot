import subprocess
import psutil
import random
import telepot
import time

def opcoes(msg):
  chat_id = msg['chat']['id']
  comando = msg['text']

  if comando == '/percentual':
    bot.sendMessage(chat_id, psutil.cpu_percent())
  elif comando == '/data':
    bot.sendMessage(chat_id, subprocess.check_output('date', shell=True).decode())
  elif comando == '/resposta':
    bot.sendMessage(chat_id, random.choice(['42','Voce nao fez a pergunta fundamental','Toalha']))


bot = telepot.Bot('1760589241:AAEvdlTDlAivAN3Hj8WiVcxZ9jT7wleWu40')
bot.message_loop(opcoes)
print('Kuwait please wait......')

while True:
  time.sleep(10)