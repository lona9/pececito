from discord import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command
import pendulum
import datetime
from datetime import datetime
from discord.utils import get

class Log(Cog):
  def __init__(self, bot):
    self.bot = bot

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.log_channel = self.bot.get_channel(862379511227482128)
      self.bot.cogs_ready.ready_up("log")
      self.guild = self.bot.get_guild(855476704978010132)

  @Cog.listener()
  async def on_member_update(self, before, after):

      tz_CL = pendulum.timezone('America/Santiago')
      time_now = datetime.now(tz_CL)

      if before.display_name != after.display_name:
        embed = Embed(title="Member update", description="Nickname change", timestamp=time_now)

        fields = [("Before", before.display_name, False),
                  ("After", after.display_name, False),
                  ("Member ID", after.id, False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='pececito', icon_url=after.guild.icon_url)

        await self.log_channel.send(embed=embed)

      if before.roles != after.roles:
        embed = Embed(title="Member update", description= f"Role change: user **{after.display_name}#{after.discriminator}**", timestamp=time_now)

        fields = [("Before", ", ".join([r.mention for r in before.roles]), False),
                ("After", ", ".join([r.mention for r in after.roles]), False),
                ("Member ID", after.id, False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name='pececito', icon_url=after.guild.icon_url)

        await self.log_channel.send(embed=embed)

  @Cog.listener()
  async def on_member_remove(self, member):

      tz_CL = pendulum.timezone('America/Santiago')
      time_now = datetime.now(tz_CL)

      embed = Embed(title="Member remove", timestamp=time_now)

      fields = [("This member left the server", f"{member}", False),
                ("Member ID", member.id, False)]

      for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

      embed.set_author(name='pececito', icon_url=self.guild.icon_url)

      await self.log_channel.send(embed=embed)

  @Cog.listener()
  async def on_member_join(self, member):

      tz_CL = pendulum.timezone('America/Santiago')
      time_now = datetime.now(tz_CL)

      embed = Embed(title="Member join", timestamp=time_now)

      fields = [("This member joined the server", f"{member}", False),
                ("Member ID", member.id, False)]

      for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

      embed.set_author(name='pececito', icon_url=self.guild.icon_url)

      await self.log_channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Log(bot))
