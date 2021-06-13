from discord.ext import commands
from asyncio import sleep
from database import get_all, Muted, delete_mute
from datetime import datetime
from configs.config import main_guild, mute_role

class Timer(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Timer start")
        guild = self.bot.get_guild(main_guild)
        while True:
            for user in get_all(Muted):
                if datetime.now() >= user.timewarn:
                    print(type(user))
                    member = guild.get_member(user.id)
                    role = guild.get_role(mute_role)
                    delete_mute(user)
                    await member.send("С тебя сняли мут.")
                    await member.remove_roles(role)
            await sleep(30)

def setup(bot):
    bot.add_cog(Timer(bot))