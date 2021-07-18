import discord
import os
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Ayuda(Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bot.remove_command("help")

  @command(name="ayuda", aliases=["info", "help"])
  async def ayuda(self, ctx):

    self.ctx = ctx

    embed = Embed(colour=0x03A4DB)

    fields = [("¡Hola!", "Soy el bot de **La Pecera** y estoy aquí para ayudarte.", False),
                ("Escribe los siguientes comandos para pedir más información:", "**!ayuda**: estás aquí!\n**!comandos**: lista de comandos disponbiles\n**!canales**: lista de los canales y sus descripciones", False),
                ("Algunos datos útiles:", ":fish: Puedes encontrar las reglas en el canal <#862069303141466144>\n:fish: Puedes agregarte distintos roles en el canal <#857388217946210314>\n:fish: Este bot tiene incorporado un sistema de experiencia que te dará **maricooins** cada vez que envíes un mensaje (cooldown de 20 segundos).", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)

    await ctx.channel.send(embed=embed)

  @command(name="comandos", aliases=["comando"])
  async def comandos(self, ctx):

    self.ctx = ctx

    embed = Embed(colour=0x03A4DB)

    fields = [("Lista de comandos:", "**!canales**: resumen de los canales del servidor\n**!rrss**: redes sociales de **blvebetta**\n**!playlist**: link a playlists de spotify de **blvebetta**.\n**!nivel**: revisa tu nivel o el de otra persona\n**!puesto**: revisa tu puesto o el de otra persona\n**!ranking**: revisa el ranking del servidor\n**!reglas**: revisa las reglas del servidor\n**!invitacion**: envía una invitación al servidor por DM que caduca en 24 horas.", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)

    await ctx.channel.send(embed=embed)

  @command(name="canales", aliases=["channels"])
  async def canales(self, ctx):

    self.ctx = ctx

    embed = Embed(colour=0x03A4DB)

    fields = [("Lista de canales", "WIP", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)

    await ctx.channel.send(embed=embed)


  @command(name="playlist", aliases=["spotify"])
  async def playlist(self, ctx):

    self.ctx = ctx

    embed = Embed(title="Playlists", colour=0x03A4DB)
    fields = [("Escribe el nombre (o primera palabra) de una playlist de la lista:", "kperreo\nmenphobic\nokay maybe some of them deserve rights\nfull kpopera", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)

    await ctx.channel.send(embed=embed)

    message = await self.bot.wait_for('message', timeout=20, check=lambda message: message.author == ctx.author)

    if message.content.lower() == "kperreo":
        await ctx.send("Acá está el link para playlist **kperreo**: https://open.spotify.com/playlist/6UQMXDbhSM8T6Vdrsuuv73?si=OodCoSuXR_GYhIcEBT81VQ&dl_branch=1&nd=1")

    elif message.content.lower() == "menphobic":
        await ctx.send("Acá está el link para playlist **menphobic**: https://open.spotify.com/playlist/39f71XBB9TlGaQfQP3ji9g?si=a01MLA1cSOCh6UoqVEGFsQ&dl_branch=1&nd=1")

    elif message.content.lower() == "okay" or message.content.lower() == "okay maybe some of them deserve rights":
        await ctx.send("Acá está el link para playlist **okay maybe some of them deserve rights**: https://open.spotify.com/playlist/4SN1XFRFuDojZY6GPlFeF0?si=44QBYgYgThCOw3-ANitwyA&dl_branch=1&nd=1")

    elif message.content.lower() == "full" or message.content.lower() == "full kpopera":
        await ctx.send("Acá está el link para playlist **full kpopera**: https://open.spotify.com/playlist/1ZrjkV51qHaBhgV7ZBzTJi?si=KPer8M7WSouzXU0lguYlXw&dl_branch=1&nd=1")

    else:
        await ctx.send("Debes ingresar una opción válida!")

  @command(name="redes", aliases=["rrss"])
  async def redes(self, ctx):

    self.ctx = ctx

    embed = Embed(colour=0x03A4DB)
    fields =[("Redes sociales de blvebetta", "**Tik Tok**: Tik Tok: www.tiktok.com/blvebetta\n**Instagram:** https://www.instagram.com/d.mnq", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)

    await ctx.channel.send(embed=embed)

  @command(name="reglas", aliases=["regla", "rules"])
  async def reglas(self, ctx):

    self.ctx = ctx

    embed = Embed(colour=0x03A4DB)
    fields =[("Reglas", ":no_entry_sign: Spamear contenido publicitario (twitch, youtube, tiktok, etc).\n:no_entry_sign: Cualquier tipo de comentario que se considere como racismo, homofobia, xenofobia, etc.\n:no_entry_sign: Todo tipo de insinuaciones o contenido de carácter sexual.\n:no_entry_sign: Ser menor de 16 años.\n:no_entry_sign: Fotos de perfil inadecuadas.\n:no_entry_sign: Acoso de cualquier tipo, bullying, amenazas, difundir información personal.\n:no_entry_sign: Salir y entrar del server para evadir mutes.\n\n:firecracker: Considerar que @domi tiene una vida aparte de este server. Respetar sus tiempos y espacios privados, no spamear con pings ni mandar mensajes directos para que responda. :firecracker:", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)

    await ctx.channel.send(embed=embed)

  @command(name="eco", aliases=["echo"])
  async def eco(self, ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

  @command(name='invitacion', aliases=["invite"])
  async def invitacion(self, ctx, *argument):

    invitelink = await ctx.channel.create_invite(max_age=86400,unique=True)

    await ctx.author.send('¡Aquí está el link de invitación al servidor que pediste! Debes usarlo en las siguientes 24 horas antes de que expire. ')
    await ctx.author.send(invitelink)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))
