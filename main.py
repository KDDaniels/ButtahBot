#!/usr/bin/env python

"""
    ButtahBot is a hobby Discord bot to just do goofy stuff with.
    Copyright (C) 2024 Kendall Daniels

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


    
    Fun little Discord bot I've made for my friends and I to goof around with,
    probably won't add anything too complicated unless it sounds neat (e.g. TTS)
"""

import os
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'\033[92m[INFO]\033[0m We have logged in as \033[96m{bot.user}\033[0m')
    await bot.change_presence(activity=discord.CustomActivity(name='Loading...'))

    # Loads all of the cogs in the ./cogs folder
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'\033[92m[INFO]\033[0m Loaded cog from \033[96m{filename}\033[0m')
            except Exception as e:
                print(f'\033[91m[ERROR]\033[0m Failed to load cog in \033[96m{filename}\033[0m: {e}')

    await bot.change_presence(activity=discord.CustomActivity(name='Done!'))
    await asyncio.sleep(1)
    await bot.change_presence(activity=None)
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