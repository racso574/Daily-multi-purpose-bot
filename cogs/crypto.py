import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands, tasks
from openpyxl import load_workbook
import urllib.request
import re
import time
from datetime import date


uid = '465475553458388994'

h1 = '0605'
h2 = '1533'
h3 = '2315'

c1 = '/bitcoin/'
c2 = '/ethereum/'
c3 = '/binance-coin/'
c4 = '/solana/'
c5 = '/cardano/'


class crypto(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def cp(self, ctx):
        webdata1 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c1)
        cdata1 = re.findall(r"<span>\$(\S{9})", webdata1.read().decode())
        webdata2 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c2)
        cdata2 = re.findall(r"<span>\$(\S{8})", webdata2.read().decode())
        webdata3 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c2)
        cdata3 = re.findall(r"<span>\$(\S{6})", webdata3.read().decode())
        webdata4 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c4)
        cdata4 = re.findall(r"<span>\$(\S{6})", webdata4.read().decode())
        webdata5 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c5)
        cdata5 = re.findall(r"<span>\$(\S{4})", webdata5.read().decode())
        embed = discord.Embed(title="", description=f"")
        embed.add_field(name='BTC', value=cdata1[0], inline=False)
        embed.add_field(name="ETH", value=cdata2[0], inline=False)
        embed.add_field(name="BNB", value=cdata3[0], inline=False)
        embed.add_field(name="SOL", value=cdata4[0], inline=False)
        embed.add_field(name="ADA", value=cdata5[0], inline=False)
        await ctx.send(embed=embed)

    @tasks.loop(seconds=60)
    async def a(self):
        webdata1 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c1)
        cdata1 = re.findall(r"<span>\$(\S{9})", webdata1.read().decode())
        webdata2 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c2)
        cdata2 = re.findall(r"<span>\$(\S{8})", webdata2.read().decode())
        webdata3 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c2)
        cdata3 = re.findall(r"<span>\$(\S{6})", webdata3.read().decode())
        webdata4 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c4)
        cdata4 = re.findall(r"<span>\$(\S{6})", webdata4.read().decode())
        webdata5 = urllib.request.urlopen('https://coinmarketcap.com/currencies' + c5)
        cdata5 = re.findall(r"<span>\$(\S{4})", webdata5.read().decode())
        embed = discord.Embed(title="Cryptocurrency Values", description=f"")
        embed.add_field(name="BTC", value=cdata1[0], inline=False)
        embed.add_field(name="ETH", value=cdata2[0], inline=False)
        embed.add_field(name="BNB", value=cdata3[0], inline=False)
        embed.add_field(name="SOL", value=cdata4[0], inline=False)
        embed.add_field(name="ADA", value=cdata5[0], inline=False)
        channel = self.client.get_channel(id=927667259495829555)
        myid = '<@' + uid + '>'
        if time.strftime("%H%M") == h1:
            await self.channel.send(myid)
            await self.channel.send(embed=embed)
        elif time.strftime("%H%M") == h2:
            await self.channel.send(myid)
            await self.channel.send(embed=embed)
        elif time.strftime("%H%M") == h3:
            await channel.send(myid)
            await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(crypto(bot))
