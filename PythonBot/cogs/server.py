from discord import activity, client
from discord.ext import commands
import discord
import socket
import msgpack as mp
import asyncio
import threading
from configs.config import main_guild



async def create_server(bot):
    guild = bot.get_guild(main_guild)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0",9090))
    while True:
        request, addr = sock.recvfrom(1024)
        data = mp.unpackb(request)
        if data == "join":
            count_members = 0
            member = guild.get_member(613269904963141643)
            channels = []
            for channel in guild.channels:
                if channel.type is discord.ChannelType.text:
                    channels.append((channel.name,channel.id))
            channels = tuple(channels)
            for Member in guild.members:
                if not Member.bot:
                    count_members += 1
            sock.sendto(mp.packb([member.activities[0].name,channels,count_members]),addr)

        if data[0] == "CS":
            await bot.change_presence(status=discord.Status.idle,activity=discord.Game(data[1]))
            sock.sendto(b"succ",addr)

        if data[0] == "SM":
            channel = guild.get_channel(data[1])
            bot.loop.create_task(channel.send(data[2]))


class Server(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Server start")
        _thread = threading.Thread(target=asyncio.run,args=(create_server(self.bot),))
        _thread.start()




def setup(bot):
    bot.add_cog(Server(bot))