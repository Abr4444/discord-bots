import discord
from discord.ext import commands
from discord.ext.commands import Cog


class Moderation(Cog):

  def __init__(self, client):
    self.client = client

  @commands.command() 
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason="None"):
    await member.kick(reason=reason)
    embed=discord.Embed(title='Sucess', description= f'{member.name} has been kicked\nReason: {reason}', color=0x050505)
    await ctx.send(embed=embed)

  @commands.command() 
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason="None"):
    await member.ban(reason=reason)
    embed=discord.Embed(title='Sucess', description= f'{member.name} has been banned\nReason: {reason}', color =0x050505)
    await ctx.send(embed=embed)

  @commands.command()
  async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
    
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f"{user} have been unbanned sucessfully")
      return
  
def setup(client):
  client.add_cog(Moderation(client))