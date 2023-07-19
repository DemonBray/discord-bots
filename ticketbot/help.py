import discord
from discord.ext import commands
import asyncio

####################################################################################################
# This bot was made by Jomi#7153 please do not give out the code without permission                #
####################################################################################################

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True) #!HELP COMMAND FOR ALL THE DUMB DUMBS
    async def help(self,ctx):
        if ctx.invoked_subcommand is None:
            embed=discord.Embed(name="Help",description="Arguments surrounded in [] are required. Arguments surrounded in () are optional.",color=self.bot.embed)
            embed.add_field(name="!help (admin)",value="- For those who forgot.",inline=False)
            await ctx.send(embed=embed)
    
    @help.command()
    async def admin(self,ctx):
        for role in ctx.message.author.roles:
            if role.name == 'Admin' or role.name == 'Mod':
                embed=discord.Embed(name="Help",description="Arguments surrounded in [] are required. Arguments surrounded in () are optional.",color=self.bot.embed)
                embed.add_field(name="!game [new status]",value="- Change bot's playing status.",inline=False)
                embed.add_field(name="!name [new status]",value="- Change bot's name.",inline=False)
                await ctx.send(embed=embed)
                return
        embed=discord.Embed(name="Error:", description="You do not have permission to see those commands!",color=self.bot.embed)
        await ctx.send(embed=embed)

def setup(bot): 
    bot.add_cog(Users(bot))