import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands, tasks
from openpyxl import load_workbook
import urllib.request
import re
import time
from datetime import date


class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.te.start()

    @tasks.loop(seconds=3)
    async def te(self):
        channel = self.bot.get_channel(927667259495829555)
        await channel.send('test')


def setup(bot):
    bot.add_cog(test(bot))