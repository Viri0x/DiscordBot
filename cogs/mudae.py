import discord
import random
import logging
from discord.ext import commands

# Log SetUp
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode="w")

class MudaeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def settle(self, ctx, *args: discord.Member):
        win = random.randint(0,len(args) - 1)
        logging.info("random was " + str(win) + " -> " + args[win].name)

        embed = discord.Embed(color=discord.Colour.orange())
        embed.add_field(name = "The RNG has spoken...".format(args[win].mention), value = args[win].mention + "takes it all !", inline = False)
        await ctx.send(embed = embed)

    
    @commands.command()
    async def free_rolls(self, ctx, mx, rolls: int):

        def check(m):
            return True

        for i in range(rolls):
            await ctx.send("$" + mx)
            await bot.wait_for("message", check=check)
        logging.info("Mudae was summoned")

def setup(bot):
    bot.add_cog(MudaeCog(bot))