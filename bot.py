# bot.py

import os
import discord
import random
import espn
from espn import Team
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

home_team = []
away_team = []
@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break

	print(f'{client.user} is connected to the following guild:\n'
		  f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	chant = [
		'Go preds.',
		'Rinne putting on a clinc'
	]

	if message.content == 'preds':
		response = random.choice(chant)
		home_team,away_team = espn.start("20191027")
		i = 0
		while(i < len(home_team)):
			await message.channel.send("--------------------------------------")
			await message.channel.send(("{} @ {}".center(70, ' ')).format(away_team[i].getName(), home_team[i].getName()))
			await message.channel.send(("{} - {}".center(99, ' ')).format(away_team[i].getScore(), home_team[i].getScore()))
			await message.channel.send(("{} - {}\n".center(45, ' ')).format(away_team[i].getStartingGoalie(), home_team[i].getStartingGoalie()))
			await message.channel.send("--------------------------------------")
			i = i + 1
client.run(TOKEN)