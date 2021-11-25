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
    def answer_print (text, text_answer):
        print (text)
        update.message.reply_text(text_answer)  
    random_talk_number = randint(0,4)  
    if random_talk_number == 0:
        text = update.message.text
        text_answer = 'Приму это к сведению! Может быть, может быть...'
        answer_print(text, text_answer)
    elif random_talk_number == 1:
        text = update.message.text
        text_answer = f'{text} - говоришь ты) а я что? Я примус починяю!'
        answer_print(text, text_answer)
    elif random_talk_number == 2:
        text = update.message.text
        text_answer = text[::-1]
        answer_print(text, text_answer)
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
            text_answer = ' '.join(text_splits_reversed)            
        answer_print(text, text_answer)
    else:
        text = update.message.text
        stickers_id = ['CAACAgIAAxkBAAEDV3xhnBTrsL951NGnA5hi9iQULPVnFAACeQADkkPGLdMIosFTpWvhIgQ',
                       'CAACAgIAAxkBAAEDV4JhnBhF-RshQSAgw8l9np9QRrJZtgACeQIAAladvQr_E3Q_a7YvniIE',
                       'CAACAgEAAxkBAAEDV4RhnBhi77WVJxOwU5s952HWo5g0JwAC5ggAAuN4BAAB2g8zsbmcSxEiBA',
                       'CAACAgIAAxkBAAEDV4ZhnBi0d9BfxUohJbODUKoosuINgQACSQEAAntOKhDSitDV6aV93yIE',
                       'CAACAgQAAxkBAAEDV4hhnBj64mhT-1_v3we8tQUgzz0LEQACZgADgBs8A5etJKHD5zZ5IgQ',
                       'CAACAgIAAxkBAAEDWiFhnhOC3401IPsnRdAM3oaZIlUxjwACoAADq1fEC2nC4av5TKV7IgQ',
                       'CAACAgIAAxkBAAEDWiNhnhOLbCB8-UH0IcKAQRIch25a8gACLQADOcGJDNQzp1v1ga4qIgQ',
                       'CAACAgIAAxkBAAEDWiVhnhOhUXhLiXu__1qG2OfJ5Sd-0gACIAEAArhdDQABIeLrSJePA_QiBA',
                       'CAACAgQAAxkBAAEDWidhnhOkr5APAgX0A7-iswRP9nNtjwACJwAD9ZhQCxU-2boU4tbCIgQ',
                       'CAACAgIAAxkBAAEDWilhnhOsZQAB_fIvssodp0HLRZYO6h0AAjMUAAILcJhKyY19ErwBvuoiBA']
        random_sticker_number = randint(0,9)
        sticker_id = stickers_id [random_sticker_number]
        print (text)
        update.message.reply_sticker(sticker_id)

def answer_step_1 ():
    text = update.message.text
    text_answer = 'Приму это к сведению! Может быть, может быть...'
    print (text)
    update.message.reply_text(text_answer)

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