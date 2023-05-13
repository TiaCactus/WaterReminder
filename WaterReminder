import telepot
import time
import datetime

# Replace 'BOT_TOKEN' with your own bot token
bot = telepot.Bot('6137330496:AAEQJf5HDo5IIukp8CIDwHqMBxMj3avNpDg')

# Replace 'CHAT_ID' with your own chat ID
chat_id = '30400541'

# Set start and end times for reminders
start_time = datetime.time(8, 30)
end_time = datetime.time(22, 30)

# Set reminder interval in seconds
interval = 5400  # 1.5 hours

while True:
    # Get current time
    current_time = datetime.datetime.now().time()
    
    # Check if current time is within reminder window
    if current_time >= start_time and current_time <= end_time:
        # Send reminder message
        bot.sendMessage(chat_id, '🥛')
    
    # Wait for interval before checking time again
    time.sleep(interval)
