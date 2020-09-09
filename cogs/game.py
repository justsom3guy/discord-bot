import discord
from discord.ext import commands
from database.user import User
from database.monster import Monster
from mongoengine import DoesNotExist
import random


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_name = "rpg"

    @commands.command(help='Registers User', aliases=['create'])
    async def register(self, ctx):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        if ctx.channel.name == channel.name:
            try:
                user = User.objects(name=str(ctx.author)).get()
                response = f'{user.name[:-5]} of level {user.level} exists!!'
                await channel.send(response)
            except DoesNotExist:
                user = User(name=str(ctx.author))
                user.save()
                response = f'Player {user.name[:-5]} created. Have fun!!'
                await channel.send(response)

    @commands.command(help='Shows stats')
    async def stats(self, ctx):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        if ctx.channel.name == channel.name:
            try:
                user = User.objects(name=str(ctx.author)).get()
                response = (f'{user.name[:-5]}\'s stats-\n'
                            f'Level : {user.level}\n'
                            f'Xp : {user.xp}\n'
                            f'Health : {user.health}\n'
                            f'Current Floor : {user.floorLevel}\n'
                            f'Max Floor : {user.floorReached}\n'
                            f'Currently in fight : {user.inFight}\n'
                            )

                await channel.send(response)
            except DoesNotExist:
                response = f'{ctx.author} not register please register'
                await channel.send(response)

    @commands.command(help="Find Monster", aliases=['find'])
    async def findMonster(self, ctx):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        chance = bool(random.getrandbits(1))
        if chance:
            if ctx.channel.name == channel.name:
                monster = random.choice(Monster.objects)
                response = f'You found {monster.name}'
                await channel.send(response)
        else:
            response = 'No monster was found try again later'
            await channel.send(response)

    @commands.command(help="Create Monster", aliases=['createM'])
    @commands.has_role("MOD")
    async def createMonster(self, ctx, name):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        if ctx.channel.name == channel.name:
            try:
                monster = Monster.objects(name=name).get()
                response = f'Monster {monster.name} exists'
                await channel.send(response)
            except DoesNotExist:
                monster = Monster(name=name)
                monster.save()
                response = f'New monster {monster.name} is born in this world'
                await channel.send(response)

    @createMonster.error
    async def createMonster_handler(self, ctx, error):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        if ctx.channel.name == channel.name:
            if isinstance(error, commands.errors.MissingRole):
                response = 'You dont have enough privlages'
                await channel.send(response)

            if isinstance(error, commands.MissingRequiredArgument):
                response = 'You didn\'t provide a name for the monster'
                await channel.send(response)

    @commands.command(help="Delete player data", aliases=['leave'])
    async def unregister(self, ctx):
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name=self.channel_name)
        if ctx.channel.name == channel.name:
            try:
                user = User.objects(name=str(ctx.author)).delete()
                response = f'Player delete :/'
                await channel.send(response)
            except DoesNotExist:
                response = f'Player named {ctx.author} does not exist in database.'
                await channel.send(response)


def setup(bot):
    bot.add_cog(Game(bot))
