import discord
from discord.ext import commands
import os



class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=0x050505, description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)
      
class Client(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix='!', intents=discord.Intents.all())

client=Client()  


for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    client.load_extension(f"cogs.{file[:-3]}")


client.help_command = MyHelpCommand()
client.run(os.getenv("TOKEN")) 