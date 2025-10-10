import asyncio
from datetime import datetime, timedelta

# Key = user_id, Value = dict with end time and asyncio task
pomodoro_timers = {}

#25 minutes. Each minute has 60 seconds. This is the standard duration for a Pomodoro timer.
POMODORO_DURATION = 25 * 60 
BREAK_DURATION = 5 * 60


async def start_pomodoro(ctx, options=None):
    user_id = ctx.author.id
    
    # Check if a timer is running already
    if user_id in pomodoro_timers:
        await ctx.send("You already have a Pomodoro running! Use `!pomodoro status` to check it's status. Cancel it with `!pomodoro cancel`.")
        return
    
    end_time = datetime.now() + timedelta(seconds=POMODORO_DURATION)
    
    task = asyncio.create_task(pomodoro_timer(ctx, user_id, POMODORO_DURATION))
    
    pomodoro_timers[user_id] = {
        "task": task,
        "end_time": end_time
    }
    
    await ctx.send("🍅 Pomodoro started! I'll notify you in 25 minutes. Use `!pomodoro status` to check progress.")



async def pomodoro_timer(ctx, user_id, duration):
    try:
        await asyncio.sleep(duration)
        await ctx.send(f"⏰ Time's up, {ctx.author.mention}! You did great! 👏 Break time! ☕")
        
        pomodoro_timers.pop(user_id, None)
        await break_pomodoro(ctx)
        
    except asyncio.CancelledError:
        await ctx.send("Pomodoro cancelled!")
        pomodoro_timers.pop(user_id, None)
    
      
async def cancel_pomodoro(ctx):
    user_id = ctx.author.id
    
    if user_id in pomodoro_timers:
        task = pomodoro_timers[user_id]["task"]
        task.cancel()
        pomodoro_timers.pop(user_id, None)
        
    else:
        await ctx.send(f"{ctx.author.mention}, you don't have a Pomodoro running!")
        
        
# gets called automatically when the pomodoro timer is done
async def break_pomodoro(ctx):
    await asyncio.sleep(BREAK_DURATION)
    await ctx.send("Your break is set for 5 minutes! I'll notify you when it's over.")
    await ctx.send(f"⏰ Time's up, {ctx.author.mention}! You did great! 👏 Back to work! Starting again? Use `!pomodoro start`")
        
    
def get_status(user_id):
    if user_id in pomodoro_timers:
        end_time = pomodoro_timers[user_id]["end_time"]
        remaining = (end_time - datetime.now()).total_seconds()
        return max(0, int(remaining))
    return None 
    
    

