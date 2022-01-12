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





def setup(client):
    client.add_cog(ing(client))



