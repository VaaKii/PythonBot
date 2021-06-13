from discord.ext import commands
from discord import Embed, Colour
from configs.config import role_newprogrammer, role_unsociable, channel_count_users, main_guild, come_out_channel, banwords
from database import *
from fuzzywuzzy import fuzz

class Listener(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        import os,time
        os.environ["TZ"] = 'Europe/Moscow'
        time.tzset()
        guild = self.bot.get_guild(main_guild)
        channel = guild.get_channel(channel_count_users)
        for member in guild.members:
            if member.bot is False:
                user = get_user(member.id)
                if user is None:
                    add_user(User(id=member.id,experience=0,money=0,level=1))
        for user in all():
            if not guild.get_member(user.id):
                delete_user(user)        
        print("Bot started!")
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        role_new = member.guild.get_role(role_newprogrammer)
        role_unsocial = member.guild.get_role(role_unsociable)
        channel = member.guild.get_channel(channel_count_users)
        come = member.guild.get_channel(come_out_channel)
        add_user(User(id=member.id,experience=0,money=0,level=1))
        await member.add_roles(role_new)
        await member.add_roles(role_unsocial)
        await channel.edit(name=f"Людей на сервере: {member.guild.member_count}")
        await come.send(embed=Embed(colour=Colour.green(),title=f"Зашел на сервер **{member.name}**"))
        

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        delete_user(get_user(member.id))
        channel = member.guild.get_channel(channel_count_users)
        await channel.edit(name=f"Людей на сервере: {member.guild.member_count}")
        out = member.guild.get_channel(come_out_channel)
        await out.send(embed=Embed(colour=Colour.red(),title=f"Увы... **{member.name}** ушел с сервера"))


    @commands.Cog.listener()
    async def on_message(self,message):
     #   for word in message.content.split():
      #      for banword in banwords:
       #         if fuzz.ratio(banword,word) >= 50:
        #            await message.channel.send("пизда те")
        try:
            channel = message.guild.get_channel(688373372945694725)
        except:
            pass
        
        if message.guild is not None and message.channel != channel:
            embed = Embed(title="Отправлено сообщение:",description=f"`{message.content}`",colour=Colour.dark_theme())
            print(f"{message.channel} : {message.author} : {message.content}")
            embed.add_field(name="Канал:",value=message.channel)
            embed.add_field(name="Автор:", value=message.author)
            if message.attachments == []:
                embed.add_field(name="Изображение/Видео:",value="None",inline=False)
            else:
                embed.add_field(name="Изображение/Видео:",value="_ _",inline=False)
                embed.set_image(url=message.attachments[0].url)
            

            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        channel = message.guild.get_channel(688373372945694725)
        if message.guild is not None and message.channel != channel:
            print(f"{message.channel} : {message.author} : '{message.content}'")
            await channel.send(f"{message.channel} : {message.author} : '{message.content}'")

    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        channel = before.guild.get_channel(688373372945694725)
        if before.guild is not None and before.channel != channel:
            print(f"{before.channel} : {before.author} : {before.content} -> {after.content}")
            await channel.send(f"{before.channel} : {before.author} : {before.content} -> {after.content}")

def setup(bot):
    bot.add_cog(Listener(bot))
