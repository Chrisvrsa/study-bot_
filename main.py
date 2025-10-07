import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment and grab token from discord
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')


# Set up command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.display_name}! 👋")

bot.run(discord_token)