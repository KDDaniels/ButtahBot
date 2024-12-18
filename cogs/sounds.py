import discord
import asyncio
from discord.ext import commands



class Sound_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def join(self, ctx):
        current_channel = ctx.author.voice.channel
        await current_channel.connect()

    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(aliases=["play", "p"])
    async def play_sound(self, ctx, sound=None):
        if not discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild):
            await self.join(ctx)

        if sound != None:
            print(f'\033[92m[INFO]\033[0m Playing \033[96m{sound}\033[0m.')
            await asyncio.sleep(1)
            try:
                voice = ctx.channel.guild.voice_client
                voice.play(discord.FFmpegPCMAudio(f'./audio/{sound}.mp3'))
                while voice.is_playing():
                    await asyncio.sleep(0.5)
                await self.leave(ctx)
            except NameError:
                await ctx.send('Audio file not found, check your spelling.')


async def setup(client):
    await client.add_cog(Sound_Commands(client))