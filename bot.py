import discord
from login import token
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is alive')


client.run(token)
