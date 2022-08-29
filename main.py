import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

from discord.ext import commands
from discord.utils import get
client = discord.Client()

bot = commands.Bot(command_prefix = 'pain!') #put your own prefix here

@bot.command(pass_context=True)

async def roleplease(message):
    await message.channel.send("Welcome to the pain        server. Here have a free role.")

    member = message.author
    role = get(member.guild.roles, name="pain 1")
    await member.add_roles(role)
@bot.command(pass_context=True)
async def ok(message):
    await message.channel.send("yes")
@bot.command(pass_context=True)

async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f"{text}")
bot.run("MTAxMTgyNTI5ODMzNTA3MjM0OA.G60KLM.zC2PfZbuTd_0a7_cCdcQ9bzYOFGcMi81m4AOl0") 
#get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!
