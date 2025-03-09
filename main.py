
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Установка logger'а
logger = logging.getLogger(__name__)

# Токен бота
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Замените на ваш токен

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /start."""
    user = update.effective_user
    await update.message.reply_text(f"Привет, {user.first_name}! Я бот-автоответчик. Напишите мне сообщение, и я отвечу.")

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /help."""
    await update.message.reply_text("Это бот-автоответчик. Просто напишите мне, и я отвечу!")

# Автоответчик на сообщения
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отвечает на сообщение пользователя."""
    text = update.message.text
    
    # Здесь вы можете настроить различные ответы на разные типы сообщений
    if "привет" in text.lower():
        reply = "Привет! Как я могу помочь вам сегодня?"
    elif "помощь" in text.lower():
        reply = "Я бот-автоответчик. Что вас интересует?"
    elif "спасибо" in text.lower():
        reply = "Всегда рад помочь!"
    else:
        reply = "Спасибо за ваше сообщение! К сожалению, в данный момент никого нет на месте. Мы свяжемся с вами как можно скорее."
    
    await update.message.reply_text(reply)

def main() -> None:
    """Запуск бота."""
    # Создаем приложение и передаем ему токен бота
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Обрабатываем все текстовые сообщения
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
