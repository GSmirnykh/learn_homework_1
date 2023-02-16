import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import ephem
from datetime import date


logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text("Здравствуй, пользователь!")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def planet_info(update, context):
    text = update.message.text.split()
    planet = text[1].lower()

    if planet == 'mars':
        planet_position = ephem.Mars(date.today())
        const = ephem.constellation(planet_position)

    elif planet == 'mercury':
        planet_position = ephem.Mercury(date.today())
        const = ephem.constellation(planet_position)

    elif planet == 'moon':
        planet_position = ephem.Moon(date.today())
        const = ephem.constellation(planet_position)

    result = ' '.join(const)
    update.message.reply_text(result)  # Почему при попытке распоковать словарь результат не выводится в телеграмме?



    print(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot has started!")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
