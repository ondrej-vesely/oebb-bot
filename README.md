# ÖBB (Nightjet) Bot

Want to book ticket for your Christmas sleeper train journey but no tickets are available yet? This bot can notify you when your desired holiday travel date becomes available for booking.

Nightjet ticket sales generally start 180 days prior to departure, but travelling dates after the annual timetable change in mid-December may be subject to shorter irregular booking periods (often less than two months).

This script uses `python-telegram-bot` package to send you Telegram notifications to your phone or PC.


## Setting up the Telegram
You can follow the detailed steps of setting up the Telegram bot in the [Notebook](./oebb-bot.ipynb).

*tl;dr* If you've already created Telegram bots before, you just need to:
1. Create a new bot and store its API token in `.env` file under `TELEGRAM_BOT_TOKEN`
2. Add it to a chat group and store the group's Chat ID in `.env` file under `TELEGRAM_CHAT_ID`

## Changing booking date
The date the script will check for is defined in the `.env` file as well.
You can change it under `BOOKING_DATE` key using `YYYY-mm-dd` format.