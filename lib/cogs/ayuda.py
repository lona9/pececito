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

    fields = [("ola", "ola ola ola", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)
    embed.set_footer(text="ola")

    await ctx.channel.send(embed=embed)

  @command(name="comandos", aliases=["comando"])
  async def comandos(self, ctx):

    self.ctx = ctx

    embed = Embed(title="Lista de comandos", colour=0x03A4DB)

    fields = [("\u200B", "!ayuda\n!comandos\n!rrss\n!playlist\n!nivel\n!puesto", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)
    embed.set_footer(text="ola")

    await ctx.channel.send(embed=embed)


  @command(name="playlist", aliases=["spotify"])
  async def playlist(self, ctx):

    self.ctx = ctx

    embed = Embed(title="Playlists", colour=0x03A4DB)
    fields = [("ola", "ola ola ola", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)
    embed.set_footer(text="ola")

    await ctx.channel.send(embed=embed)

  @command(name="redes", aliases=["rrss"])
  async def redes(self, ctx):

    self.ctx = ctx

    embed = Embed(colour=0x03A4DB)
    fields =[("Redes sociales de blvebetta", "**Tik Tok**: Tik Tok: www.tiktok.com/blvebetta\n**Instagram:** https://www.instagram.com/d.mnq", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)


    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)

    await ctx.channel.send(embed=embed)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))
