from discord.ext import commands
from discord import Embed, Colour
from database import *
import random
import math

class Economy(commands.Cog):
    "This is all economy in this server."
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def rank(self,ctx,*,id=None):
        "Gived you your card."
        if id is None:
            user = get_user(ctx.author.id)
            embed = Embed(title="Твоя карточка",
                    colour = Colour.purple()
                        )
        else:
            id = int(id)
            user = get_user(id)
            member = ctx.guild.get_member(id)
            embed = Embed(title=f"Карточка {member.name}",
                        colour = Colour.purple()
                        )
        embed.add_field(name="Уровень:",value=user.level)
        embed.add_field(name="Опыт:",value=user.experience)
        embed.add_field(name="Деньги:",value=user.money)
        embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot is False:
            commands = []
            this_command = False
            for command in self.bot.commands:
                commands.append("."+command.name)
            for command in commands:
                if message.content.find(command) != -1:
                    this_command = True
            if message.author.bot is False and not this_command:
                multiplier = 5
                user = get_user(message.author.id)
                if len(message.content) >= 60:
                    add_exp = user.experience + user.level*random.randint(3,8)*int(math.sqrt(user.experince))
                else:
                    add_exp = user.experience + user.level*random.randint(3,8)

                user.experience = add_exp
                if (user.experience)/(user.level*multiplier*int(math.sqrt(user.experience)*3)) >= 1:
                    await message.channel.send("New level!")
                    user.level = user.level + 1
                session.commit()
    
def setup(bot):
    bot.add_cog(Economy(bot))
