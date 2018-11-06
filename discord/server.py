import discord
import asyncio
import json
import requests

client = discord.Client()

# Character you want the bot to look for to start commands.
prefix = '!'

# Name of the bot to follow the prefix.
bot_name = 'waifu'

# Channel ID of the channel you want the bot to work in.
botChannel = '261731325055074305'
testBotChannel = '458186960331341824'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.channel.id == botChannel or message.channel.id == testBotChannel:
        if message.content.startswith(prefix) or message.author.bot: return
        if message.content.startswith(prefix + bot_name):

client.run('token')