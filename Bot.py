#First Bot
import discord
import random
import logging
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

# Log SetUp
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode="w")

# Bot SetUp
client = discord.Client()
intents = discord.Intents().all()
bot = commands.Bot(command_prefix= '>', intents=intents)

extensions = ['cogs.basics', 'cogs.mudae', 'cogs.admin', 'cogs.features']

if __name__ == '__main__':
    for e in extensions:
        bot.load_extension(e)

@bot.event
async def on_ready():
    logging.info("Allons-y !")
    logging.info("I'm running on " + bot.user.name)
    logging.info("with the ID" + str(bot.user.id))
        
#secure the token in a specific file
f = open("token.txt", "r")
bot.run(f.read())