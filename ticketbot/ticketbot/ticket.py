import discord 
from discord.ext import commands 
import asyncio

####################################################################################################
# This bot was made by Jomi#7153 please do not give out the code without permission                #
####################################################################################################

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.confirmation = False

    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):        
        zuser=user
        guild=reaction.message.guild

        if user.bot:
            return
        if str(reaction.emoji) == "\U0001f39f" and (reaction.message.channel.id) == self.bot.reactionchannel:
            await reaction.message.remove_reaction(reaction, user)
            guild=reaction.message.guild
            overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    guild.me: discord.PermissionOverwrite(read_messages=True,send_messages=True),
                    user: discord.PermissionOverwrite(read_messages=True,send_messages=True)
            }
            uname=user.name
                
            name="ticket-"+uname+"-"+str(user.id)
            name.replace(" ", "-")
            channel = await guild.create_text_channel(name,overwrites=overwrites,category=self.bot.get_channel(self.bot.ticketcategory))
            
            embed=discord.Embed(title="Welcome To Your Ticket - Step 1" , description="**To get started, please provide your account name.**",color=self.bot.embed)
            msg=await channel.send(content=user.mention,embed=embed)
            def check(m):
                return (m.channel == channel and m.author==zuser)
                        
            res1 = await self.bot.wait_for('message', check=check)
            await res1.delete()
            embed=discord.Embed(title="Welcome To Your Ticket - Step 2" , description=F"Please state the issue as best as possible, someone will be with you shortly. To close the ticket please press the lock button at any time.",color=self.bot.embed)
            await msg.edit(embed=embed)
            await msg.add_reaction('\U0001F512')

            def reactioncheck(reaction,user):
                if (not user.bot):
                    if reaction.message.id==msg.id:
                        if reaction.emoji in ['\U0001F512']:
                            self.confirmation=True
                            return True
                return False
            
            reaction, user = await self.bot.wait_for("reaction_add", check=reactioncheck)

            if (self.confirmation==True):
                await msg.remove_reaction(reaction, user)
                embed=discord.Embed(title="You have locked the ticket..." , description=F"We hope to have helped, the ticket will close shortly. Have a good day!",color=self.bot.embed)
                await msg.channel.send(embed=embed)
                await asyncio.sleep(5)
                await msg.channel.delete()

def setup(bot): 
    bot.add_cog(Admin(bot))