from discord import activity
from discord.ext import commands
import discord
import socket
import msgpack as mp

def create_sock() -> socket.socket:
    return socket.socket(socket.AF_INET,socket.SOCK_STREAM)
class Server(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Server start")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("127.0.0.1",9090))
        while True:
            request, addr = sock.recvfrom(1024)
            data = mp.unpackb(request)
            if data == "join":
                print(self.bot.activity)
            if data[0] == "CS":
                print(self)
                await self.bot.change_presence(status=discord.Status.idle,activity=discord.Game(data[1]))
                sock.sendto(b"succ",addr)




def setup(bot):
    bot.add_cog(Server(bot))