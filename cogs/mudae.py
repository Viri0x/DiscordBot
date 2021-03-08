import discord
import random
import logging
from time import sleep
from discord.ext import commands

# Log SetUp
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode="w")

class Mudae(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def settle(self, ctx, *args: discord.Member):
        win = random.randint(0,len(args) - 1)
        logging.info("random was " + str(win) + " -> " + args[win].name)

        embed = discord.Embed(color=discord.Colour.orange())
        #embed.add_field(name = "The RNG has spoken...".format(args[win].mention), value = args[win].mention + "takes it all !", inline = False)
        msg = await ctx.send(embed = embed)

        for i in [":three:", ":two:", ":one:"]:
            embed = discord.Embed(color=discord.Colour.orange())
            embed.add_field(name = "The RNG will spoke in...".format(args[win].mention), value = i, inline = False)
            await msg.edit(embed = embed)
            sleep(1)


        embed = discord.Embed(color=discord.Colour.orange())
        embed.add_field(name = "The RNG has spoken...".format(args[win].mention), value = ":tada: **" + args[win].mention + "** takes it all ! :tada:", inline = False)
        await msg.edit(embed = embed)


def setup(bot):
    bot.add_cog(Mudae(bot))