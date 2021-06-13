from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self,bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.guild is not None:
            role_there_is = False
            roles = {".js":622102319026274314,".python":622101981032349697,".kotlin":699601139116802049,".html":622103727557443606,".java":622103732607254538,".cpp":622102338294775858,".c++":622102338294775858,".css":622103728484253746,".csharp":622103730690588693,".c#":622103730690588693,".cs":622103730690588693,".c":622103731848216596,".rust":707318536674082824,".ржавчина":707318536674082824,".ruby":622336566320431134,".php":622103729126244363,".lua":622103730120032257,".pascal":622336566085550081,".говно":622336566085550081}
            for role in message.author.roles:
                try:
                    if role.id == roles[f'{message.content.lower()}']:
                        role_there_is = True
                except:
                    pass
            if message.content.lower() in roles:
                print(role_there_is)
                if role_there_is is True:
                    role = message.guild.get_role(roles[f'{message.content.lower()}'])
                    await message.author.remove_roles(role)
                    await message.channel.send(f"Роль {role} убрана.")
                else:
                    role = message.guild.get_role(roles[f'{message.content.lower()}'])
                    await message.author.add_roles(role)
                    await message.channel.send(f"Роль {role} выдана.")

def setup(bot):
    bot.add_cog(Roles(bot))