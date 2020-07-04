from telegram.ext import Updater, CommandHandler
from bs4 import BeautifulSoup
import requests
import re


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_dog_image_url():
    allowed_extension = ['jpeg', 'jpg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_cat_image_url():
    allowed_extension = ['jpeg', 'jpg', 'png']
    file_extension = ''
    
    while file_extension not in allowed_extension:
        url = 'https://random.cat/'
        website = requests.get(url)
        soup = BeautifulSoup(website._content, 'html.parser')
        url = soup.find(id='cat')['src']
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
    


def cat(bot, update):
    image_url = get_cat_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=image_url)

def dog(bot, update):
    image_url = get_dog_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=image_url)

def main():
    updater = Updater('ENTER TOKEN HERE')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog',dog))
    dp.add_handler(CommandHandler('cat',cat))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
