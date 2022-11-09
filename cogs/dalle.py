import discord
import logging
from discord.ext import commands
import openai

# Log SetUp
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode="w")

# Retrieve openai_key
openai_file = open("openai_key.txt", "r")
OPENAI_KEY = openai_file.read()
logging.info(f"OPENAI_KEY = {OPENAI_KEY}")
openai.api_key = OPENAI_KEY

def send_dalle_request(prompt, size = "256x256", nb_pics = 1):
    """
    Use openai Dalle API to request pictures

    ---- parameters
    prompt : str
    size: int - default is (1024x1024) but can be (256x256 or 512x512)
    nb_pics: int - between 1 and 10. Default is 1
    """
    response = openai.Image.create(
        prompt=prompt,
        n=nb_pics,
        size=size
    )
    return response


class Dalle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def dalle(self, ctx, *args):
        """Send a request to DALLE API and display result"""
        # Health check of args
        args_length = len(args)

        nb_pics = 1

        # First args must be prompt, second can be nb_pics wanted.
        if args_length < 1:
            await ctx.send("You must enter a prompt as input !")
            return
        if args_length == 2:
            nb_pics = int(args[1])

        # Send request to Dalle and get image
        prompt = args[0]
        response = send_dalle_request(prompt, nb_pics=nb_pics)

        logging.info(response)
        image_url = response['data'][0]['url']


        # Create Embedded message to display
        embed = discord.Embed(color=discord.Colour.blue())
        embed.add_field(name = f"Your Dall-e creation for the prompt :", value = prompt, inline = False)
        embed.set_image(url=image_url)

        # Display final message
        await ctx.send(embed = embed)


async def setup(bot):
    await bot.add_cog(Dalle(bot))