from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
import pendulum
import datetime
from datetime import datetime

class Live(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command()
  async def live(self, ctx):
    await ctx.message.delete()
    self.ctx = ctx
    embed = Embed(title="**blvebetta** está en vivo!", colour=0x03A4DB)

    fields = [("En vivo", "https://www.twitch.tv/blvebetta", False)]

    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

    tz = pendulum.timezone('America/La_Paz')
    datetime_cl = datetime.now(tz)
    timestamp = datetime_cl.strftime("%H:%M")

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/855531786746069002/856657283626172446/IMG-0143_1.PNG")
    embed.set_footer(text=timestamp)

    await ctx.channel.send(embed=embed)

    guild = ctx.message.guild
    for role in guild.roles:
      if role.name == "notifs":
        role_id = role
        break

    for member in guild.members:
      if role_id in member.roles:
          try:
              await member.send(embed=embed)
          except Forbidden:
              pass

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("live")

def setup(bot):
  bot.add_cog(Live(bot))
