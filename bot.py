import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hello', help='Replies with Hello <3')
async def hello(ctx):
    response = 'Hello daddy <3'
    await ctx.send(response)


@bot.command(name='dice_roll', help='Rolls a dice')
async def dice_roll(ctx):
    dice = random.randint(1, 6)
    await ctx.send(dice)

bot.run(TOKEN)
