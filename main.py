import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from pomodoro import start_pomodoro, get_status

# Load environment and grab token from discord
load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')


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
    
@bot.command()
async def pomodoro(ctx):
    await start_pomodoro(ctx)
    
@bot.command()
async def pomodoro_status(ctx):
    user_id = ctx.author.id
    remaining = get_status(user_id)
    
    if remaining is None:
        await ctx.send(f"{ctx.author.display_name}, you haven't started a pomodoro yet! 😂")
        return

    minutes = remaining // 60
    seconds = remaining % 60
    await ctx.send(f"⏱️ {ctx.author.display_name}, your pomodoro has {minutes} minutes and {seconds} seconds remaining!")


bot.run(BOT_TOKEN)