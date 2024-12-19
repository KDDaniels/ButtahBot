import discord
import asyncio
import io
from RealtimeTTS import TextToAudioStream, CoquiEngine
from discord.ext import commands

class TTS_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.engine = None
        self.stream = None
        self.voice = None


    async def initialize(self):
        self.engine = CoquiEngine()
        self.stream = TextToAudioStream(self.engine)
   


    @commands.command(aliases=["s"])
    async def speak(self, ctx, *, text: str):
        if ctx.voice_client and ctx.voice_client.is_connected():
            if not self.engine or not self.stream:
                await ctx.send("\033[91m[ERROR]\033[0m TTS is not initialized yet.")
                return
            
            if not self.voice:
                self.voice = ctx.channel.guild.voice_client

            self.stream.feed(text)
            self.stream.play_async(output_wavfile="./audio/speech.wav", muted=True)
            while self.stream.is_playing():
                await asyncio.sleep(0.1)

            self.voice.play(discord.FFmpegPCMAudio("./audio/speech.wav"))
            while self.voice.is_playing():
                await asyncio.sleep(0.1)
        else:
            await ctx.send("I'm not in a voice channel ya goober.")


    @commands.command(aliases=["cv"])
    async def change_voice(self, ctx, num=0):
        self.voices = self.engine.get_voices()
        if num == -1:
            for index, voice in enumerate(self.voices, start=1):
                print(f"{index}. {voice}")
        else:
            _voice = self.voices[num]
            self.engine.set_voice(_voice)
            await self.speak(ctx, text=f'This is the voice of {_voice}')
        

async def setup(client):
    try:
        tts_cog = TTS_Commands(client)
        await tts_cog.initialize()
        await client.add_cog(tts_cog)
    except Exception as e:
        print(f'\033[91m[ERROR]\033[0m {e}')
        raise