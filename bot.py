from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime, time, date, timedelta

import settings
import logging
import ephem

logging.basicConfig(filename='bot.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print ('Вызван /start')
    print (update)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

# задание по ссылке: https://learn.python.ru/lessons/tasks_lesson2.html?full#4
def def_next_full_moon (update, context):
    datetime_marks = ['.', '-', '/', '\\']
    user_date = update.message.text
    user_date = user_date.replace('/next_full_moon', '')
    for datetime_mark in datetime_marks:
        user_date = user_date.replace(datetime_mark, '/')
    try:
        next_full_moon_user_date = ephem.next_full_moon(user_date)
        text_answer = f"Ближайшее полнолуние от указанной Вами даты: {next_full_moon_user_date}"
    except ValueError:
        text_answer = "В поле с командой должна быть указана только дата в формате YYYY-MM-DD!"
    update.message.reply_text(text_answer)  

# задание по ссылке: https://learn.python.ru/lessons/tasks_lesson2.html?full#3    
def wordcount_user(update, context):
    none_element = ''
    punctuation_marks = ['!', '.', ',', '?', '"', "'", ']', '[', '@', '#', '$', '%', '^', "&", '*', '(', ')', '_', '-', '+', '=',
                         '}', '{', ';', ':', '>', "<", '/', "|", '~', "\\", '`']
    user_wordcount = update.message.text
    for punctuation_mark in punctuation_marks:
        user_wordcount = user_wordcount.replace(punctuation_mark, '')
    wordcount_split = user_wordcount.split(' ')
    wordcount_split.pop(0)
    while none_element in wordcount_split:
        wordcount_split.remove(none_element)
    wordcount_score = len(wordcount_split)
    if wordcount_score > 0:
        text_answer = f"Предложение содержит {wordcount_score} слова или слов."
    else:
        text_answer = "Предложение не содержит слов или иных конвертируемых для расчета значений!"
    update.message.reply_text(text_answer)  

def talk_to_me(update, context):
    text = update.message.text
    print (text)
    def answer_print (text_answer):
        update.message.reply_text(text_answer)  
    random_talk_number = randint(0,4)  
    if random_talk_number == 0:
        text_answer = 'Приму это к сведению! Может быть, может быть...'
        answer_print(text_answer)
    elif random_talk_number == 1:
        text_answer = f'{text} - говоришь ты) а я что? Я примус починяю!'
        answer_print(text_answer)
    elif random_talk_number == 2:
        text_answer = text[::-1]
        answer_print(text_answer)
    elif random_talk_number == 3:
        text_splits = text.split()
        for word in reversed(text_splits):
            text_splits.append(word[::-1])
            text_splits.remove(word)
            text_splits_reversed = text_splits
        for reverse_word in reversed(text_splits_reversed):
            text_splits_reversed.append(reverse_word)
            text_splits_reversed.remove(reverse_word)
            text_answer = ' '.join(text_splits_reversed)            
        answer_print(text_answer)
    else:
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
        update.message.reply_sticker(sticker_id)

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount_user))
    dp.add_handler(CommandHandler("next_full_moon", def_next_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()