import discord
from discord.ext import commands

class DND_Commands(commands.Cog):
    """
    List of commands for handling DND related tasks
    """
    def __init__(self, client):
        self.client = client
        self.ai_cog = self.client.get_cog("AI_Commands")
        self.data_cog = self.client.get_cog("Data_Commands")
        
    @commands.command(alias=["desc", "des"],
                      description="Describe an object in detail with AI")
    async def describe(self, ctx, *, object: str):
        msg = "Describe in one or two sentences: " + object
        reply = await self.ai_cog.get_openai_response("You explain objects from a magical and mysterious world.", msg)
        await ctx.send(reply)


async def setup(client):
    await client.add_cog(DND_Commands(client))