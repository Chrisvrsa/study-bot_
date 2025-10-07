import asyncio
from datetime import datetime, timedelta

# Key = user_id, Value = dict with end time and asyncio task
pomodoro_timers = {}

#25 minutes. Each minute has 60 seconds
POMODORO_DURATION = 25 * 60 

async def start_pomodoro(ctx):
    user_id = ctx.author.id
    
    # Check if a timer is running already
    if user_id in pomodoro_timers:
        await ctx.send(f"You already have a Pomodoro running! Use `!pomodoro status` to check it's status.")
        return
    
    end_time = datetime.now() + timedelta(seconds=POMODORO_DURATION)
    
    task = asyncio.create_task(pomodoro_timer(ctx, user_id, POMODORO_DURATION))
    pomodoro_timers[user_id] = {
        "task": task,
        "end_time": end_time
    }
    
    await ctx.send(f"🍅 Pomodoro started! I'll notify you in 25 minutes. Use `!pomodoro status` to check progress.")
