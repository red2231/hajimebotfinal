from discord.ext.commands import Context as context
from discord.ext.commands.cog import Cog
from discord.ext.commands.bot import Bot
import discord.ext.commands as p

class Player(Cog):
 def __init__(self, but:Bot):
     self.bot = but
 @p.slash_command(description="Novo por aqui? Use este comando para começar no RPG!")
 async def iniciar(self, ctx:context):
     await ctx.send("testando")


p = 't'