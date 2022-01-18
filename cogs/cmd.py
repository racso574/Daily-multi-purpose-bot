import discord
from discord.ext import commands

class cmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="PAN COMMANDS", description=f"Here is the list of PAN commands:")
        embed.add_field(name="FAV", value='Random video from a list of the best Pan piano videos', inline=False)
        embed.add_field(name="PIANO", value='Random video of the Pan piano channel', inline=False)
        embed.add_field(name="NEW", value='Spam the new Pan piano video', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def clear(self, ctx):
        if ctx.message.content == 'clear':
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=int(ctx.message.content[6]) + 1)




def setup(bot):
    bot.add_cog(cmd(bot))
