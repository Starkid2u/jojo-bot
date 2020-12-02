import discord
import asyncio
import random
from discord.ext import commands

async def kill(killed, healthroles):
	await killed.remove_roles(healthroles[1], reason="killed")
	await killed.add_roles(healthroles[0], reason="killed")
	await asyncio.sleep(3600)
	await killed.remove_roles(healthroles[0], reason="revived")
	await killed.add_roles(healthroles[1], reason="revived")

@commands.cooldown(1, random.randrange(3, 6), commands.BucketType.user)
async def standattack(attacker, attacked, dmg, healthroles, message):
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
	sleeping = discord.utils.get(message.guild.roles, id = 741552665892356147)

	
	if healthroles[0] in message.author.roles or healthroles[0] in message.mentions[0].roles or scared in message.author.roles or sleeping in message.author.roles:
		return
	if stand in attacked.roles:
		await message.channel.send("attack the user, not the stand")
		return
	if enraged in attacked.roles:
		message.channel.send("user is in a blind rage, you cannot damage them")
		return
	if enraged_victim in attacked.roles and enraged in attacker.roles:
		dmg = dmg*2
	for x in range(dmg):
		if (healthroles[10] in attacked.roles):
			await attacked.remove_roles(healthroles[10],reason="attacked")
			await attacked.add_roles(healthroles[9],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[9] in attacked.roles):
			await attacked.remove_roles(healthroles[9],reason="attacked")
			await attacked.add_roles(healthroles[8],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[8] in attacked.roles):
			await attacked.remove_roles(healthroles[8],reason="attacked")
			await attacked.add_roles(healthroles[7],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[7] in attacked.roles):
			await attacked.remove_roles(healthroles[7],reason="attacked")
			await attacked.add_roles(healthroles[6],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[6] in attacked.roles):
			await attacked.remove_roles(healthroles[6],reason="attacked")
			await attacked.add_roles(healthroles[5],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[5] in attacked.roles):
			await attacked.remove_roles(healthroles[5],reason="attacked")
			await attacked.add_roles(healthroles[4],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[4] in attacked.roles):
			await attacked.remove_roles(healthroles[4],reason="attacked")
			await attacked.add_roles(healthroles[3],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[3] in attacked.roles):
			await attacked.remove_roles(healthroles[3],reason="attacked")
			await attacked.add_roles(healthroles[2],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[2] in attacked.roles):
			await attacked.remove_roles(healthroles[2],reason="attacked")
			await attacked.add_roles(healthroles[1],reason="attacked")
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with a stand for {dmg} health!")
		elif (healthroles[1] in attacked.roles):
			await message.channel.send(f"{attacker.name} killed {attacked.name} with a stand!")
			killed = attacked
			await kill(killed, healthroles)

@commands.cooldown(1, 5, commands.BucketType.user)
async def hamonattack(attacker, attacked, dmg, healthroles, message):
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
	sleeping = discord.utils.get(message.guild.roles, id = 741552665892356147)

	
	if healthroles[0] in message.author.roles or healthroles[0] in message.mentions[0].roles or scared in message.author.roles or sleeping in message.author.roles:
		return
	if stand in attacked.roles:
		await message.channel.send("attack the user, not the stand")
		return
	if enraged in attacked.roles:
		message.channel.send("user is in a blind rage, you cannot damage them")
		return
	if enraged_victim in attacked.roles and enraged in attacker.roles:
		dmg = dmg*2
	for x in range(dmg):
		if (healthroles[10] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[10],reason="attacked")
			await attacked.add_roles(healthroles[9],reason="attacked")
		elif (healthroles[9] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[9],reason="attacked")
			await attacked.add_roles(healthroles[8],reason="attacked")
		elif (healthroles[8] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[8],reason="attacked")
			await attacked.add_roles(healthroles[7],reason="attacked")
		elif (healthroles[7] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[7],reason="attacked")
			await attacked.add_roles(healthroles[6],reason="attacked")
		elif (healthroles[6] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[6],reason="attacked")
			await attacked.add_roles(healthroles[5],reason="attacked")
		elif (healthroles[5] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[5],reason="attacked")
			await attacked.add_roles(healthroles[4],reason="attacked")
		elif (healthroles[4] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[4],reason="attacked")
			await attacked.add_roles(healthroles[3],reason="attacked")
		elif (healthroles[3] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[3],reason="attacked")
			await attacked.add_roles(healthroles[2],reason="attacked")
		elif (healthroles[2] in attacked.roles):
			await message.channel.send(f"{attacker.name} attacked {attacked.name} with hamon for {dmg} health!")
			await attacked.remove_roles(healthroles[2],reason="attacked")
			await attacked.add_roles(healthroles[1],reason="attacked")
		elif (healthroles[1] in attacked.roles):
			await message.channel.send(f"{attacker.name} killed {attacked.name} with hamon")
			killed = attacked
			await kill(killed, healthroles)

