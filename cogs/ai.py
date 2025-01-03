import os
import openai
from discord.ext import commands

class AI_Commands(commands.Cog):
    """
    List of commands handling OpenAI related stuff
    e.g. asking questions, changing personality, etc
    """
    def __init__(self, client):
        self.client = client
        self.tokens = 0
        self.personality = "You answer questions in a short paragraph"
        openai.api_key = os.environ["OPENAI_API_KEY"]

    async def get_openai_response(self, role, prompt):
        try:
            messages = [
                    {"role": "system", "content": role},
                    {"role": "user", "content": prompt}
                ]
            
            response = openai.chat.completions.create(
                model = "gpt-4o-mini",
                messages = messages,
                temperature = 0.7,
                # max_tokens = 150,
            )

            self.tokens += response.usage.total_tokens
            print(f"\033[92m[INFO]\033[0m Tokens used: {response.usage.total_tokens}; Total: {self.tokens}")
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"\033[91m[ERROR]\033[0m Error getting response: {e}")
            return "father help, I am having issues"
        
    @commands.command()
    async def personality(self, ctx, *, personality: str):
        self.personality = personality + " You respond in a short paragraph."
        print(f"\033[92m[INFO]\033[0m Personality changed to: {personality}")
        await ctx.send(f"Personality changed to: {personality}.")

    @commands.command()
    async def ask(self, ctx, *, question: str):
        reply = await self.get_openai_response(self.personality, question)
        await ctx.send(reply)



async def setup(client):
    await client.add_cog(AI_Commands(client))