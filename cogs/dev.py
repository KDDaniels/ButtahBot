import discord
import os
from discord.ext import commands

class Dev_Commands(commands.Cog):
    """
    Dev contains all of the dev commands for ButtahBot
    """
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        """
        Basic reply for quick testing
        """
        await ctx.send("Hello!")

    @commands.command(aliases=["quit", "q", "sd"])
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        """
        Shuts down the bot through a command
        """
        await ctx.send("Later nerds!")
        await self.client.close()
        print('\033[93m[INFO]\033[0m Bot has shut down. Exiting...')

    @commands.command(aliases=["r"])
    @commands.has_permissions(administrator=True)
    async def reload_cog(self, ctx, cog=None):
        if cog is None:
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    try:
                        await self.client.reload_extension(f'cogs.{filename[:-3]}')
                        print(f'\033[92m[INFO]\033[0m Reloaded cog from \033[96m{filename}\033[0m')
                        await ctx.send(f"[INFO] Reloaded cog from {filename}")
                    except Exception as e:
                        print(f'\033[91m[ERROR]\033[0m Failed to load cog in \033[96m{filename}\033[0m: {e}')
            
        elif cog == "list":
            cog_list = ["Cogs:\n"]
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    filename = filename.replace('.py', '\n')
                    cog_list.append(filename)
            cogs = ''.join(str(x) for x in cog_list)
            await ctx.send(cogs)
        else:
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    try:
                        if filename[:-3] == cog:
                            await self.client.reload_extension(f'cogs.{filename[:-3]}')
                            print(f'\033[92m[INFO]\033[0m Reloaded cog from \033[96m{filename}\033[0m')
                            await ctx.send(f'[INFO] Reloaded cog from {filename}')
                    except Exception as e:
                        print(f'\033[91m[ERROR]\033[0m Failed to load cog in \033[96m{filename}\033[0m: {e}')

async def setup(client):
    await client.add_cog(Dev_Commands(client))