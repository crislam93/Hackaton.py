#descargar modulo: pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler

def main():
    #instanciamos el Updater
    updater = Updater(token=open("Telegram Chatbot/token.txt").read(), use_context= True)
    
    #añadimos un manejador al comando start de Telegram
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #añadimos un manejador para el comando repite de Telegram
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #añadir manejador para el comando suma de Telegram
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    #Capturamos señales de parada
    updater.idle()


def start(update, context):
    update.message.reply_text("Hola, soy un Bot")  

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    #args = [2, 2]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es " + str(resultado))

main()