from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from discord.utils import get

class Bienvenida(Cog):
  def __init__(self, bot):
    self.bot = bot

  @Cog.listener()
  async def on_member_join(self, member):
    self.bienvenida = self.bot.get_channel(859506827070930945)

    await self.bienvenida.send(f"Hola {member.mention}!! Gracias por unirte a **La Pecera**, recuerda leer las <#862069303141466144> y pasar por <#857388217946210314> para asignarte roles <:emoji_24:857037609304719370>")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("bienvenida")

def setup(bot):
  bot.add_cog(Bienvenida(bot))
