import discord
from discord.ext import commands
from discord import Interaction
import wavelink
import os
bot = commands.Bot(command_prefix='!', intents= discord.Intents.all(), case_insensitive = True, help_command=None)
# Events:
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.activity.Game(name="Your Mix!"), status= discord.Status.idle)
    print(f'Logged in as {bot.user.name}')
    for filename in os.listdir("./Interactions"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Interactions.{filename[:-3]}")
        print(f"Loaded interactions")
    for filename in os.listdir("./Events"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Events.{filename[:-3]}")
        print(f"Loaded events")
    for filename in os.listdir("./Prefix"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Prefix.{filename[:-3]}")
        print(f"Loaded prefix")
    synced = await bot.tree.sync()
    print(f'Synced commands: {str(len(synced))}')
#----------------------------------------------------------------
# Commands:
@bot.command()
@commands.is_owner()
async def reload(ctx):
    for filename in os.listdir("./Interactions"):
        if filename.endswith(".py") and not filename.startswith("__"):
            await bot.reload_extension(f"Interactions.{filename[:-3]}")
            await ctx.send(f"Reloaded {filename[:-3]}")
    for filename in os.listdir("./Prefix"):
        if filename.endswith(".py"):
            await bot.reload_extension(f"Prefix.{filename[:-3]}")
            await ctx.send(f"Reloaded {filename[:-3]}")
    for filename in os.listdir("./Events"):
        if filename.endswith(".py"):
            await bot.reload_extension(f"Events.{filename[:-3]}")
        await ctx.send(f"Reloaded {filename[:-3]}")
@bot.hybrid_command()
@commands.is_owner()
async def node(ctx, uri: str, password: str):
    node = wavelink.Node(uri=uri, password=password,retries=1)
    try:
        await wavelink.Pool.connect(client=bot, nodes=[node])
        await ctx.send(f"Connected to Node successfully!")
    except Exception as e:
        await ctx.send(f"Failed to connect to Node: {e}")
#-----------------------------------------------------------------
bot.run("")
 
