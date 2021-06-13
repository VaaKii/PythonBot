from discord.ext import commands
from discord import PermissionOverwrite
from database import Private,get_private,add_private,session

class Privates(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        if after.channel != None:
            channelQ = get_private(after.channel.id)
        else:
            channelQ = get_private(before.channel.id)
        if channelQ != None:
            channels = session.query(Private).all()
            if after.channel == None:
                channelQ.count_members = 0
            else:
                channelQ.count_members = len(after.channel.members)
            for channel in channels:
                channeld = member.guild.get_channel(channel.channel_id)
                if channeld.members == []:
                    await channeld.delete()
                    session.delete(channel)
            session.commit()
        else:
            if after.channel.id == 649676227329654834:
                channel = await member.guild.create_voice_channel(member.name,category=after.channel.category)
                add_private(Private(channel_id=channel.id,count_members=1))
                await member.move_to(channel)
                overwrite = PermissionOverwrite()
                overwrite.manage_channels = True
                await channel.set_permissions(member,overwrite=overwrite)
def setup(bot):
    bot.add_cog(Privates(bot))