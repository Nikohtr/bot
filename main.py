import discord
import os
from discord.ext import commands
import asyncio
from discord.utils import get
import random
import re

client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    
@client.command(pass_context = True)
@commands.has_role("Admin")
async def locolives(ctx):
    if message.channel.type != discord.ChannelType.private:
        await client.say("What's your referral")
        ref = await bot.wait_for_message(author=ctx.message.author)
        await client.say("How many lives would you like?")
        num = await bot.wait_for_message(author=ctx.message.author)
        await client.send_message(client.get_channel("536980166719832075"), "{0.author.mention} , "+ref+", " +num+"".format(ctx.message))
        await client.say("Your lifes will come within 24 hours")
    else:
        await client.send_message(ctx.message.channel, "This bot isn't made for DMs")

    
@client.command(pass_context = True)
@commands.has_role("Admin")
async def lococoins(ctx):
    if message.channel.type != discord.ChannelType.private:
        await client.say("What's your referral")
        ref = await bot.wait_for_message(author=ctx.message.author)
        await client.say("What's your phone number?")
        num = await bot.wait_for_message(author=ctx.message.author)
        regrex = r"^([0]|\+91)?[789]\d{9}$"
        if re.search(regrex, num):
            pass
        else:
            while not re.search(regrex, num):
                await client.say("What's your phone number?")
                num = await bot.wait_for_message(author=ctx.message.author)  
        await client.send_message(client.get_channel("536986693878808596"), "{0.author.mention} , "+ref+", " +num+"".format(ctx.message))
    else:
        await client.send_message(ctx.message.channel, "This bot isn't made for DMs")

        
@client.command(pass_context = True)
@commands.has_role("Admin")
async def locoverify(ctx, user: discord.Member):
    if message.channel.type != discord.ChannelType.private:
        if not user: await client.say("Please specify a user")
        else:
            await client.send_message(await client.get_user_info(user), "Hey can you send me your OTP to claim your loco coins")
            otp = await bot.wait_for_message(author=user)
            await client.send_message(client.get_channel("536986693878808596"), user+", "+ otp)
    else:
        await client.send_message(ctx.message.channel, "This bot isn't made for DMs")



token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
