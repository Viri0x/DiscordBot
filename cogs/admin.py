import discord
from discord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def clean(self, ctx, mx: int): 
        if (ctx.message.author.id == 155823093544255489):
            await ctx.channel.purge(check=None, limit=mx + 1)
        else:
            await ctx.send("You don't have permission to do that !")

def setup(bot):
    bot.add_cog(AdminCog(bot))