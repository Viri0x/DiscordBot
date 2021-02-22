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

@bot.event
async def on_ready():
    logging.info("Allons-y !")
    logging.info("I'm running on " + bot.user.name)
    logging.info("with the ID" + str(bot.user.id))
    
@bot.command(pass_context=True)
async def Help(ctx):
    embed = discord.Embed(title="Bot's Help", description = "Everything you need to know", color = 0x00ff00)
    embed.add_field(name=">info \"user\"", value = "Give user's info", inline=False)
    embed.add_field(name=">kick \"user\"", value ="Kick the hell out of someone", inline=False)
    embed.add_field(name=">someone \"user\"", value ="Tag a connected person of the server, BOT not included.", inline=False)
    embed.add_field(name=">cheatox", value = "no one will notice", inline = False)
    embed.add_field(name=">poll \"choice1\" \"emoji1\" \"choice2\" \"emoji2\" ... ",value = "Make a poll", inline = False)
    embed.add_field(name=">settle \"list of user\"", value = "Randomly choose one of the user", inline = False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello wonderful perso")
    logging.info("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description = "Here's what I could find.", color = 0x00ff00)
    embed.add_field(name="Name", value = user.name, inline=True)
    embed.add_field(name="ID", value = user.id, inline=True)
    embed.add_field(name="Status", value = user.status, inline=True)
    embed.add_field(name="Highest role", value = user.top_role)
    embed.add_field(name="Joined", value = user.joined_at)
    embed.set_thumbnail(url= user.avatar_url)
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def kick(ctx, user : discord.Member):
    await ctx.send(":boot: PAF," + ctx.message.author.name + " just kicked {} !".format(user.name))
    await ctx.message.delete()

@bot.command(pass_context=True)
async def settle(ctx, *args: discord.Member):
    win = random.randint(0,len(args) - 1)
    logging.info("random was " + str(win) + " -> " + args[win].name)

    embed = discord.Embed(color=discord.Colour.orange())
    embed.add_field(name = "The RNG has spoken...".format(args[win].mention), value = args[win].mention + "takes it all !", inline = False)
    await ctx.send(embed = embed)

def filterOnlyOnline(member):
    return member.status != discord.Status.offline and not member.bot

@bot.command()
async def someone(ctx):
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

    embed = discord.Embed()
    embed.add_field(name = "You have been randomly pinged by {}, have a good day !".format(ctx.message.author.name), value = memb[Loto].mention, inline = False)
    embed.set_image(url='https://media.giphy.com/media/wrBURfbZmqqXu/giphy.gif')
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def cheatox(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://media.giphy.com/media/3ohhwf3mprga8qAIOQ/giphy.gif")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def clean(ctx, mx: int): 
    if (ctx.message.author.id == 155823093544255489):
        await ctx.channel.purge(check=None, limit=mx + 1)
    else:
        await ctx.send("You don't have permission to do that !")

@bot.command(pass_context=True)
async def free_rolls(ctx, mx, rolls: int):

    def check(m):
        return True

    for i in range(rolls):
        await ctx.send("$" + mx)
        await bot.wait_for("message", check=check)
    logging.info("Mudae was summoned")

@bot.command(pass_context=True)
async def poll(ctx, *args):
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

#secure the token in a specific file
f = open("token.txt", "r")
bot.run(f.read())