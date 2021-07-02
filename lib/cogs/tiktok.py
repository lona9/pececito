from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Tiktok(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command()
  async def tiktok(self, ctx, link, *args):
    title = str(" ".join(args))

    self.ctx = ctx
    embed = Embed(title=f"{title}",colour=0x03A4DB)

    fields = [(f"link:", f"{link}", False)]

    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='pececito', icon_url=self.ctx.guild.icon_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/855531786746069002/856657283626172446/IMG-0143_1.PNG")

    await ctx.channel.send(embed=embed)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("tiktok")

def setup(bot):
  bot.add_cog(Tiktok(bot))
