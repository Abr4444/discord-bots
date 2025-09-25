import discord, jsonOps
from discord.ext import commands
from random import randint
import requests
import random
import json

class Fun(commands.Cog):
  def __init__(self, client):
    self.client = client




def setup(client):
  client.add_cog(Fun(client))
  print("Fun Cog ready.")