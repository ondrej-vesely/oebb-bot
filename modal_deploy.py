import modal
import oebb_bot


app = modal.App("oebb-bot")
image = (
    modal.Image.debian_slim(python_version="3.10")
    .pip_install("python-dotenv")
    .pip_install("python-telegram-bot")
    .pip_install("requests")
)

@app.function(
    image=image,
    secrets=[modal.Secret.from_dotenv()],
    #schedule=modal.Period(days=1),         # run daily
    schedule=modal.Cron("00 07,17 * * *"),  # run daily at 7:00 & 17:00
)
def main():
    oebb_bot.main()