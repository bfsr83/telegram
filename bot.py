import telebot # Importamos las librería

TOKEN = '992968153:AAHAMmgFVvJ5ARxKoY6Wwxdgp81bZiQbpQM' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

# enviar mensagem simples

tb.send_message(chatid, text) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
