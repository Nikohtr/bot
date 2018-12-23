import discord
import os
from discord.ext import commands
import asyncio
from discord.utils import get
import random
import urllib.request
import json
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role



loop = True

client = commands.Bot(command_prefix='+')
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    client.loop.create_task(change_playing())

@client.command()
async def gap():
    key = os.getenv("KEY")
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
    subspew = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    data1 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+key).read()
    subst = json.loads(data1)["items"][0]["statistics"]["subscriberCount"]
    gapis=int(subspew)-int(subst)
    await client.say("T-series is "+"{:,d}".format(int(gapis))+" subs away from Pewdiepie")

@client.command()
async def dislikes():
    key = os.getenv("KEY")
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=YbJOTdZBX1g&key="+key).read()
    dis = json.loads(data)["items"][0]['statistics']['dislikeCount']
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=kffacxfA7G4&key="+key).read()
    dis1 = json.loads(data)["items"][0]['statistics']['dislikeCount']
    raz = int(dis)-int(dis1)
    await client.say("Youtube Rewind 2018 has {:,d}".format(int(dis))+" dislikes. That's {:,d}".format(int(raz))+" above Justin Bieber's Baby")

@client.command(pass_context = True)
async def say(ctx, *, mg = None):
    if ctx.message.author.id == "263685060819943425":
      await client.delete_message(ctx.message)

      if not mg: await client.say("Please specify a message to send")
      else: await client.say(mg)

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return True
    else:
        return False
lp = True
@client.command(pass_context = True)
@has_permissions(administrator = True)
async def color(ctx):
    global lp
    lp = True
    role = get(ctx.message.server.roles, id="517751310989131796")
    await client.send_message(ctx.message.channel, "**Started rainbow colored roles!**")
    while lp:
      r = lambda: random.randint(0,255)
      color = ('%02X%02X%02X' % (r(),r(),r()))
      await client.edit_role( ctx.message.server, role, color = discord.Colour(value = int(color, 16)))
      await asyncio.sleep(2)

@client.command(pass_context = True)
@has_permissions(administrator = True)
async def stopcolor(ctx):
    global lp
    lp = False
    await client.send_message(ctx.message.channel, "**Stoped rainbow colored roles!**")


@client.command(pass_context = True)
async def word(ctx, *, word=None):
    global loop
    if ctx.message.author.id == "263685060819943425":
      await client.send_message(ctx.message.channel, "Saying "+word+" 100,000 times")
      await client.delete_message(ctx.message)
      times = 2000//(len(word)+2)
      to100 = 100000//times
      count = 0
      if not word: await client.say("Please specify a word to say 100,000 times"))
      else: 
        while count<=to100:
          loop = False
          await client.change_presence(game=discord.Game(name='SAYING '+word+" 100,000 TIMES."))
          await client.send_message(client.get_channel('518709484634243082'), ("\n"+word)*times)
          count+=1
        await client.send_message(client.get_channel('518709484634243082'), "I said "+word+" 100,000 times") 
        if count>=to100:
          loop=True
          await change_playing() 

@client.event
async def on_member_remove(member):
    await client.send_message(client.get_channel('517765643114643457'),member.display_name+" wasn't a real mate so he left. HAHA WHAT A NOOB!!!")

@client.event
async def change_playing():
    global loop
    while loop:
      await client.change_presence(game=discord.Game(name='SUBSCIBING TO PEWDIEPIE'))
      await asyncio.sleep(10)
      await client.change_presence(game=discord.Game(name='UNSUBSCIBING FROM T-SERIES'))
      await asyncio.sleep(10)
  
@client.event
async def on_message_edit(old, new):
    await on_message(new)

@client.event
async def on_message(message):
    m = message.content
    m = m.lower()
    await client.process_commands(message)
    if message.author != client.user:
      if (message.content.startswith("+") and message.author.id == "263685060819943425"):
        pass
      elif message.content=="+gap" or message.content=="+dislikes":
        pass
      elif isEnglish(message.content):
        await client.delete_message(message)
        await client.send_message(message.channel, "That's not very nice you know. I only understand English")

      else:    
        if "mate" in m or "m8" in m or ":mate:" in m or message.attachments:
          if message.channel.id != '517780380049473563':
            mesg = "Thank you mate, very cool!!!"
            await client.send_message(message.channel, mesg)
          else:
              num = random.randint(1,3)
              if num == 1:
                msg1="YOU CAN'T SAY THAT YOU LITTLE RAT!!!"
              elif num == 2:
                msg1="DON'T EVEN THINK ABOUT IT!!!"  
              elif num == 3:
                msg1="NO, NO AND NO!!!"
              await client.send_message(message.channel, msg1)
              await asyncio.sleep(0.5)
              await client.delete_message(message)    
        else:
          if message.channel.id != '517780380049473563':  
            mesg = "WTF {0.author.mention}???".format(message)
            await client.send_message(message.channel, mesg)
            if message.channel.id != "518086090436116491":
              await client.send_message(client.get_channel('517765643114643457'), "{0.author.mention}".format(message))
              role = get(message.server.roles, id='517774248010579969')
              await client.add_roles(message.author, role)
              await asyncio.sleep(0.5)
              await client.delete_message(message)
              role1 = get(message.server.roles, id='517751378802638904')
              await client.remove_roles(message.author, role1)
              await client.change_nickname(message.author, message.author.display_name.replace("MATE", "LOSER"))
          else:
            await client.send_message(message.channel, "YOU ARE A DISAPPOINTMENT FOR EVERYONE!!!")    


token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)