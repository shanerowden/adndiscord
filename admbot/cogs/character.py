from discord.ext import commands
from admbot import bot
import os
from textwrap import dedent as wrap
from adndiscord.attributes import AbilityScoreGen

class Character(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            if guild.name == os.environ['DISCORD_GUILD']:
                print(
                    f'{self.bot.user} is connected to the following guild:\n'
                    f'{guild.name}(id: {guild.id})'
                )

        testing_channel = self.bot.get_channel(730254366740709397)
        await testing_channel.send(wrap(
            """
            Discord Bot is Online and Ready. 
            Be aware that bot commands are only available when I am running the server. 
            They will not work when it is off.
            """
        ))

    @commands.command()
    async def roll(self, ctx):
        """
        Roll ability scores with no arguments
        """
        for guild in bot.guilds:
            if guild.name == os.environ['DISCORD_GUILD']:
                break

        if ctx.author == self.bot.user:
            return

        ability_scores = AbilityScoreGen()
        print(ability_scores)
        await ctx.send(str(ability_scores))


def setup(bot):
    bot.add_cog(Character(bot))


