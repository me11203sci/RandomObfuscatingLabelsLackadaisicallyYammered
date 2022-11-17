# Imports
from dotenv import load_dotenv
from discord.ext import commands
import discord
import os
import platform

# Set intents.
intents = discord.Intents.default()
intents.message_content = True

# Create bot client instance.
rolly = commands.Bot(command_prefix = '!', intents = intents)

@rolly.event
async def on_ready():
    notes_queue = rolly.get_channel(1037976833221726268)
    await notes_queue.send("I am retarded (and ready to help)!")

@rolly.command()
async def poke(context):
    """( ´∀` )σ)`A´ )"""
    await context.send("Um, you stink and leave me alone please!")

@rolly.command()
async def clear(context):
    """Clears channel."""
    async for message in context.channel.history():
        await message.delete()

@rolly.command()
async def do(context):
    """Downloads, Deletes, Converts, Renames, and Relocates files"""
    os.system("mkdir temporary && cp .env temporary/.env && cp hashVisuals.sh temporary/hashVisuals.sh")
    print("!DO: Created directory \"temporary\"")
    i=0
    async for message in context.channel.history():
        if(len(message.attachments) == 0):
            await message.delete()
        for attachment in message.attachments:
            if(attachment.content_type != "application/pdf"):
                await message.delete()
            else:
                await attachment.save(fp = f"temporary/{i}.pdf")
                await message.delete()
                i+=1
    previousDirectory = os.getcwd()
    os.chdir("temporary")
    for file in os.listdir():
        if(file.split(".")[1] == "pdf"):
            print(f"!DO: Converting {file}")
            outputName = file.split(".")[0]
            os.system(f"pdfimages -j -p {file} {outputName} && rm {file}")
    for picture in list(filter(lambda x: x.split(".")[1] == "jpg", os.listdir())):
        os.system(f"sh hashVisuals.sh {picture}")
    os.chdir(previousDirectory)
    os.system("rm -rf temporary")
    print("!DO: Deleted directory \"temporary\"")
    print("All done. *burps*")

envPath = os.path.join(os.getcwd(),".env")
load_dotenv(envPath)
token = os.getenv("BOT_TOKEN")
rolly.run(token)
