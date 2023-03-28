import discord
from discord.ext import commands

#Class for the Embed command
class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the Embed command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Embed.py is ready!")

    #Embed command defining the formatting of the embedded message
    @commands.command()
    async def embed(self, ctx):
        embed_message = discord.Embed(title = "Author", description = "This embed displays the creator of Paimon Bot", color = discord.Color.random())

        embed_message.set_author(name = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar)
        embed_message.set_thumbnail(url = ctx.guild.icon)
        embed_message.set_image(url = ctx.guild.icon)
        embed_message.add_field(name = "Commands", value = "-help - to view the list of commands \n-ping - displays the ping of the  ", inline = False)
        embed_message.set_footer(text = f"Requested by {ctx.author.name}", icon_url =ctx.author.avatar)

        await ctx.send(embed = embed_message)

async def setup(client):
    await client.add_cog(Embed(client))