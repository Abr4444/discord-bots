from webserver import keep_alive
import os
import json
import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = commands.Botclient = commands.Bot(command_prefix="!", intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print("Running")
    activity = discord.Game(name="with your money")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command(aliases=['balance'])
async def bal(ctx):
    user = ctx.author
    await open_account(ctx.author)
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    embed = discord.Embed(title=":moneybag: Your wallet", description=f'Your balance is {wallet_amt}', color=0x8792fd)
    await ctx.send(embed=embed)
    
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def give(ctx, user: discord.Member, amount):
        await open_account(user)
        users = await get_bank_data()
        users[str(user.id)]["wallet"] += amount
        await ctx.send('Success')
        with open ("mainbank.json", "w") as f:
            json.dump(users,f)
    

@client.command()
async def open_account(user):
    with open ("mainbank.json", "r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def beg(ctx):
    user = ctx.author

    await open_account(ctx.author)

    users = await get_bank_data()

    earnings = random.randrange(101)
    embed = discord.Embed(description=f'Some person just gave you {earnings} pls dont gamble them lol', color=0x8792fd)
    await ctx.send(embed=embed)
     
    users[str(user.id)]["wallet"] += earnings

    with open ("mainbank.json", "w") as f:
        json.dump(users,f)
        

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def get(ctx):
    user = ctx.author

    await open_account(ctx.author)

    users = await get_bank_data()

    earnings = random.randrange(10000000)
    embed = discord.Embed(description=f'Some person just gave you {earnings} pls dont gamble them lol', color=0x8792fd)
    await ctx.send(embed=embed)
     
    users[str(user.id)]["wallet"] += earnings

    with open ("mainbank.json", "w") as f:
        json.dump(users,f)

@client.command()
async def coinflip(ctx, amnt = None, side = None):
    user = ctx.author
    if not amnt : await ctx.send("Invalid command. Usage: `!coinflip <amount> <coinside>`")
    try:
        accept = int(amnt)
    except ValueError:
        await ctx.send("That didn't work out... have you entered a number?")
    await open_account(ctx.author)

    users = await get_bank_data()

    if not side:
        await ctx.send("Invalid command. Usage: `!coinflip <amount> <coinside>`")
    elif not amnt:
        await ctx.send("Invalid command. Usage: `!coinflip <amount> <coinside>`")
    else:
        if side in ("heads", "tails"):
            if users[str(user.id)]["wallet"] < accept:
                await ctx.send("You can't bet more money than you have")
            else:
                num1 = random.choice(["heads", "tails"])
                if num1 != side:
                    users[str(user.id)]["wallet"] -= accept
                    embed = discord.Embed(title=':red_circle: LOSS', description=f'You got **{num1}** and lost {accept} coins', color=0xfd0000)
                    await ctx.send(embed=embed)
                elif num1 == side:
                    users[str(user.id)]["wallet"] += accept
                    embed = discord.Embed(title=':green_circle: WIN', description=f'You got **{num1}** and won {accept} coins', color=0x00ff0a)
                    await ctx.send(embed=embed)
        else:
            await ctx.send("Wrong coin side! It can only be `heads` or `tails`")
        with open ("mainbank.json", "w") as f:
            json.dump(users,f)

@client.command()
async def roll(ctx, amnt = None):
    user = ctx.author
    if not amnt : await ctx.send("Invalid command. Usage: `!roll <amount>`")
    return
    try:
        accept = int(amnt)
    except ValueError:
        await ctx.send("That didn't work out... have you entered a number?")
    await open_account(ctx.author)

    users = await get_bank_data()

    if not amnt :
        await ctx.send("Invalid command. Usage: `!roll <amount>`")
    else:
        if users[str(user.id)]["wallet"] < accept:
            await ctx.send("You can't bet more money than you have")
        else:
            num1 = random.randint(1,12)
            num2 = random.randint(1,12)
            if num1 > num2:
                users[str(user.id)]["wallet"] += accept
                embed = discord.Embed(title=':green_circle: WIN', color=0x00ff0a)
                embed.add_field(name='You', value=f'Rolled `{num1}`')
                embed.add_field(name='Wager', value=f'Rolled `{num2}`')
                await ctx.send(embed=embed)
            elif num1 < num2:
                users[str(user.id)]["wallet"] -= accept
                embed = discord.Embed(title=':red_circle: LOSS', color=0xfd0000)
                embed.add_field(name='You', value=f'Rolled `{num1}`')
                embed.add_field(name='Wager', value=f'Rolled `{num2}`')
                await ctx.send(embed=embed)
            elif num1 == num2:
                embed = discord.Embed(title='Tie', color=0xf1ff00)
                embed.add_field(name='You', value=f'Rolled `{num1}`')
                embed.add_field(name='Wager', value=f'Rolled `{num2}`')
                await ctx.send(embed=embed)

    with open ("mainbank.json", "w") as f:
        json.dump(users,f)

@client.command()
async def help(ctx):
    embed = discord.Embed(title=':scroll: Commands', color=0x8792fd)
    embed.add_field(name='Open', value='Open a bank account Usage: `!open`')
    embed.add_field(name='Coinflip', value='Flip that coin and see if you won. Usage: `!coinflip <amount of cash> <coin side>`')
    embed.add_field(name='Roll', value='Diceroll with me. IM THE GAMBLING GOD! Usage: `!roll <amount of cash>`')
    embed.add_field(name='Spin', value='Spin the wheel and check if today is your lucky day. Usage: `!spin <color> <number>`')
    embed.add_field(name='Beg', value='Beg for money if you dont have a lot, and if you have it doesnt matter its FREE. Usage: `!beg`')
    embed.add_field(name='Bal', value='Check how much money you have. Usage: `!bal`') 
    embed.add_field(name='Admin: get', value='Get a really big amount of money, admin only. Usage: `!get`') 
    embed.add_field(name='Admin: clear', value='Reset your or the bal of someone, admin only. Usage: `!clear`') 
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx):
        os.remove("mainbank.json")
        f = open("mainbank.json", "a+")
        f.write("{\n\n}")
        await ctx.send("Done")
  

@client.command()
async def botowner(ctx):
    embed = discord.Embed(title='my owner is !         Abr#4444', color=0x8792fd)
    await ctx.send(embed=embed)
    
@client.command()
async def spin(ctx, amnt = None, color = None):
    user = ctx.author
    if not amnt : await ctx.send("Invalid command. Usage: `!spin <amount> <color> <number>`")
    try:
        accept = int(amnt)
    except ValueError:
        await ctx.send("That didn't work out... have you entered a number?")
    await open_account(ctx.author)

    users = await get_bank_data()

    if not color:
        await ctx.send("Invalid command. Usage: `!spin <amount> <color> <number>`")

    else:
        if color in ("red1", "red3", "red5", "red7", "red9", "red12", "red14", "red16", "red18", "red19","red21", "red23", "red25", "red7", "red30", "red32", "red34", "red36", "black2", "black4", "black6", ":black_circle: 8", ":black_circle: 10",  ":black_circle: 11",  ":black_circle: 13",  "black15",  "black17",  "black20",  "black22",  "black24",  "black26",  "black29",  "black 31",  "black33",  "black35"):
            if users[str(user.id)]["wallet"] < accept:
                await ctx.send("You can't bet more money than you have")
            else:
                num1 = random.choice(["red1", "red3", "red5", "red7", "red9", "red12", "red14", "red16", "red18", "red19","red21", "red23", "red25", "red7", "red30", "red32", "red34", "red36", "black2", "black4", "black6", ":black_circle: 8", ":black_circle: 10",  ":black_circle: 11",  ":black_circle: 13",  "black15",  "black17",  "black20",  "black22",  "black24",  "black26",  "black29",  "black 31",  "black33",  "black35"])
                if num1 != color:
                    users[str(user.id)]["wallet"] -= accept
                    embed = discord.Embed(title=':red_circle: LOSS', description=f'You got **{num1}** and lost {accept} coins', color=0xfd0000)
                    await ctx.send(embed=embed)
                elif num1 == color:
                    users[str(user.id)]["wallet"] += accept
                    embed = discord.Embed(title=':green_circle: WIN', description=f'You got **{num1}** and won {accept} coins', color=0x00ff0a)
                    await ctx.send(embed=embed)
        else:
            await ctx.send("Wrong color! It can only be `black&number` or `red&number`")
        with open ("mainbank.json", "w") as f:
            json.dump(users,f)
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run("")

