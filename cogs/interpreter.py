import discord
from discord.ext import commands
from googletrans import Translator



class interpreter(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def tr(self, ctx):
        tr = Translator()
        trf = tr.translate(ctx.message.content[3:], dest='es')
        await ctx.send(ctx.message.content[3:] + ' = ' + trf.text)

    @commands.command()
    async def hts(self, ctx):
        c = str(ctx.message.content[4:].replace(ctx.message.content[6:], ''))
        tr = Translator()
        trf = tr.translate(str(ctx.message.content[6:]), dest=str(c))
        await ctx.send(ctx.message.content[6:] + ' = ' + trf.text)

    @commands.command()
    async def lg(self, ctx):
        embed = discord.Embed(title="LANGUAGES", description=f"")
        embed.add_field(name="ca", value='catalan', inline=False)
        embed.add_field(name="es", value='spanish', inline=False)
        embed.add_field(name="en", value='english', inline=False)
        embed.add_field(name="ja", value='japanese', inline=False)
        embed.add_field(name="ko", value='korean', inline=False)
        embed.add_field(name="ro", value='romanian', inline=False)
        embed.add_field(name="it", value='italian', inline=False)
        embed.add_field(name="de", value='german', inline=False)
        embed.add_field(name="fr", value='french', inline=False)
        embed.add_field(name="ru", value='russian', inline=False)
        embed.add_field(name="la", value='latin', inline=False)
        embed.add_field(name="pt", value='portuguese', inline=False)
        await ctx.send(embed=embed)





def setup(client):
    client.add_cog(interpreter(client))



