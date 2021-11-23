from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import logging

logging.basicConfig(filename='bot.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print ('Вызван /start')
    print (update)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    random_talk_number = randint(0,4)
    if random_talk_number == 0:
        text = update.message.text
        text_answer_1 = 'Приму это к сведению! Может быть, может быть...'
        print (text)
        update.message.reply_text(text_answer_1)
    elif random_talk_number == 1:
        text = update.message.text
        text_answer_1 = f'{text} - говоришь ты) а я что? Я примус починяю!'
        print (text)
        update.message.reply_text(text_answer_1) 
    elif random_talk_number == 2:
        text = update.message.text
        text_answer_2 = text[::-1]
        print (text)
        update.message.reply_text(text_answer_2) 
    elif random_talk_number == 3:
        text = update.message.text
        text_splits = text.split()
        for word in reversed(text_splits):
            text_splits.append(word[::-1])
            text_splits.remove(word)
            text_splits_reversed = text_splits
        for reverse_word in reversed(text_splits_reversed):
            text_splits_reversed.append(reverse_word)
            text_splits_reversed.remove(reverse_word)
            text_answer_3 = ' '.join(text_splits_reversed)            
        print (text)
        update.message.reply_text(text_answer_3)
    else:
        text = update.message.text
        random_sticker_number = randint(0,4)
        if random_sticker_number == 0:
            sticker_bot = 'CAACAgIAAxkBAAEDV3xhnBTrsL951NGnA5hi9iQULPVnFAACeQADkkPGLdMIosFTpWvhIgQ'
        elif random_sticker_number == 1:
            sticker_bot = 'CAACAgIAAxkBAAEDV4JhnBhF-RshQSAgw8l9np9QRrJZtgACeQIAAladvQr_E3Q_a7YvniIE'
        elif random_sticker_number == 2:
            sticker_bot = 'CAACAgEAAxkBAAEDV4RhnBhi77WVJxOwU5s952HWo5g0JwAC5ggAAuN4BAAB2g8zsbmcSxEiBA'
        elif random_sticker_number == 3:
            sticker_bot = 'CAACAgIAAxkBAAEDV4ZhnBi0d9BfxUohJbODUKoosuINgQACSQEAAntOKhDSitDV6aV93yIE'
        else:
            sticker_bot = 'CAACAgQAAxkBAAEDV4hhnBj64mhT-1_v3we8tQUgzz0LEQACZgADgBs8A5etJKHD5zZ5IgQ'    
        print (text)
        update.message.reply_sticker(sticker_bot)

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()