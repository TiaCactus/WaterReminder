from typing import Final

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN: Final = '6137330496:AAEQJf5HDo5IIukp8CIDwHqMBxMj3avNpDg'
BOT_USERNAME: Final = '@Water5bot'
  
# Set the time range for reminders (8:30 to 22:30)
start_time = datetime.time(8, 30)
end_time = datetime.time(22, 30)

# Set the interval between reminders (1.5 hours)
interval = datetime.timedelta(hours=1, minutes=30)

# Define a function to send the milk glass emoji message
def send_milk_glass(context):
    bot = context.bot
    chat_id = context.job.context
    bot.send_message(chat_id=chat_id, text='🥛')

# Define a function to start the reminders
def start(update, context):
    chat_id = update.effective_chat.id
    context.job_queue.run_repeating(send_milk_glass, interval, first=datetime.datetime.combine(datetime.date.today(), start_time), context=chat_id)
    update.message.reply_text('Milk glass reminders have been started!')

# Define a function to stop the reminders
def stop(update, context):
    chat_id = update.effective_chat.id
    context.job_queue.stop()
    update.message.reply_text('Milk glass reminders have been stopped.')

# Create an Updater object and set up the CommandHandlers
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stop', stop))

# Start the bot
updater.start_polling()
updater.idle()



