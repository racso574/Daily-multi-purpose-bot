import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='', case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user} uwu')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)