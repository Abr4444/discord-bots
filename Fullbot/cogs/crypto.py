import discord, jsonOps, json
from discord.ext import commands
from random import randint
import requests
import random
from replit import db


class Crypto(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["btc","btcusd","usdbtc"])
  async def bitcoin(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=1").json()
      j = ['open']
      dolor = j['open']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Bitcoin command", description=f"Bitcoin value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["eth","ethusd","usdeth"])
  async def ethereum(self, ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Etherum command", description=f"Etherum value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["bnb","bnbusd","usdbnb"])
  async def binance(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Binance command", description=f"Binance value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["axs","axsusd","usdaxs"])
  async def axie(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=AXS&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Axie command", description=f"Axie value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["xrpusd","usdxrp"])
  async def xrp(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - XRP command", description=f"XRP value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command()
  async def busd(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BUSD&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Busd command", description=f"Busd value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["doge","dogeusd","usddoge"])
  async def dogecoin(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Doge command", description=f"Doge value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["ltc","ltceusd","usdltc"])
  async def litecoin(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Litecoin command", description=f"Litecoin value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["yfi","yfieusd","usdyfi"])
  async def yearn(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=YFI&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Yearn command", description=f"Yearn value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["trx","trxusd","usdtrx"])
  async def tron(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=TRX&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Trx command", description=f"Trx value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)
  @commands.command(aliases=["bsw","bswusd","usdbsw"])
  async def biswap(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BSW&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Biswap command", description=f"Bsw value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["monsta","moniusd","usdmoni"])
  async def moni(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=MONI&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Moni command", description=f"Moni value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["sol","solusd","usdsol"])
  async def solana(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Solana command", description=f"Solana value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)

  @commands.command(aliases=["bch","bchusd","usdbch"])
  async def bitcoincash(self,ctx):
      data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=USD").text
      j = json.loads(data)
      dolor = j['USD']
      randcolor = random.randint(0x000000, 0xFFFFFF)
      embed=discord.Embed(title="Nixbot - Bitcoincash command", description=f"Bch value : `${dolor}`", color=randcolor)

      embed.set_footer(text="Nixcorp ™ ")
      await ctx.send(embed=embed)




def setup(client):
  client.add_cog(Crypto(client))
  print("Crypto Cog ready.")