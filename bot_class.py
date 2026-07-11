import discord
import random
import os
import requests
from discord.ext import commands

from Bot_logic import gen_emodji, gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def halo(ctx):
    await ctx.send(f'Hi!')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def password(ctx):
    password = gen_pass(10)
    await ctx.send("Your password: " + password)

@bot.command()
async def emodji(ctx):
    emodji = gen_emodji()
    await ctx.send(emodji)
    
@bot.command()
async def flip(ctx):
    flip = random.randint(0, 1)
    if flip == 0:
        await ctx.send("HEADS")
    else:
        await ctx.send("TAILS")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def daftar_perintah(ctx):
    """Displays a list of available commands."""
    commands_list = [
        "$halo - Greets the user.",
        "$bye - Sends a smiley face.",
        "$add <num1> <num2> - Adds two numbers together.",
        "$repeat <times> <message> - Repeats a message multiple times.",
        "$password - Generates a random password.",
        "$emodji - Sends a random emoji.",
        "$flip - Flips a coin and returns heads or tails.",
        "$joined <member> - Displays when a member joined the server.",
        "$mem - Sends a meme image.",
        "$dog - Sends a random dog image."
    ]
    help_message = "\n".join(commands_list)
    await ctx.send(f"Available commands:\n{help_message}")

@bot.command()
async def mem(ctx):
    image_path = os.listdir('KODLAND/images')
    image_file = random.choice(image_path)
    with open(f'KODLAND/images/{image_file}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

def get_dog_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def dog(ctx):
    '''Setelah kita memanggil perintah anjing (dog), program akan memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command()
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run("token")
