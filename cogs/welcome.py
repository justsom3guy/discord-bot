import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 744782496180469800

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_cl = self.bot.get_channel(self.channel_id)
        await welcome_cl.send(f'{member.name} joined')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        welcome_cl = self.bot.get_channel(self.channel_id)
        await welcome_cl.send(f'{member.name} left.')


def setup(bot):
    bot.add_cog(Welcome(bot))
