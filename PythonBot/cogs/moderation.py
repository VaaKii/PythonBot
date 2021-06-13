from discord.ext import commands
from discord import Member
from database import Muted, add_mute
from datetime import datetime, timedelta 
import os
import time

os.environ["TZ"] = "Russia/Moscow"
time.tzset()

def mute_member(id,hours):
    time = datetime.now() + timedelta(hours=hours)
    add_mute(Muted(id=id,timewarn=time))

class Moderate(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def mute(self,ctx,member: Member, hours: int):
        mute_member(member.id, hours)
        await member.send(f"Тебе выбали мут на {hours} час(а/ов).")

def setup(bot):
    bot.add_cog(Moderate(bot))