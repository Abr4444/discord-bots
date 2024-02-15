import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Welcome(Cog):

	def __init__(self, client):
		self.client = client
	
	@Cog.listener()
	async def on_member_join(self, member):
		channel = discord.utils.get(member.guild.text_channels, id=957017441953792072)
		await channel.send(
			embed = discord.Embed(
				description=f"""{member.name}, Welcome to GreyHound Race NFT, enjoy your stay here!
You are our {member.number}member """,
				color=0xffffff
			)
		)

def setup(client):
	client.add_cog(Welcome(client))