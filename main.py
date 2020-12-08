#!/usr/bin/env python3

from discord.ext.commands import Bot
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown
import random
import datetime
import asyncio
import discord
from discord import Member, Embed

import health

intents = discord.Intents.all()

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

client = discord.Client(intents=intents)

async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		file = await i.to_file()
		filelist.insert(len(filelist),file)
	return filelist

prefix = "!"

@client.event
async def on_ready():
	print("hello world!")

@client.event
async def on_message(message):

	helpmessage = discord.Embed(title="Help", description="**help stands** - get help on stands\n**help hamon** - get help on hamon\n**help combat** - get help on combat\n**help commands** - get help on commands like !sleep")
	helpmessage.set_footer(text=f"requested by {message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{message.author.id}/{message.author.avatar}.png")

	standhelpmessage = discord.Embed(title="Help stands", description="**stand attack** - ping a user to attack them with your stand")
	standhelpmessage.set_footer(text=f"requested by {message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{message.author.id}/{message.author.avatar}.png")

	hamonhelpmessage = discord.Embed(title="Help hamon", description="**hamon overdrive** - ping a user to attack them with hamon\n**hamon heal** - concentrate your energies within your body and heal and random 0 to 2 points of damage")
	hamonhelpmessage.set_footer(text=f"requested by {message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{message.author.id}/{message.author.avatar}.png")

	combathelp = discord.Embed(title="Combat", description="- every user has 10 points of health\n- basic stand attacks deal 1 point of damage\n- hamon attacks deal 1 damage to normal players and 3 to vampires (not added yet)\n")
	combathelp.set_footer(text=f"requested by {message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{message.author.id}/{message.author.avatar}.png")

	commandshelp = discord.Embed(title="Basic Commands", description="**sleep** - take a nap, do command again in the dreamland channel to wake up")
	commandshelp.set_footer(text=f"requested by {message.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{message.author.id}/{message.author.avatar}.png")


	healthroles = [discord.utils.get(message.guild.roles, id = 714534974916919349), discord.utils.get(message.guild.roles, id = 714535185273847871), discord.utils.get(message.guild.roles, id = 714535298729640047), discord.utils.get(message.guild.roles, id = 785552558738898965), discord.utils.get(message.guild.roles, id = 714535509279637525)]
	sleeping = discord.utils.get(message.guild.roles, id = 741552665892356147)
	hamon = discord.utils.get(message.guild.roles, id = 713208239764013097)
	standuser = discord.utils.get(message.guild.roles, id = 712718459431157888)
	standAndHamon = discord.utils.get(message.guild.roles, id = 713253110771875860)
	stand = discord.utils.get(message.guild.roles, id = 712718404901142528)
	dead_visitor = discord.utils.get(message.guild.roles, id = 747460046333673573)
	rof_armour = discord.utils.get(message.guild.roles, id = 747465352841134190)
	pantarmour = discord.utils.get(message.guild.roles, id = 751637329088610365)
	scared = discord.utils.get(message.guild.roles, id = 749429015621664790)
	standattackcooldown = discord.utils.get(message.guild.roles, id = 749764783498199080)
	hamonattackcooldown = discord.utils.get(message.guild.roles, id = 749767003379728466)
	hamonhealcooldown = discord.utils.get(message.guild.roles, id = 749768438418898975)
	enraged = discord.utils.get(message.guild.roles, id = 749824364618186844)
	enraged_victim = discord.utils.get(message.guild.roles, id = 749824617648226326)
	curse = discord.utils.get(message.guild.roles, id = 750130819099656284)

	args = message.content.lower().replace(prefix, "")
	argslist = args.split(" ")

	if (message.channel.id == 712716066618605591):#general
		if message.content.startswith('?echo'):
			return
		if message.content.startswith('?echo-edit'):
			return
		if message.content.startswith('sandman echo'):
			return
		text = message.content
		channel = client.get_channel(737149672728297552)
		images = await attachments_to_files(message.attachments,True)
		await channel.send(content="**{0}**\n{1}".format(message.author.mention,text),files=images)
	elif (message.channel.id == 754364505156223007):#memes
		if message.content.startswith('?echo'):
			return
		if message.content.startswith('?echo-edit'):
			return
		if message.content.startswith('sandman echo'):
			return
		text = message.content
		channel = client.get_channel(754376242777686047)
		images = await attachments_to_files(message.attachments,True)
		await channel.send(content="**{0}**\n{1}".format(message.author.mention,text),files=images)
	elif (message.channel.id == 754364579177300068):#battlezone
		if message.content.startswith('?echo'):
			return
		if message.content.startswith('?echo-edit'):
			return
		if message.content.startswith('sandman echo'):
			return
		text = message.content
		channel = client.get_channel(754376278286663762)
		images = await attachments_to_files(message.attachments,True)
		await channel.send(content="**{0}**\n{1}".format(message.author.mention,text),files=images)
	elif (message.channel.id == 730272782285537350): #stand-ideas
		if message.content.startswith('?echo'):
			return
		if message.content.startswith('?echo-edit'):
			return
		if message.content.startswith('sandman echo'):
			return
		text = message.content
		channel = client.get_channel(762741049525141514)
		images = await attachments_to_files(message.attachments,True)
		await channel.send(content="**{0}**\n{1}".format(message.author.mention,text),files=images)
	elif (message.channel.id == 750761929810903103): #nsfw
		if message.content.startswith('?echo'):
			return
		if message.content.startswith('?echo-edit'):
			return
		if message.content.startswith('sandman echo'):
			return
		text = message.content
		channel = client.get_channel(762741097411248149)
		images = await attachments_to_files(message.attachments,True)
		await channel.send(content="**{0}**\n{1}".format(message.author.mention,text),files=images)

	if message.author == client.user or message.channel.id == 747472960016875570:
		return

	if message.content.startswith(prefix):
		if (argslist[0] == "sleep" or argslist[0] == "sl"):
			if not sleeping in message.author.roles:
				await message.channel.send("you begin to fall asleep")
				await asyncio.sleep(5)
				await message.channel.send("you fall asleep")
				await message.author.add_roles(sleeping, reason="sleeping")
				healed = message.author
				await health.sleepheal(healed, healthroles, sleeping)
			elif sleeping in message.author.roles:
				await message.channel.send("you begin to wake up")
				await asyncio.sleep(5)
				await message.channel.send("you wake up")
				await message.author.remove_roles(sleeping, reason="sleeping")
		elif (argslist[0] == "help"):
			if (len(argslist) < 2):
				await message.channel.send(embed=helpmessage)
			elif (argslist[1] == "stands"):
				await message.channel.send(embed=standhelpmessage)
			elif (argslist[1] == "hamon"):
				await message.channel.send(embed=hamonhelpmessage)
			elif (argslist[1] == "combat"):
				await message.channel.send(embed=combathelp)
			elif (argslist[1] == "commands"):
				await message.channel.send(embed=commandshelp)
			else:
				await message.channel.send(embed=helpmessage)

	if hamon in message.author.roles or standAndHamon in message.author.roles:
		if (argslist[0] == "hamon" or argslist[0] == "h"):
			if (argslist[1] == "overdrive" or argslist[1] == "o"):
				if message.mentions == []:
					await message.channel.send("you need to ping a user to attack")
					return
				attacker = message.author
				attacked = message.mentions[0]
				dmg = random.randrange(2, 10)
				await health.changehealth(user=attacked, add=0, subtract=dmg, healthroles=healthroles)
				await message.channel.send(f"{attacker} attacked {attacked} using hamon and delt {dmg} damage!")
			if (argslist[1] == "heal" or argslist[1] == "h"):
				healed = message.author
				points = random.randrange(2, 10)
				await health.changehealth(user=healed, add=points, subtract=0, healthroles=healthroles)

	if standuser in message.author.roles or standAndHamon in message.author.roles:
		if (argslist[0] == "stand" or argslist[0] == "s"):
			if (argslist[1] == "attack" or argslist[1] == "a"):
				dmg = random.randrange(5, 15)
				if message.mentions == []:
					await message.channel.send("you need to ping a user to attack")
					return
				attacker = message.author
				attacked = message.mentions[0]
				await health.changehealth(user=attacked, add=0, subtract=dmg, healthroles=healthroles)
				await message.channel.send(f"{attacker} attacked {attacked} using their stand and delt {dmg} damage!")


client.run(token)