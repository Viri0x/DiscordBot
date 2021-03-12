import discord
import logging
from discord.ext import commands
import random


# Log SetUp
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode="w")

def filterOnlyOnline(member):
    return member.status != discord.Status.offline and not member.bot

class Features(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def kick(self, ctx, user : discord.Member):
        await ctx.send(":boot: PAF," + ctx.message.author.name + " just kicked {} !".format(user.name))
        await ctx.message.delete()


    @commands.command()
    async def someone(self, ctx):
        memb = list(filter(filterOnlyOnline, ctx.guild.members))
        length = len(memb) - 1

        if length <= 0 :
            await ctx.send("No one to ping :c !")
            return
        else:
            await ctx.message.delete()

        Loto = random.randint(0,length)
        while memb[Loto].id == ctx.message.author.id:
            Loto = random.randint(0,length)

        #DEBUG
        logging.info(ctx.message.author.name + " pinged " + memb[Loto].name)

        embed = discord.Embed(color=discord.Colour.green())
        embed.add_field(name = "You have been randomly pinged by {}, have a good day !".format(ctx.message.author.name), value = memb[Loto].mention,  inline = False)
        embed.set_image(url='https://media.giphy.com/media/wrBURfbZmqqXu/giphy.gif')
        await ctx.send(embed = embed)

    @commands.command()
    async def cheatox(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://media.giphy.com/media/3ohhwf3mprga8qAIOQ/giphy.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def poll(self, ctx, *args):
                #should be a "choice 1, emoji 1, choice 2, emoji 2" 

                if (len(args)%2) != 0 : 
                    await ctx.send("You must have made a mistake, pattern is: \">pool_choice1_emoji1_choice2\_emoji2 ... \" with \_ as space")
                    await bot.delete_message(ctx.message)
                else:
                    poll = ""
                    count = 0
                    k = 1
                    for i in range(0, len(args)):

                        if (i == len(args)-1) :
                            poll += args[i]
                        else:
                            if count == 0 : #is a choice
                                poll += (args[i] + " ")
                                count = 1
                            else:
                                poll += (args[i] + "  ou  ")
                                count = 0

                    embed = discord.Embed()
                    embed.add_field(name = poll, value = "asks " + ctx.message.author.name, inline = False)
                    message = await ctx.send(embed = embed)
                    
                    while k < len(args):
                        await message.add_reaction(args[k])
                        k+=2

                    await ctx.message.delete()

def setup(bot):
    bot.add_cog(Features(bot))