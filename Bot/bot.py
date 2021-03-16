import discord
from discord.ext import commands
import beeScript
import time
import json
import lotr
import keep_alive

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Bot is ready.') 

@client.command(name='spamme')
async def spamme(ctx, *name: str):
    if ctx.author == client.user:
        return
    line = 1
    if("shrek" in ''.join(name)):
        for i in beeScript.shrek:
            if(i.strip()):
                print('sent ' + str(ctx.author) + ' ' + str(line))
                await ctx.author.send(i)
                line+=1
                time.sleep(1)
    elif('bee' in ''.join(name)):
        for i in beeScript.bee:
            if(i.strip()):
                print('sent ' + str(ctx.author) + ' ' + str(line))
                await ctx.author.send(i)
                line+=1
                time.sleep(1)
    elif('lotr' in ''.join(name)):
        for i in lotr.script:
            if(i.strip()):
                print('sent ' + str(ctx.author) + ' ' + str(line))
                await ctx.author.send(i)
                line+=1
                time.sleep(1)
                
                
    else:
        await ctx.send("We don't got that movie in stock, home dawg, but you can get shrek 2, the bee movie and Lord of the rings")
    
    
    

@client.command(name='stop')
async def stop(ctx):
    await ctx.send("Don't be a baby, read it!")


client.run('NzA5NDc5MTgwNTYzMjUxMjMx.Xrmf-g.z2SX5L_-Kr2vB5S2eme9CQPRPwY')