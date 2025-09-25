import discord
import requests
from discord.ext import commands
import random


class Others(commands.Cog):
  def __init__(self, client):
    self.client = client
    



  #@commands.command()
  #async def boost(self, ctx):
  #  embed= discord.Embed(color= 0xE6C7C2, description= "<a:nitro:752151971955474482> **__NITRO BOOSTER REWARDS__** <a:nitro:752151971955474482>_Boosting MaxyLab server will get you _ :\n→ Server Booster NFT Card (https://wax.atomichub.io/explorer/template/maxylabchain/175550)\n→ Server Booster Role)"
   # await ctx.send(embed=embed)


 


def setup(client):
  client.add_cog(Others(client))
  print("Others Cog ready.")