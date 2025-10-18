import asyncio
from datetime import datetime, timedelta

# Key = user_id, Value = dict with end time and asyncio task
pomodoro_timers = {}

# 25 minutes. Each minute has 60 seconds. This is the default duration for a Pomodoro timer.
POMODORO_DURATION = 25 * 60

# 50 minutes. Uses BREAK_DURATION_LONG and extends the default. (10 minute break, 50 minute timer)
POMODORO_DURATION_LONG = (POMODORO_DURATION) * 2 


BREAK_DURATION = 5 * 60
BREAK_DURATION_LONG = (BREAK_DURATION) * 2



# default
async def start_pomodoro(ctx):
    user_id = ctx.author.id

    # Check if a timer is running already
    if user_id in pomodoro_timers:
        await ctx.send(
            "You already have a Pomodoro running! Use `!pomodoro status` to check it's status. Cancel it with `!pomodoro cancel`."
        )
        return

    end_time = datetime.now() + timedelta(seconds=POMODORO_DURATION)

    task = asyncio.create_task(pomodoro_timer(ctx, user_id)) # default call to pomodoro_timer

    pomodoro_timers[user_id] = {"task": task, "end_time": end_time}

    await ctx.send(
        "🍅 Pomodoro started! I'll notify you in 25 minutes. Use `!pomodoro status` to check progress."
    )


async def long_pomodoro(ctx):
    user_id = ctx.author.id

    # Check if a timer is running already
    if user_id in pomodoro_timers:
        await ctx.send(
            "You already have a Pomodoro running! Use `!pomodoro status` to check it's status. Cancel it with `!pomodoro cancel`."

        )
        return
    
    end_time = datetime.now() + timedelta(seconds=POMODORO_DURATION_LONG)

    task = asyncio.create_task(pomodoro_timer(ctx, user_id, POMODORO_DURATION_LONG))

    pomodoro_timers[user_id] = {"task": task, "end_time": end_time}

    await ctx.send(
        "🍅 Pomodoro started! I'll notify you in 50 minutes. Use `!pomodoro status` to check progress."

    )


async def pomodoro_timer(ctx, user_id, duration=POMODORO_DURATION): # default value is 25 minutes. Can override
    try:
        if duration == POMODORO_DURATION_LONG:
            await asyncio.sleep(POMODORO_DURATION_LONG) # long
            await ctx.send(
                f"⏰ Time's up, {ctx.author.mention}! You did great! 👏 Break time! ☕"
            )
            pomodoro_timers.pop(user_id, None)
            await break_pomodoro(ctx, True)

        else: # default
            await asyncio.sleep(duration)
            await ctx.send(
                f"⏰ Time's up, {ctx.author.mention}! You did great! 👏 Break time! ☕"
            )
            pomodoro_timers.pop(user_id, None)
            await break_pomodoro(ctx)


    except asyncio.CancelledError:
        if not ctx.bot.is_closed():
            await ctx.send("Pomodoro has either been canceled or paused! ✅ ")
            pomodoro_timers.pop(user_id, None)
        raise # allows proper clean-up
        



async def cancel_pomodoro(ctx):
    user_id = ctx.author.id

    if user_id in pomodoro_timers:
        task = pomodoro_timers[user_id]["task"]
        task.cancel()
        pomodoro_timers.pop(user_id, None)

    else:
        await ctx.send(f"{ctx.author.mention}, you don't have a Pomodoro running!")


# gets called automatically when the pomodoro timer is done
# depending on pomodoro length, creates the proper timer
# non-manual
async def break_pomodoro(ctx, extend=False):
    if extend:
        await asyncio.sleep(BREAK_DURATION_LONG)
        await ctx.send("Your break is set for 10 minutes! I'll notify you when it's over.")
        await ctx.send(
            f"⏰ Time's up, {ctx.author.mention}! You did great! 👏 Back to work! Starting again? Use `!pomodoro start`"
        )
        
    else:
        await asyncio.sleep(BREAK_DURATION)
        await ctx.send("Your break is set for 5 minutes! I'll notify you when it's over.")
        await ctx.send(
            f"⏰ Time's up, {ctx.author.mention}! You did great! 👏 Back to work! Starting again? Use `!pomodoro start`"
        )


# manual break
async def custom_break(ctx, duration: int = 5):
    user_id = ctx.author.id
    if user_id not in pomodoro_timers:
        await ctx.send("Start a pomodoro first with `!pomodoro`.")
        return
    
    task_info = pomodoro_timers.pop(user_id)
    task_info["task"].cancel()
    remaining = (task_info["end_time"] - datetime.now()).total_seconds()    # timedelta object, so we can use .total_seconds()
    await ctx.send(f"⏸️ Paused your Pomodoro. Taking a {duration}-minute break!")

    await asyncio.sleep(duration * 60)
    await ctx.send(f"⏰ Break over, {ctx.author.mention}! Resuming Pomodoro!")

    # Resume with remaining time
    end_time = datetime.now() + timedelta(seconds=remaining)
    new_task = asyncio.create_task(pomodoro_timer(ctx, user_id, remaining))
    pomodoro_timers[user_id] = {"task": new_task, "end_time": end_time}
    await ctx.send(f"Current time remaining: {(pomodoro_timers[user_id]['end_time'] - datetime.now()).total_seconds() / 60:.2f} minutes")


def get_status(user_id):
    if user_id in pomodoro_timers:
        end_time = pomodoro_timers[user_id]["end_time"]
        remaining = (end_time - datetime.now()).total_seconds()
        return max(0, int(remaining))
    return None

