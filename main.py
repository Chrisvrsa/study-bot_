import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv
from pomodoro import start_pomodoro, get_status, cancel_pomodoro
from flashcards import init_db, add_flashcard, get_random_flashcard
init_db()

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
async def manual(ctx):
    await ctx.send("\n`!pomodoro start` Start a pomodoro timer!\n`!pomodoro status` Check the status of your pomodoro timer!\n`!pomodoro cancel` Cancel your pomodoro timer\n\nAdditional documentation can be found at https://github.com/Chrisvrsa/study-bot_")
    

@bot.group()
async def pomodoro(ctx):
    """Main pomodoro command group."""
    if ctx.invoked_subcommand is None:
        await start_pomodoro(ctx)
    
    
@pomodoro.command(name="status")
async def pomodoro_status(ctx):
    user_id = ctx.author.id
    remaining = get_status(user_id)
    
    if remaining is None:
        await ctx.send(f"{ctx.author.display_name}, you haven't started a pomodoro yet!")
        return

    minutes = remaining // 60
    seconds = remaining % 60
    await ctx.send(f"⏱️ {ctx.author.display_name}, your pomodoro has {minutes} minutes and {seconds} seconds remaining!")
    
    
@pomodoro.command(name="cancel")
async def pomodoro_cancel(ctx):
    
    await cancel_pomodoro(ctx)
    

@bot.command()
async def card(ctx, *, content: str):
    """Adds a flashcard using: !card add "Question" | "Answer" """
    user_id = ctx.author.id

    # Split question and answer
    if "|" not in content:
        await ctx.send("⚠️ Format: !card add \"Question\" | \"Answer\"")
        return

    parts = content.split("|")
    question = parts[0].strip('" ').strip() # removes space and '"'
    answer = parts[1].strip('" ').strip()

    # Save it
    add_flashcard(user_id, question, answer)
    await ctx.send(f"✅ Added flashcard!\n**Q:** {question}\n**A:** {answer}")
    
    
@bot.command()
async def quiz(ctx):
    """Ask the user a random flashcard question."""
    user_id = ctx.author.id
    card = get_random_flashcard(user_id)

    if not card:
        await ctx.send("❌ You don't have any flashcards yet! Add one with `!card add \"Question\" | \"Answer\"`.")
        return

    _, question, answer = card
    await ctx.send(f"🧠 **Question:** {question}\nReply with your answer!")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await ctx.bot.wait_for("message", check=check, timeout=60)
        if msg.content.strip().lower() == answer.lower():
            await ctx.send("✅ Correct! Nice job! 🎉")
        else:
            await ctx.send(f"❌ Not quite! The correct answer was: **{answer}**.")
    except asyncio.TimeoutError:
        await ctx.send(f"⌛ Time's up! The answer was: **{answer}**.")
    
    
    
bot.run(BOT_TOKEN)