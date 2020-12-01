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
	healthroles = [discord.utils.get(message.guild.roles, id = 714535509279637525), discord.utils.get(message.guild.roles, id = 714535481928319016), discord.utils.get(message.guild.roles, id = 714535460860330066), discord.utils.get(message.guild.roles, id = 714535436143558788), discord.utils.get(message.guild.roles, id = 714535405843775518), discord.utils.get(message.guild.roles, id = 714535379675644054), discord.utils.get(message.guild.roles, id = 714535348046266449), discord.utils.get(message.guild.roles, id = 714535324759621712), discord.utils.get(message.guild.roles, id = 714535298729640047), discord.utils.get(message.guild.roles, id = 714535185273847871), discord.utils.get(message.guild.roles, id = 714534974916919349)]
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

	if hamon in message.author.roles or standAndHamon in message.author.roles:
		if (argslist[0] == "hamon" or argslist[0] == "h"):
			if (argslist[1] == "overdrive" or argslist[1] == "o"):
				if message.mentions == []:
					await message.channel.send("you need to ping a user to attack")
					return
				if rof_armour in message.mentions[0].roles:
					attacker = message.mentions[0]
					attacked = message.author
				else:
					attacker = message.author
					attacked = message.mentions[0]
				dmg = 1
				await health.hamonattack(attacker, attacked, dmg, healthroles, message)
			if (argslist[1] == "heal" or argslist[1] == "h"):
				healed = message.author
				points = random.randrange(0, 2)
				await health.heal(healed, points, healthroles)

	if standuser in message.author.roles or standAndHamon in message.author.roles:
		if (argslist[0] == "stand" or argslist[0] == "s"):
			if (argslist[1] == "attack" or argslist[1] == "a"):
				if message.mentions == []:
					await message.channel.send("you need to ping a user to attack")
					return
				if rof_armour in message.mentions[0].roles:
					attacker = message.mentions[0]
					attacked = message.author
				else:
					attacker = message.author
					attacked = message.mentions[0]
				dmg = 1
				await health.standattack(attacker, attacked, dmg, healthroles, message)

client.run(token)