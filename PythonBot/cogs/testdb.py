from discord.ext import commands
from database import *

class Test_DB(commands.Cog):
    "This is test db, only owner."
    def __init__(self,bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def test(self,ctx):
        "Test"
        await ctx.send(get_user("123"))

    

def setup(bot):
    bot.add_cog(Test_DB(bot))