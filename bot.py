from main import init
from adndiscord.attributes import AbilityScoreGen
from textwrap import dedent as wrap

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

    testing_channel = client.get_channel(730254366740709397)
    await testing_channel.send(wrap(
        """
        Discord Bot is Online and Ready. 
        Be aware that bot commands are only available when I am running the server. 
        They will not work when it is off.
        """
    ))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message == "roll":
        ability_scores = AbilityScoreGen()
        print(ability_scores)
        await message.channel.send(str(ability_scores))



client.run(TOKEN)