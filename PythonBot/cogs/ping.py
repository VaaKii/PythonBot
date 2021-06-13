from discord.ext import commands

class Ping(commands.Cog):
    "Bot with ping? You kidding?"
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        "Ping pong, what more."
        await ctx.send("Pong!")

def setup(bot):
    bot.add_cog(Ping(bot))