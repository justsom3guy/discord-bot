import discord
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')

    @commands.command(help='Delete msgs with sepecific limit')
    async def delete(self, message, number=1):
        await message.channel.purge(limit=int(number)+1)


def setup(bot):
    bot.add_cog(Main(bot))
