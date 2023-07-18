import time
from telegram import Bot

chat_id = 386169113
bot = Bot("6083437663:AAGBK_jPNeSJs5qoL0guWhnSNz1nRlWcX5o")

def send_random_cat():
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(chat_id, url)

def main() -> None:
    send_random_cat()
    print("К тебе котик!)")

if __name__ == "__main__":
    main()