import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 743710240423411755

    @commands.command()
    async def pong(self, ctx):
        if ctx.channel.id == self.channel_id:
            await ctx.send('pong')

    @commands.command()
    async def hello(self, ctx):
        if ctx.channel.id == self.channel_id:
            response = 'Hello daddy <3'
            await ctx.channel.send(response)


def setup(bot):
    bot.add_cog(General(bot))
