import os
from discord.ext import commands
from adndiscord.pathconf import PATHS, ADMBOT


token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
extentions = [c.stem for c in PATHS['COGS_DIR'].glob("./*.py") if "__init__" not in c.stem]
for ext in extentions:
    bot.load_extension(f"{ADMBOT}.cogs.{ext}")
bot.run(token)
