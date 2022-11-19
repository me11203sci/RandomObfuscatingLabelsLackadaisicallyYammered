# Imports.
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
	"""Downloads, Converts, Deletes, Renames, and Relocates P.D.F. files"""
	# Create temporary directory to store downloads.
	os.system("mkdir temporary")
	print("!do COMMAND: Created directory \"temporary\"")
	
	# Iterate through all messages in channel.
	file_name = 0
	directory = "temporary/"
	async for message in context.channel.history():
		for attachment in message.attachments:
			if(attachment.content_type == "application/pdf"):
				path = directory + str(file_name)
				await attachment.save(f"{path}.pdf")
				print(f"!do COMMAND: Downloaded file {file_name}.pdf")
				os.system(f"pdfimages -j -p {path}.pdf {path}")
				print(f"!do COMMAND: Converted {file_name}.pdf")
				os.system(f"rm {path}.pdf")
				print(f"!do COMMAND: Deleted {file_name}.pdf")
				for file in os.listdir(directory):
					os.system(f"sh hashVisuals.sh {directory}{file}")
				file_name += 1
		await message.delete()
	
	# Wrap-up.
	os.system("rm -rf temporary/")
	print("!do COMMAND: Deleted directory \"temporary\"")
	print("All done. *burps*")

# Retriveing and utilizing access token.
env_path = os.path.join(os.getcwd(),".env")
load_dotenv(env_path)
token = os.getenv("BOT_TOKEN")
rolly.run(token)
