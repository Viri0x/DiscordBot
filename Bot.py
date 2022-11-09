#First Bot
import discord
import random
import logging
from discord.ext import commands
import asyncio

# Log SetUp
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode="w")

# Bot SetUp
intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix= '>', intents=intents)

extensions = ['cogs.basics', 'cogs.mudae', 'cogs.admin', 'cogs.features', 'cogs.dalle']


async def main():
    f = open("token.txt", "r")
    async with bot:
        for e in extensions:
            await bot.load_extension(e)
        await bot.start(f.read())


if __name__ == '__main__':
    asyncio.run(main())

@bot.event
async def on_ready():
    logging.info("Allons-y !")
    logging.info("I'm running on " + bot.user.name)
    logging.info("with the ID" + str(bot.user.id))
        
#secure the token in a specific file
