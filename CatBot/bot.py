import time
from telegram import Bot

chat_id = 123 #Ваш чат id
bot = Bot("YOUR TOKEN")

def send_random_cat():
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(chat_id, url)

def main() -> None:
    send_random_cat()
    print("К тебе котик!)")

if __name__ == "__main__":
    main()