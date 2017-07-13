import discord
from discord.ext import commands

class Furry:
    """A cog that adds weird furry commands or something"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def owo(self):
        """OwO what's this?"""

        await self.bot.say("*Notices " + user.mention + "'s bulge* OwO what's this?")

def setup(bot):
    bot.add_cog(Furry(bot))
