import discord, jsonOps
from discord.ext import commands
from random import randint
import requests
import random
import json
from replit import db


class Economy(commands.Cog):
  def __init__(self, client):
    self.client = client



  @commands.command()
  @commands.cooldown(1, 900, commands.BucketType.user)
  async def mine(self, ctx):
    jsonOps.check_existence(str(ctx.author.id))

    amount = randint(10, 30)
    jsonOps.update_balances("add", ctx.author.id, amount)

    embed = discord.Embed(title="Mining successful!", description=f"You just mined {amount} $", color=0xDAA520)
    await ctx.send(embed=embed)

  @mine.error
  async def mine_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown, try again after {round(error.retry_after / 60)} minutes.", delete_after=5)

  @commands.command()
  async def balance(self, ctx):
    balance = jsonOps.check_balances(ctx.author.id)

    embed = discord.Embed(title=f"{ctx.author.name}'s Balance", description=f"{balance}$", color=0xDAA520)
    await ctx.send(embed=embed)

  @commands.command()
  async def economy(self, ctx):
    supply = jsonOps.supply()

    embed = discord.Embed(title="Total circulating Nixcoin Supply", description=f"{supply} Nixcoin", color=0xDAA520)
    await ctx.send(embed=embed)




def setup(client):
  client.add_cog(Economy(client))
  print("Economy Cog ready.")
