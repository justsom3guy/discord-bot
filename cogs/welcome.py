import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_name = "welcome"

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        await channel.send(f'{member.name} joined')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        await channel.send(f'{member.name} left.')


def setup(bot):
    bot.add_cog(Welcome(bot))
