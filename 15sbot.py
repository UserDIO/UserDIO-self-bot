import discord, json, pyfiglet #Very important imports
from discord.ext import commands #cmds
import ctypes #For terminal name and staff
from os import system #os
import time #time 
import random #random
import datetime #date

"""
I know everything here is a mass. But I'm only starting with discord.py
I think this bot isn't a complete garbage but who knows :/

The raid command isn't completed yet. But it _works_. I will update it as time goes on...
"""


bot = commands.Bot(description="UserDIO self-bot", command_prefix=">", self_bot=True)
bot.remove_command('help')




#Help

@bot.command() 
async def cmds(ctx): #List of commands lists
    print(f"\n '>cmds' was executed")
    await ctx.message.delete()
    embed=discord.Embed(title="Commands", color=discord.Color.dark_red())
    embed.add_field(name=f"`>cmds`:", value="Ur looking at it rn", inline=False)
    embed.add_field(name=f"`>fun`:", value="Fun commands", inline=False)
    embed.add_field(name=f"`>hax0r`:", value="Hax0r commands", inline=False)
    embed.add_field(name=f"`Other`", value="Some commands aren't included bc of testing or I didn't make them field", inline=False)
    embed.set_image(url='https://thumbs.gfycat.com/DarlingImmediateKakapo-max-1mb.gif')
    await ctx.send(embed=embed)



@bot.command()
async def fun(ctx): #List of commands 'fun'
    print(f"\n '>fun' was executed")
    await ctx.message.delete()
    embed=discord.Embed(title="Fun commands", color=discord.Color.dark_red())
    embed.add_field(name="`>ascii`:", value="Ascii some text", inline=False)
    embed.add_field(name="`>gp`:", value="ghost ping someone", inline=False)
    embed.add_field(name="`>loop`:", value="Alpha version of spam", inline=False)
    embed.add_field(name="`>ping`:", value="How's your ping doing?", inline=False)
    embed.add_field(name="`>count`:", value="Count before spam", inline=False)
    embed.set_image(url='https://thumbs.gfycat.com/KaleidoscopicEvenAdmiralbutterfly-size_restricted.gif')
    await ctx.send(embed=embed)



@bot.command()
async def hax0r(ctx): #List of commands 'hax0r'
    await ctx.message.delete()
    print(f"\n '>hax0r' was executed")
    embed=discord.Embed(title="Hax0r commands")
    embed.add_field(name="`>rolecreate`:", value="Create role", inline=False)
    embed.add_field(name="`>delete`:", value="Deletes all text channel", inline=False)
    embed.add_field(name="`>raid`:", value="Raid some servers :D", inline=False)
    embed.set_image(url='https://images-ext-2.discordapp.net/external/cU4ozaD4CfGh_uduXjkZa8JHUJY0ZYNEvtscpASJ_68/https/images-ext-2.discordapp.net/external/aBhuAqm09ky32gSOPs3PF0orDLIV_ZEhXgahDvuhUKI/https/media.giphy.com/media/SSNA3uYRmqJm8/giphy.gif')
    await ctx.send(embed=embed)


#fun


@bot.command() #ascii function
async def ascii(ctx, *, args):
    print(f"\n '>ascii' was executed")
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f'``` {text}```')
    


@bot.command() #ghost ping
async def gp(ctx):
    print(f"\n '>gp' was executed")
    await ctx.message.delete()



@bot.command() #Spam
async def loop(ctx, *, text):
    print(f"\n '>loop {text}' was executed")
    while True:
        await ctx.send(f"{text}")



@bot.command() # count command xd
async def count(ctx):
    print(f"\n '>count' was executed")
    i = 5
    y = 1
    while i > 0:
        await ctx.send(i)
        i -= 1
        
    
    while y < 10:
        await ctx.send(f'Why are you gay?')
        y += 1
        
    print(f"\n '>count' has ended")



@bot.command()
async def ping(ctx):
    print(f"\n '>ping' was executed")
    await ctx.send(f'bababooey :flushed:')
    await ctx.send(f'My ping is: {round(bot.latency * 1000)}ms!')



#hax0r


@bot.command()
async def rolecreate(ctx, roleName):
    print(f"\n '>rolecreate' was executed")
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_roles:
        await ctx.message.delete()
        await guild.create_role(name=f"{roleName}")
        await ctx.send(f'Role named {roleName} was created')
    else:
        print("\n Missing permission 'manage_roles'")
        await ctx.send(f'You dont have permission')



@bot.command()
async def raid(ctx):
    print(f"\n'>raid' was executed")
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()
        
        channels = 0
        while channels < 50:
            await guild.create_text_channel('ᴿᵃᶦᵈ ᵇʸ ᵁˢᵉʳᴰᴵᴼ')
            channels += 1
        
        
        roles = 0
        while roles < 50:
            await guild.create_role(name=f"Raid by UserDIO")
            roles += 1



@bot.command() #delete all channels
async def delete(ctx):
    print(f"\n'>delete' was executed")
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()
  


@bot.command() #Nsfw command
async def nsfw(ctx):
    print(f"\n'>nsfw' command was executed")
    embed=discord.Embed(title="Test")
    embed.set_image(url='https://media.discordapp.net/attachments/739239063541776486/808456584052604978/637_1000.gif')
    await ctx.send(embed=embed)
    
    
    
 # I dunno (Just for now :) ) 

    
@bot.command(pass_context=True)
async def clear(ctx, limit: int=None):
    print(f"\n'>clear' was executed")
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"\nComplete Removed {passed} messages with {failed} fails")




with open('./config.json') as f: # open for token
    config = json.load(f)
    
   
   
"""
Mᴀɪɴ ᴍᴇɴᴜ
"""

ctypes.windll.kernel32.SetConsoleTitleW("HackerHex - Menu") #Terminal name
#introduction
print("  _   _            _             _   _           ")
time.sleep(0.3)
print("| | | | __ _  ___| | _____ _ __| | | | _____  __ ")
time.sleep(0.3)
print("| |_| |/ _` |/ __| |/ / _ \ '__| |_| |/ _ \ \/ / ")
time.sleep(0.3)
print("|  _  | (_| | (__|   <  __/ |  |  _  |  __/>  <  ")
time.sleep(0.3)
print("|_| |_|\__,_|\___|_|\_\___|_|  |_| |_|\___/_/\_\ ")
time.sleep(0.3)
print("=" * 50)




#token
token = config.get('token')
bot.run(token, bot=False)
