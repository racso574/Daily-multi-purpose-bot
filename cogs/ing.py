from discord.ext import commands
from googletrans import Translator



class ing(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ing(self, ctx):
        tr = Translator()
        tren = tr.translate('help', dest='es')
        await ctx.send(tren.text)





def setup(client):
    client.add_cog(ing(client))



