from discord.ext import commands

class Server(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def or_ready(self):
        print("Server start")

def setup(bot):
    bot.add_cog(Server(bot))