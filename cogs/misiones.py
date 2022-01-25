import discord
from discord.ext import commands
from googletrans import Translator
from openpyxl import load_workbook
import time
from random import randint, choice




class misiones(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ms(self, ctx):
        xl = load_workbook('./cogs/db/misiones.xlsx')
        edit = xl['Sheet1']

        t1 = str(edit['a1'].value)
        t2 = str(edit['a2'].value)
        t3 = str(edit['a3'].value)
        t4 = str(edit['a4'].value)
        t5 = str(edit['a4'].value)

        embed = discord.Embed(title="MISIONES", description=f"")
        embed.add_field(name='1', value=t1, inline=False)
        embed.add_field(name='2', value=t2, inline=False)
        embed.add_field(name='3', value=t3, inline=False)
        embed.add_field(name='4', value=t4, inline=False)
        embed.add_field(name='5', value=t5, inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def nms(self, ctx):
        xl = load_workbook('./cogs/db/misiones.xlsx')
        edit = xl['Sheet1']

        t1 = str(edit['a1'].value)
        t2 = str(edit['a2'].value)
        t3 = str(edit['a3'].value)
        t4 = str(edit['a4'].value)
        t5 = str(edit['a4'].value)

        if t1 == 'None':
            edit['a1'].value = ctx.message.content[4:]
            xl.save('./cogs/db/misiones.xlsx')
        elif t2 == 'None':
            edit['a2'].value = ctx.message.content[4:]
            xl.save('./cogs/db/misiones.xlsx')
        elif t3 == 'None':
            edit['a3'].value = ctx.message.content[4:]
            xl.save('./cogs/db/misiones.xlsx')
        elif t4 == 'None':
            edit['a4'].value = ctx.message.content[4:]
            xl.save('./cogs/db/misiones.xlsx')
        elif t5 == 'None':
            edit['a5'].value = ctx.message.content[4:]
            xl.save('./cogs/db/misiones.xlsx')








def setup(bot):
    bot.add_cog(misiones(bot))
