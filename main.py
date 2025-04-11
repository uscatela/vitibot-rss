import feedparser
import time
import telebot

# Вставь сюда свой Telegram API Token
API_TOKEN = '8109236901:AAFre_lPPvXhM8pJIRsGBygRTBdqI47HVZk'

# ID твоего чата (пока оставим пустым, добавим позже)
CHAT_ID = 'ТВОЙ_CHAT_ID'

# RSS ссылка на Авито — сюда можно вставить отфильтрованную ссылку
RSS_URL = 'https://example.com/rss'  # заменим позже

bot = telebot.TeleBot(API_TOKEN)
seen_entries = set()

def check_feed():
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries:
        if entry.id not in seen_entries:
            seen_entries.add(entry.id)
            message = f"🆕 Новое объявление:\n\n{entry.title}\n{entry.link}"
            bot.send_message(CHAT_ID, message)

# Бесконечный цикл проверки
while True:
    try:
        check_feed()
    except Exception as e:
        print(f"Ошибка: {e}")
    time.sleep(60)  # Проверка каждые 60 сек
