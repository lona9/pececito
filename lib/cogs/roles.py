from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.utils import get
from discord import Embed

class Roles(Cog):
  def __init__(self, bot):
    self.bot = bot

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("roles")

  @command(name="pais")
  async def pais(self, ctx):
    paises = await ctx.channel.send("Para agregarte un rol de acuerdo a tu nacionalidad/país de residencia, haz click en la bandera del país que corresponda.")
    banderas = ["🇦🇷", "🇧🇴", "🇧🇷", "🇨🇱", "🇨🇴", "🇪🇨", "🇺🇸", "🇲🇽", "🇵🇾", "🇵🇪", "🇻🇪", "🇫🇷"]
    for i in banderas:
      await paises.add_reaction(i)

  @command()
  async def notifs(self, ctx):
    await ctx.message.delete()
    notifs = await ctx.channel.send("Para agregarte el rol de <@&856666465145978890>, reacciona con la campanita abajo.")
    await notifs.add_reaction('🛎️')

  @Cog.listener()
  async def on_raw_reaction_add(self, payload):
    user = payload.member

    if user == self.bot:
      return

    campanita = get(user.guild.roles, name="notificaciones")
    argentina = get(user.guild.roles, name="argentina")
    bolivia = get(user.guild.roles, name="bolivia")
    brasil = get(user.guild.roles, name="brasil")
    chile = get(user.guild.roles, name="chile")
    colombia = get(user.guild.roles, name="colombia")
    ecuador = get(user.guild.roles, name="ecuador")
    estados_unidos = get(user.guild.roles, name="estados unidos")
    mexico = get(user.guild.roles, name="méxico")
    paraguay = get(user.guild.roles, name="paraguay")
    peru = get(user.guild.roles, name="perú")
    venezuela = get(user.guild.roles, name="venezuela")
    spain = get(user.guild.roles, name="españa")
    francia = get(user.guild.roles, name="francia")

    if payload.channel_id == 857388217946210314:
      if payload.emoji.name =='🛎️':
        await user.add_roles(campanita)
      elif payload.emoji.name == '🇦🇷':
        await user.add_roles(argentina)
      elif payload.emoji.name == '🇧🇴':
        await user.add_roles(bolivia)
      elif payload.emoji.name == '🇧🇷':
        await user.add_roles(brasil)
      elif payload.emoji.name == '🇨🇱':
        await user.add_roles(chile)
      elif payload.emoji.name == '🇨🇴':
        await user.add_roles(colombia)
      elif payload.emoji.name == '🇪🇨':
        await user.add_roles(ecuador)
      elif payload.emoji.name == '🇺🇸':
        await user.add_roles(estados_unidos)
      elif payload.emoji.name == '🇲🇽':
        await user.add_roles(mexico)
      elif payload.emoji.name == '🇵🇾':
        await user.add_roles(paraguay)
      elif payload.emoji.name == '🇵🇪':
        await user.add_roles(peru)
      elif payload.emoji.name == '🇻🇪':
        await user.add_roles(venezuela)
      elif payload.emoji.name == '🇪🇸':
        await user.add_roles(spain)
      elif payload.emoji.name == '🇫🇷':
        await user.add_roles(francia)

def setup(bot):
  bot.add_cog(Roles(bot))
