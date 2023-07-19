import discord
from discord.ext import commands
import os 
import sys
import json
import asyncio

####################################################################################################
# This bot was made by Jomi#7153 please do not give out the code without permission                #
####################################################################################################

TOKEN = ""

cogs = [
    'help',
    'game',
    'ticket'
]

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix=";", case_insensitve=True)

        self.check = ":white_check_mark:"
        self.x = ":x:"
        self.error=0xFF0000
        self.embed=0x000080
        self.reactionchannel=817605633880621086
        self.ticketcategory=817598210541486091
        self.devs = [
            148292553681141760,  # Jomi
            285975702774480897, # Noodle
            158020304466083840 # Intrinsic
        ]

    async def on_ready(self):
        print(f"Please wait...\n")

        activityName = await self.addToConfig()

        activity = discord.Activity(name=activityName, type=discord.ActivityType.playing)
        await bot.change_presence(activity=activity)
        channel=self.get_channel(self.reactionchannel)
        await channel.purge()
        embed=discord.Embed(title="**Create A Ticket**" , description="Create a support ticket by reacting!",color=0x008000)
        embed.set_footer()
        msg = await channel.send(embed=embed)
        await msg.add_reaction('\U0001f39f')

        for cog in cogs:
            try:
                bot.load_extension(cog)
                print(f"Loaded {cog}")
            except Exception as e:
                print(e)

        print(f"\nComplete.")

    async def addToConfig(self):
        f = open('config.json',) 
        data = json.load(f) 
        f.close() 
        return data

bot = Bot()
bot.remove_command('help')

@bot.command()
async def restart(ctx):
  if not ctx.author.id in bot.devs:
    return
  embed=discord.Embed(name="Restarting",description="Restarting. Please wait.",color=bot.embed)
  await ctx.send(embed=embed)
  await bot.change_presence(status = discord.Status.dnd, activity = discord.Game("RESTARTING BOT!"))
  os.execv(sys.executable, ['python3'] + sys.argv)

@bot.command()
async def reload(ctx, cog = None):
    if not ctx.author.id in bot.devs:
        return
    if not cog:
        return
    try:
        bot.reload_extension(cog)
        embed=discord.Embed(name="Reloading",description=F"{bot.check} Successfully reloaded **{cog}**!",color=bot.embed)
        await ctx.send(embed=embed)
    except Exception as e:
        embed=discord.Embed(name="Reloading",description=F"{bot.x} couldn't reload **{cog}**!\n**({e})**",color=bot.embed)
        await ctx.send(embed=embed)

bot.run(TOKEN)