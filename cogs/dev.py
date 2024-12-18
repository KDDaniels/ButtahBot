import discord
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
        await self.client.close()
        print('\033[93m[INFO]\033[0m Bot has shut down. Exiting...')
    

async def setup(client):
    await client.add_cog(Dev_Commands(client))