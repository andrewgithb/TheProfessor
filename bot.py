# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if 'the professor' in message.content.lower():
            response = 'Fuck you, don\'t speak bad on my name!'
            await message.author.create_dm()
            await message.author.dm_channel.send(response)

client.run(TOKEN)
