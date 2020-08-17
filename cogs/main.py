import discord
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')


def setup(bot):
    bot.add_cog(Main(bot))
