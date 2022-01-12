import os
import discord
from dotenv import load_dotenv
from discord.ext import commands




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

client = commands.Bot(command_prefix='')


@client.event
async def on_ready():
    print(f'{client.user} uwu')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)