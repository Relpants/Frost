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

	if "!scores" in message.content:
		message_split = message.content.split(" ")
		home_team,away_team = espn.start(message_split[1])
		i = 0
		while(i < len(home_team)):
			await message.channel.send(away_team[i].getLogo())
			await message.channel.send("```\n    {}\n          {}\n{}\n\n          @ \n\n    {}\n          {}\n{}\n```".center(70, ' ').format(
				away_team[i].getName(), 
				away_team[i].getScore(), 
				away_team[i].getStartingGoalie(), 
				home_team[i].getName(), 
				home_team[i].getScore(), 
				home_team[i].getStartingGoalie()))
			await message.channel.send(home_team[i].getLogo())
			await message.channel.send("```--------------------------------------\n----------------------------------------------------------------------------\n----------------------------------------------------------------------------\n----------------------------------------------------------------------------\n----------------------------------------------------------------------------\n```")
			i = i + 1
client.run(TOKEN)
