from main import init
from adndiscord.attributes import AbilityScoreGen

import os
import discord
from dotenv import load_dotenv

init()

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

    if message == "!roll attributes":
        ability_scores = AbilityScoreGen()
        await message.channel.send(str(ability_scores))



client.run(TOKEN)