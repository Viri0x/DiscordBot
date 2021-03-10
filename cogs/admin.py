import discord
from discord.ext import commands

admin_id = 155823093544255489

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.clean = -1
        self.ctx = None

    @commands.command()
    async def clean(self, ctx, mx: int): 
        if (ctx.message.author.id != admin_id):
            await ctx.send("You don't have permission to do that !")
            return

        embed = discord.Embed(color=discord.Colour.purple(), title="Clean -Warning-")
        embed.add_field(name = "\u200b", value = "Do you really want to clean " + str(mx) + " messages ?", inline = False)

        if (mx > 15):
            self.clean = mx
            msg = await ctx.send(embed = embed)
            await msg.add_reaction("\u2705")
            await msg.add_reaction("\u274c")
        else:
            await ctx.channel.purge(check=None, limit=mx + 1)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        msg = reaction.message

        print(msg.embeds != [])
        print(msg.embeds[0].title)
        print(msg.embeds[0].title == "Clean -Warning-")
        print(self.clean != -1)

        users = await reaction.users().flatten()

        # Clean messages
        if msg.embeds != [] and msg.embeds[0].title == "Clean -Warning-" and self.clean != -1 and len(users) != 1:

            print("HELLO")
            if reaction.emoji == "\u2705":
                print("CACA")
                await msg.channel.purge(check=None, limit=self.clean + 1)
            else:
                print("COCO")
                await msg.channel.purge(check=None, limit=1)
            self.clean = -1


def setup(bot):
    bot.add_cog(Admin(bot))