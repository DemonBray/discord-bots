import discord 
from discord.ext import commands
import asyncio
import json

####################################################################################################
# This bot was made by Jomi#7153 please do not give out the code without permission                #
####################################################################################################

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def addToConfig(self, data):
        with open('config.json', 'w') as outfile:
            json.dump(data, outfile)

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def game(self,ctx,*,value=None):
        if not value:
            embed=discord.Embed(title="Incorrect Command Usage.",description="The correct usage of this command is `!game [new status]`.",color=self.bot.error)
            td=await ctx.send(embed=embed)
        activity = discord.Activity(name=value, type=discord.ActivityType.playing)
        await self.addToConfig(value)
        await self.bot.change_presence(activity=activity)
        
def setup(bot): 
    bot.add_cog(Users(bot))