import dotenv, os
import requests
import asyncio
from datetime import datetime
from telegram import Bot 

dotenv.load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
BOOKING_DATE = datetime.strptime(os.getenv("BOOKING_DATE"), "%Y-%m-%d")

async def send_message(bot, message, chat_id):
    await bot.send_message(text=message, chat_id=chat_id)

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    page_data = requests.post("https://www.nightjet.com/nj-booking-ocp/init/start", json={"lang": "en"})

    if page_data.ok:
        max_bookable_date = datetime.strptime(page_data.json()["maxBookableDate"], "%Y-%m-%d")

        if max_bookable_date >= BOOKING_DATE:
            message = f"🔥🚨 Tickets are available for {BOOKING_DATE.date()}! 🚨🔥"
        else:
            message = f"⏳ No luck with booking for {BOOKING_DATE.date()} yet."""
    else:
        message = "😢 Couldn't get required data from Nightjet booking website."

    asyncio.run(send_message(bot, message, chat_id=TELEGRAM_CHAT_ID))

if __name__ == "__main__":
    main()