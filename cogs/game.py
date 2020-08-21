import discord
from discord.ext import commands
from database.user import User
from mongoengine import DoesNotExist


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 744760039121616896

    @commands.command(help='Registers User')
    async def register(self, ctx):
        if ctx.channel.id == self.channel_id:
            try:
                user = User.objects(name=str(ctx.author)).get()
                response = f'{user.name} of level {user.level} exists!!'
                await ctx.channel.send(response)
            except DoesNotExist:
                user = User(name=str(ctx.author), level=1)
                user.save()
                response = f'{user.name} created with level {user.level}. Have fun!!'
                await ctx.channel.send(response)

    @commands.command(help='Level up')
    async def levelup(self, ctx):
        if ctx.channel.id == self.channel_id:
            try:
                user = User.objects(name=str(ctx.author)).get()
                user.update(
                    level=int(user.level) + 1
                )
                user.save()
                user = User.objects(name=str(ctx.author)).get()
                response = f'{user.name} is now of level {user.level}!!'
                await ctx.channel.send(response)
            except DoesNotExist:
                response = f'{ctx.author} not register please register'
                await ctx.channel.send(response)

    @commands.command(help='Shows stats')
    async def stats(self, ctx):
        if ctx.channel.id == self.channel_id:
            try:
                user = User.objects(name=str(ctx.author)).get()
                response = f'{user.name} is now of level {user.level}!!'
                await ctx.channel.send(response)
            except DoesNotExist:
                response = f'{ctx.author} not register please register'
                await ctx.channel.send(response)


def setup(bot):
    bot.add_cog(Game(bot))
