# 🚄🌙 ÖBB (Nightjet) Bot 

Want to use those comfy Austrian sleeper trains for you holiday travels but there are no tickets available yet? Tired of waiting for ÖBB to update their timetables? This bot can notify you when your desired travel date becomes available for booking!

> Ticket sales generally start 180 days prior to departure. Travelling dates after the annual timetable change in mid-December may, however, be subject to shorter booking periods.
(from [Nightjet FAQ](https://www.nightjet.com/en/buchung/faq/buchung-im-nightjet))

This script uses `python-telegram-bot` package to send you Telegram notifications about ticket avaibility to your phone or PC.

## Setting up the Telegram
You can follow the detailed steps of setting up the Telegram bot in the [Notebook](./oebb-bot.ipynb).

**tl;dr** If you've already created Telegram bots before, you need to:
1. Create a new bot and store bot's API token in `.env` file as `TELEGRAM_BOT_TOKEN`
2. Add it to a chat group and store the group's Chat ID in `.env` file as `TELEGRAM_CHAT_ID`

## Changing booking date
The booking date to check for is defined in the `.env` file.
You can change the `BOOKING_DATE` value using `YYYY-mm-dd` format.

## Deploying
To run the bot periodically (if you don't have access to your own 24/7 running system), I recommend deploying to Modal (*the 30$ of credits you get with free tier should cover you completely*).

1. Go to [modal.com](https://modal.com/) and create a new account
2. `pip install modal`
3. `python -m modal setup`
4. `modal deploy modal_deploy.py`

The [modal_deploy.py](./modal_deploy.py) contains all the deployment parameters , including the scheduling. To adjust the scheduled run times, you can use:

 * `schedule=modal.Period(days=1)`          to simply run daily
 * `schedule=modal.Cron("00 07,17 * * *")`  Cron to run daily eg. at 7:00 & 17:00*

*the cron syntax uses UTC time, so don't forget to adjust for your local time zone