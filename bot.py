import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands

from mongoengine import connect

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MONGO_HOST = os.getenv('MONGO_HOST')
prefix = os.getenv('Prefix')

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

connect(host=MONGO_HOST)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(TOKEN)
