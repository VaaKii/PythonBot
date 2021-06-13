from discord.ext import commands
from asyncio import sleep
from configs.config import main_guild, channel_count_users

class Timer5(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Timer 5 min start")
        guild = self.bot.get_guild(main_guild)
        channel = guild.get_channel(channel_count_users)
        while True:
            await channel.edit(name=f"Людей на сервере: {guild.member_count}")
            await sleep(300)

def setup(bot):
    bot.add_cog(Timer5(bot))