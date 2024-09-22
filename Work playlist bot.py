import logging
import telegram
import random
import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Список плейлистов
PLAYLISTS = [
    "https://music.yandex.ru/users/yamusic-sound/playlists/1016",
    "https://music.yandex.ru/users/music-blog/playlists/1587",
    "https://music.yandex.ru/users/music.partners/playlists/1398",
    "https://music.yandex.ru/users/music-blog/playlists/2620",
    "https://music.yandex.ru/users/music-blog/playlists/2400"
    "https://music.yandex.ru/users/music-blog/playlists/2389"
]

nest_asyncio.apply()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляем приветственное сообщение и рекомендации плейлиста."""
    user_first_name = update.effective_user.first_name
    playlist = random.choice(PLAYLISTS)
    message = f"Привет, {user_first_name}! Вот тебе плейлист для продуктивной работы:\n{playlist}"
    await update.message.reply_text(message)

async def playlist_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет случайный плейлист."""
    playlist = random.choice(PLAYLISTS)
    await update.message.reply_text(f"Вот твой плейлист для работы:\n{playlist}")

def main():
    """Запуск бота."""
    token = "YOUR_TELEGRAM_BOT_API_TOKEN"  # Замените на ваш токен
    
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("playlist", playlist_command))

    application.run_polling()

if __name__ == '__main__':
    main()


