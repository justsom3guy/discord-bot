import discord
from discord.ext import commands


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 744760039121616896
        self.db = sqlite


def setup(bot):
    bot.add_cog(Game(bot))
