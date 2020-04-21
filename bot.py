import discord
from login import token
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is alive')


@client.command()
async def ping(ctx):
    await ctx.send(f'PONG! Ping to server is: {round(client.latency *1000 )}ms')


# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined the server.')
#
# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left the server.')

client.run(token)
