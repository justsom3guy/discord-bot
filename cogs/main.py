import discord
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')

    @commands.command(help='Delete msgs with specified limit', aliases=['clear', 'purge'])
    @commands.has_role("MOD")
    async def delete(self, message, number=1):
        await message.channel.purge(limit=int(number)+1)

    @delete.error
    async def delete_error(self, message, error):
        if isinstance(error, commands.BadArgument):
            await message.channel.send('Please Enter an Integer')
        if isinstance(error, commands.errors.MissingRole):
            response = 'You don\'t have enough privileges'
            await message.channel.send(response)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            response = 'Are you sure you entered the right spelling?\nTry ***!help*** to find the right command <3'
            await ctx.channel.send(response)


def setup(bot):
    bot.add_cog(Main(bot))
