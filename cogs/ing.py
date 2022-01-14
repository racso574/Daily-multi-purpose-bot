from discord.ext import commands
from googletrans import Translator



class ing(commands.Cog):

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







def setup(client):
    client.add_cog(ing(client))