@commands.cooldown(1, 30, commands.BucketType.user)
async def heal(healed, points, healthroles):
	if healthroles[0] in healed.roles:
		return
	for x in range(points):
		if (healthroles[10] in healed.roles):
			points = 0
			break
		elif (healthroles[9] in healed.roles):
			await healed.remove_roles(healthroles[9],reason="healed")
			await healed.add_roles(healthroles[10],reason="healed")
		elif (healthroles[8] in healed.roles):
			await healed.remove_roles(healthroles[8],reason="healed")
			await healed.add_roles(healthroles[9],reason="healed")
		elif (healthroles[7] in healed.roles):
			await healed.remove_roles(healthroles[7],reason="healed")
			await healed.add_roles(healthroles[8],reason="healed")
		elif (healthroles[6] in healed.roles):
			await healed.remove_roles(healthroles[6],reason="healed")
			await healed.add_roles(healthroles[7],reason="healed")
		elif (healthroles[5] in healed.roles):
			await healed.remove_roles(healthroles[5],reason="healed")
			await healed.add_roles(healthroles[6],reason="healed")
		elif (healthroles[4] in healed.roles):
			await healed.remove_roles(healthroles[4],reason="healed")
			await healed.add_roles(healthroles[5],reason="healed")
		elif (healthroles[3] in healed.roles):
			await healed.remove_roles(healthroles[3],reason="healed")
			await healed.add_roles(healthroles[4],reason="healed")
		elif (healthroles[2] in healed.roles):
			await healed.remove_roles(healthroles[2],reason="healed")
			await healed.add_roles(healthroles[3],reason="healed")
		elif (healthroles[1] in healed.roles):
			await healed.remove_roles(healthroles[1],reason="healed")
			await healed.add_roles(healthroles[2],reason="healed")

async def sleepheal(healed, healthroles, sleeping):
	while True:
		await asyncio.sleep(300)
		if healthroles[10] in healed.roles:
			await healed.remove_roles(sleeping, reason="healed to max")
			break
		if not sleeping in healed.roles:
			break
		elif (healthroles[9] in healed.roles):
			await healed.remove_roles(healthroles[9],reason="healed")
			await healed.add_roles(healthroles[10],reason="healed")
		elif (healthroles[8] in healed.roles):
			await healed.remove_roles(healthroles[8],reason="healed")
			await healed.add_roles(healthroles[9],reason="healed")
		elif (healthroles[7] in healed.roles):
			await healed.remove_roles(healthroles[7],reason="healed")
			await healed.add_roles(healthroles[8],reason="healed")
		elif (healthroles[6] in healed.roles):
			await healed.remove_roles(healthroles[6],reason="healed")
			await healed.add_roles(healthroles[7],reason="healed")
		elif (healthroles[5] in healed.roles):
			await healed.remove_roles(healthroles[5],reason="healed")
			await healed.add_roles(healthroles[6],reason="healed")
		elif (healthroles[4] in healed.roles):
			await healed.remove_roles(healthroles[4],reason="healed")
			await healed.add_roles(healthroles[5],reason="healed")
		elif (healthroles[3] in healed.roles):
			await healed.remove_roles(healthroles[3],reason="healed")
			await healed.add_roles(healthroles[4],reason="healed")
		elif (healthroles[2] in healed.roles):
			await healed.remove_roles(healthroles[2],reason="healed")
			await healed.add_roles(healthroles[3],reason="healed")
		elif (healthroles[1] in healed.roles):
			await healed.remove_roles(healthroles[1],reason="healed")
			await healed.add_roles(healthroles[2],reason="healed")
