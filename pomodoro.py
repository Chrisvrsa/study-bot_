import asyncio
from datetime import datetime, timedelta

# Key = user_id, Value = dict with end time and asyncio task
pomodoro_timers = {}

#25 minutes. Each minute has 60 seconds. This is the standard duration for a Pomodoro timer.
POMODORO_DURATION = 25 * 60 

async def start_pomodoro(ctx):
    user_id = ctx.author.id
    
    # Check if a timer is running already
    if user_id in pomodoro_timers:
        await ctx.send("You already have a Pomodoro running! Use `!pomodoro status` to check it's status.")
        return
    
    end_time = datetime.now() + timedelta(seconds=POMODORO_DURATION)
    
    task = asyncio.create_task(pomodoro_timer(ctx, user_id, POMODORO_DURATION))
    
    pomodoro_timers[user_id] = {
        "task": task,
        "end_time": end_time
    }
    
    await ctx.send("🍅 Pomodoro started! I'll notify you in 25 minutes. Use `!pomodoro status` to check progress.")


async def pomodoro_timer(ctx, user_id, duration):
    await asyncio.sleep(duration)
    await ctx.send(f"⏰ Time's up, {ctx.author.mention}! You did great! 👏 Break time! ☕")
    pomodoro_timers.pop(user_id, None)
    
    
    
def get_status(user_id):
    if user_id in pomodoro_timers:
        end_time = pomodoro_timers[user_id]["end_time"]
        remaining = (end_time - datetime.now()).total_seconds()
        return max(0, int(remaining))
    return None 