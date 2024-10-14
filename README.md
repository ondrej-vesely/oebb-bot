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

## Deploying
To sure the script periodically checks the booking availability (and if don't have access to  24/7 running system where you can schedule this), I recommend deploying to Modal (*the 30$ of credits you currently get with free tier should cover you completely here*).

1. Go to [modal.com](https://modal.com/) and create a new account
2. `pip install modal`
3. `python -m modal setup`
4. `modal deploy modal_deploy.py`

The [modal_deploy.py](./modal_deploy.py) contains all the deployment parameters , including the scheduling. To adjust the scheduled run times, you can either use:

 * `schedule=modal.Period(days=1)`          to simply run daily
 * or `schedule=modal.Cron("00 07,17 * * *")`  using Cron syntax to run daily eg. at 7:00 & 17:00*

*the Cron times are in UTC time, so don't forget to adjust for your local time zone