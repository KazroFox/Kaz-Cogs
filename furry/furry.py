import discord
from discord.ext import commands

class Furry:
    """A cog that adds weird furry commands or something"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def owo(self, user : discord.Member):
        """OwO what's this?"""
        await self.bot.say("*Notices " + user.mention + "'s bulge* OwO what's this?")
    
    @commands.command()
    async def succ(self, user : discord.Member):
        """Someone gonna get some *succ*"""
        await self.bot.say("*Pleasures " + user.mention + " with my mighty fine fox succ skills*")

def setup(bot):
    bot.add_cog(Furry(bot))
