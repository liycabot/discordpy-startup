from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")
    
@bot.command()
async def naa(ctx):
    await ctx.send("?")
    
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)
    

bot.run(token)
