import logging
import os

import colorama
import dotenv
import interactions
from colorama import Fore, Style

dotenv.load_dotenv()

colorama.init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    LOG_COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.LOG_COLORS.get(record.levelno, Fore.WHITE)
        record.msg = f"{log_color}{record.msg}{Style.RESET_ALL}"
        return super().format(record)


logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)


formatter = ColoredFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


ch.setFormatter(formatter)


logger.addHandler(ch)

bot = interactions.Client(
    intents=interactions.Intents.DEFAULT | interactions.Intents.MESSAGE_CONTENT,
    sync_interactions=True,
    logger=logger,
)


@interactions.listen()
async def on_startup():
    print(colorama.Fore.BLUE + "Bot is ready!")


@interactions.slash_command(name="ping", description="Ping the bot")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


def startBot():
    bot.start(os.environ.get("AXOLOTL_TOKEN"))
