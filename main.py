#!/usr/bin/env python

import os
import discord
from discord.ext import commands

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension(f'cogs.{filename[:-3]}')
                    print(f'[INFO] Loaded cog {filename[:-3]}')
                except Exception as e:
                    print(f'[ERROR] Failed to load cog {filename[:-3]}: {e}')

        
        print(f'We have logged in as {bot.user}')

    bot.run(os.environ["BUTTAHBOT_TOKEN"])