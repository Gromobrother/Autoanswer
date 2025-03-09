from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Привет! Я ваш бот-автопоответчик.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater("8162715791:AAGpT1xBJO46j_v9RlvSjuV8RZyM4K6wVMY", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()