import discord, os, asyncpraw
from discord.ext import commands
import random
import sys

class Nsfw(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.clientid = os.environ['clientid']
    self.clientsec = os.environ['clientsec']
    self.redusername = os.environ['redusername']
    self.redpass = os.environ['redpass']
    self.reduseragent = os.environ['reduseragent']
    self.reddit = asyncpraw.Reddit(client_id = self.clientid, client_secret = self.clientsec, username = self.redusername, password = self.redpass, user_agent = self.reduseragent)



  @commands.command()
  async def porn(self, ctx): 
      subreddit = ["porn", "boobs", "ass", "tits", "blowjob", "nsfw", "nsfw2", "nudes","boobies", "tittydrop", "slut", "BigBoobsGW", "homemadexxx", "deepthroat", "onherknees", "bigasses", "asstastic", "booty"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)          
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)
  
  @commands.command()
  async def gayporn(self, ctx): 
      subreddit = ["gayporn", "penis", "gaybrosgonewild", "femboys", "bisexy", "LadyBonersGW", "MassiveCock", "GayGifs", "Twinks", "monsterdicks", "thickdicks", "sissies"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)     
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)
  
  @commands.command()
  async def femdom(self, ctx):
      subreddit = ["femdom", "ruinedorgasms", "postorgasm", "femdom_gifs", "femdomgonewild"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)     
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  async def hentai(self, ctx): 
      subreddit = ["hentai", "hentai gifs", "WesternHentai", "hentai irl", "hentaibondage", "ecchi", "doujinshi", "r34", "rule34"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)     
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)
  

  @commands.command()
  async def boobs(self, ctx):
      subreddit = ["boobs","tits","boobies","tittydrop","boltedontits","boobbounce","downblouse","homegrowntits", "cleavage", "breastenvy", "youtubetitties", "torpedotits", "thehangingboobs", "page3galmour", "fortyfivefiftyfive", "tits", "amazingtits", "titstouchingtits"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)          
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)
  

  @commands.command()
  async def ass(self, ctx): 
      subreddit = ["ass", "asstastic", "facedownassup", "assinthong", "bigasses", "buttplug", "theunderbun", "booty", "cutelittlebutts", "hipcleavage", "frogbutt", "Hungrybutts", "cottontails", "lovetowatchyouleave", "celebritybutts", "cosplaybutts", "whooties", "booty_queens", "twerking"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)          
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  async def anal(self, ctx): 
      subreddit = ["anal", "analgw", "painal", "masterofanal", "buttsharpies"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)          
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  async def titfuck(self, ctx): 
      await ctx.message.delete()
      subreddit = ["titfuck", "clothedtitfuck"]
      subreddit = await self.reddit.subreddit(random.choice(subreddit))
      all_subs = []
      top = subreddit.top(limit=150)
      async for submission in top:
          all_subs.append(submission)
      random_sub = random.choice(all_subs)          
      name = random_sub.title
      url = random_sub.url
      randcolor = random.randint(0x000000, 0xFFFFFF) 
      embed = discord.Embed(title=name,color=randcolor)
      embed.set_image(url=url)
      await ctx.send(embed=embed)






def setup(client):
  client.add_cog(Nsfw(client))
  print("Nsfw Cog ready.")