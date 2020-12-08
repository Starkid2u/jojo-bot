import discord
import asyncio
import random
import json
from discord.ext import commands


async def kill(killed, healthroles):
	await killed.remove_roles(healthroles[3], reason="killed")
	await killed.add_roles(healthroles[4], reason="killed")
	await asyncio.sleep(3600)
	await killed.remove_roles(healthroles[4], reason="revived")
	await killed.add_roles(healthroles[3], reason="revived")

with open("health.json","rt") as rawhealth:
	health = json.loads(rawhealth.read())

async def changehealth(user, add, subtract, healthroles):

	id = str(user.id)

	try:
		health[id] = health[id] + add
		health[id] = health[id] - subtract
		if health[id] >= 76:
			await user.remove_roles(healthroles[1], reason="killed")
			await user.remove_roles(healthroles[2], reason="killed")
			await user.remove_roles(healthroles[3], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[0], reason="killed")
		if health[id] in range(51, 75):
			await user.remove_roles(healthroles[0], reason="killed")
			await user.remove_roles(healthroles[2], reason="killed")
			await user.remove_roles(healthroles[3], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[1], reason="killed")
		if health[id] in range(26, 50):
			await user.remove_roles(healthroles[0], reason="killed")
			await user.remove_roles(healthroles[1], reason="killed")
			await user.remove_roles(healthroles[3], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[2], reason="killed")
		if health[id] in range(1, 25):
			await user.remove_roles(healthroles[0], reason="killed")
			await user.remove_roles(healthroles[1], reason="killed")
			await user.remove_roles(healthroles[2], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[3], reason="killed")
		if health[id] <= 0:
			await kill(killed=user, healthroles=healthroles)
	except KeyError:
		health[id] = 100
		health[id] = health[id] + add
		if health[id] in range(76, 101):
			await user.remove_roles(healthroles[1], reason="killed")
			await user.remove_roles(healthroles[2], reason="killed")
			await user.remove_roles(healthroles[3], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[0], reason="killed")
		if health[id] in range(51, 75):
			await user.remove_roles(healthroles[0], reason="killed")
			await user.remove_roles(healthroles[2], reason="killed")
			await user.remove_roles(healthroles[3], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[1], reason="killed")
		if health[id] in range(26, 50):
			await user.remove_roles(healthroles[0], reason="killed")
			await user.remove_roles(healthroles[1], reason="killed")
			await user.remove_roles(healthroles[3], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[2], reason="killed")
		if health[id] in range(1, 25):
			await user.remove_roles(healthroles[0], reason="killed")
			await user.remove_roles(healthroles[1], reason="killed")
			await user.remove_roles(healthroles[2], reason="killed")
			await user.remove_roles(healthroles[4], reason="killed")
			await user.add_roles(healthroles[3], reason="killed")
		if health[id] <= 0:
			await kill(killed=user, healthroles=healthroles)
		print(f"{user} didnt have health but now they do")

	healthfile = open("health.json", "wt")
	healthfile.write(json.dumps(health))
	healthfile.close()

async def sleepheal(healed, healthroles, sleeping):
	id = healed.id
	
	while True:
		await asyncio.sleep(300)
		if health[id] >= 100:
			health[id] = 100
			await healed.remove_roles(sleeping, reason="healed to max")
			break
		if not sleeping in healed.roles:
			break
		await changehealth(user=healed, add=random.randrange(1, 10), subtract=0, healthroles=healthroles)