import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_name = "general"

    @commands.command(help='Replies with pong')
    async def ping(self, ctx):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        if ctx.channel.name == channel.name:
            await channel.send('pong')

    @commands.command(help='Says hello back')
    async def hello(self, ctx):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        response = f'Hello {str(ctx.author)[:-5]} <3'
        await channel.send(response)


def setup(bot):
    bot.add_cog(General(bot))
