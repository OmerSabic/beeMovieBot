import discord
from discord.ext import commands

import time
import json
import os
import requests

## Script files
import beeScript
import lotr
import meinKampf as kampf
import communism
import test


from dotenv import load_dotenv
import sys
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("TOKEN")
API_SECRET = os.getenv("API_SECRET")

api_url = "https://beebotwebsite.omersabic.repl.co"

client = commands.Bot(command_prefix='$')

sending = []

@client.event
async def on_ready():
    activity = discord.Game(name="OUR NEW QUEEN BEE! TAXKING!", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    


scriptList = {
    "shrek2": beeScript.shrek,
    "bee": beeScript.bee,
    "lotr": lotr.script,
    "kampf": kampf.hitler,
    "communistmanifesto": communism.communism,
    "test": test.test
}


async def spam(ctx, script, scriptName):
    line = 1
    if str(ctx.author.id) in sending:
        embed = discord.Embed(
            title="You are already being sent messages! Wait for the current one to finish.", 
            color=0xc0c0c0
        )
        await ctx.send(embed=embed)
        return
    sending.append(str(ctx.author.id))
    for i in script:
        try:
            if (i.strip()):
                await ctx.author.send(i)
                line += 1
                time.sleep(1)
        except:
            embed = discord.Embed(title="Whoops! Looks like *%s* was a little wussy and couldn't handle a little spam." % ctx.author.name,description=sys.exc_info() ,color=0xc0c0c0)
            sending.remove(str(ctx.author.id))
            await ctx.send(embed=embed)
            return

    sending.remove(str(ctx.author.id))
    
    requests.put(
        api_url + "/api/user/increment/" +
        str(ctx.author.id) + "/" + str(scriptName) + "/" + str(API_SECRET))




@client.command(name="stats")
async def stats(ctx, member: discord.User = None):
    if (member == None):
        member = ctx.author

    if(str(member.id) == "327397589668331520" and str(ctx.author.id) not in ["327397589668331520", "357493109460041730"]):
        await ctx.send('no')

    dat = requests.get(api_url + "/api/user/" +
                       str(member.id))

    if (dat.status_code == 400):
        await ctx.send(
            "That user hasn't used Bee Movie Bot yet. TEACH THEM THE WAY!!!")

    data = json.loads(dat.text)

    embed = discord.Embed(
        title="BeeMovieBot stats website link",
        url=api_url + "/info/" + str(member.id),
        color=0xc0c0c0)
    embed.set_author(name=member.name + "#" + member.discriminator)

    dong = {
        "Bee Movie": data["bee"],
        "Lord of The Rings": data["lotr"],
        "Shrek 2": data["shrek2"],
        "The Communist Manifesto": data["communistmanifesto"],
        "Mein Kampf": data["kampf"]
    }

    embed.set_thumbnail(url=member.avatar_url)
    for key, value in dong.items():
        embed.add_field(name=str(key), value=value, inline=False)

    await ctx.send(embed=embed)


@client.command(name="girl")
async def girl(ctx):
    await ctx.send(
        "A girl.... AND a gamer? Whoa mama! Hummina hummina hummina bazooooooooing! eyes pop out AROOOOOOOOGA! jaw drops tongue rolls out WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF tongue bursts out of the mouth uncontrollably leaking face and everything in reach WURBLWUBRLBWURblrwurblwurlbrwubrlwburlwbruwrlblwublr tiny cupid shoots an arrow through heart Ahhhhhhhhhhh me lady... heart in the shape of a heart starts beating so hard you can see it through shirt ba-bum ba-bum ba-bum ba-bum ba-bum milk truck crashes into a bakery store in the background spiling white liquid and dough on the streets BABY WANTS TO FUCK inhales from the gas tank honka honka honka honka masturabtes furiously ohhhh my gooooodd~"
    )


@client.command(name='stop')
async def stop(ctx):
    await ctx.send("Don't be a baby, read it!")

client.run(SECRET_KEY)