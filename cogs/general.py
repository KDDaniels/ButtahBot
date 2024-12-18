from discord.ext import commands

class General_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

async def setup(client):
    await client.add_cog(General_Commands(client))