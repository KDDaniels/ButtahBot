#!/usr/bin/env python

"""

"""

import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'\033[92m[INFO]\033[0m We have logged in as \033[96m{bot.user}\033[0m')

    # Loads all of the cogs in the ./cogs folder
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'\033[92m[INFO]\033[0m Loaded cog from \033[96m{filename}\033[0m')
            except Exception as e:
                print(f'\033[91m[ERROR]\033[0m Failed to load cog in \033[96m{filename}\033[0m: {e}')

    print(f'\033[92m[INFO]\033[0m Cogs done loading.')

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return

if __name__ == "__main__":
    try:
        bot.run(os.environ["BUTTAHBOT_TOKEN"])
    except Exception as e:
        print(f'\033[91m[ERROR]\033[0m Error: {e}')