# Library Imports
import discord # For discord
from discord.ext import commands # For discord
import json # For interacting with json
from pathlib import Path # For paths
import platform # For stats
import logging

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

#Defining requirements
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix='!', case_insensitive=True, owner_id=216456015208644608)
bot.config_token = secret_file['token']


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: !\n-----")
    await bot.change_presence(activity=discord.Game(name=f"Use ! to interact with me!")) # This changes the bots 'activity'

@bot.command()
async def stats(ctx):
    """
    Displays bot stats. Server count, 
    Members using it, and its dependable libraries 
    """
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))
    await ctx.send(f"This bot is running on {serverCount} Discord servers - with a total of {memberCount} members.\nIt's running Python Version: {pythonVersion} and uses Discord.py Version: {dpyVersion}")

@bot.command(aliases=['disconnect', 'leave', 'stop'])
@commands.is_owner()
async def logout(ctx):
    """
    If the user running the command 
    owns the bot then this will disconnect the bot from discord.
    """
    await ctx.send(f"Ok cya :wave:")
    await bot.logout()

@logout.error
async def logout_error(ctx, error):
    """
    Logout command an error handling
    """
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You lack permission to use this command.")
    else:
        raise error

bot.run(bot.config_token) # Runs our bot