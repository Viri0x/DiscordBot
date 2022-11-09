import discord
import logging
from discord.ext import commands

# Log SetUp
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode="w")

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def Help(self, ctx):
        embed = discord.Embed(title="Bot'sy Help", description = "Everything you need to know", color = 0x00ff00)
        embed.add_field(name=">info <user>", value = "Give user's info", inline=False)
        embed.add_field(name=">kick <user>", value ="Kick the hell out of someone", inline=False)
        embed.add_field(name=">someone <user>", value ="Tag a connected person of the server, BOT not included.", inline=False)
        embed.add_field(name=">cheatox", value = "no one will notice", inline = False)
        embed.add_field(name=">poll <choice1> <emoji1> <choice2> <emoji2> ... ",value = "Make a poll", inline = False)
        embed.add_field(name=">settle <list of user>", value = "Randomly choose one of the user", inline = False)
        embed.add_field(name=">dalle \"<prompt>\" [Optional]<number_pics>", value = "Create a DALL-E generated image from your prompt", inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello wonderful perso")

    @commands.command()
    async def info(self, ctx, user: discord.Member):
        embed = discord.Embed(title="{}'s info".format(user.name), description = "Here's what I could find.", color = 0x00ff00)
        embed.add_field(name="Name", value = user.name, inline=True)
        embed.add_field(name="ID", value = user.id, inline=True)
        embed.add_field(name="Status", value = user.status, inline=True)
        embed.add_field(name="Highest role", value = user.top_role)
        embed.add_field(name="Joined", value = user.joined_at)
        embed.set_thumbnail(url= user.avatar.url)
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Basics(bot))