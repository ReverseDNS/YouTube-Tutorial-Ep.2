import json
import discord
from discord.ext import commands

#Importing Config Information
file = open("config.json", "r")
config = json.load(file)
file.close()

#Bot Prefix & Remove help command
client = commands.Bot(command_prefix=(config["prefix"]))
client.remove_command('help')

#Bot Online Command & Status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".help | BOTNAME"))
    print(f"{client.user} is online!")

#Basic Ping Command
@client.command()
async def ping(ctx):
    await ctx.channel.send(":ping_pong: Pong!")

#Token Login
client.run(config["token"])