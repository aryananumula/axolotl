import os

import colorama
import interactions

bot = interactions.Client()


@interactions.listen()
async def on_startup():
    print(colorama.Fore.BLUE + "Bot is ready!" + colorama.Style.RESET_ALL)


@interactions.listen()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


print(os.environ.get("AXOLOTL_TOKEN"))
bot.start(os.environ.get("AXOLOTL_TOKEN"))
