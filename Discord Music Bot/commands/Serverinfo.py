import discord
from discord.ext import commands
from discord import Embed

#Class for the Serverinfo command
class Serverinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the Serverinfo command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Serverinfo.py is ready!")

    #Serverinfo command that multiplies the latency by 1000 and displays it
    @commands.command()
    async def serverinfo(self, ctx, guild: discord.Guild = None):

        #Defines guild as the one specified from the author
        guild = ctx.author.guild

        #Formatting of the embed for serverinfo
        server_embed = discord.Embed(title = f"Server Information for {guild.name}", description = "All information about this server", color =discord.Color.random())
        server_embed.set_thumbnail(url = guild.icon)
        server_embed.add_field(name = "Server Name:", value = guild.name, inline = False)
        server_embed.add_field(name = "Server ID:", value = guild.id, inline = False)
        server_embed.add_field(name = "Server Owner:", value = guild.owner, inline = False)
        server_embed.add_field(name = "Total Members:", value = guild.member_count, inline = False)
        server_embed.add_field(name = "AFK Channel?", value = guild.afk_channel, inline = False)
        server_embed.add_field(name = "Server Created:", value = guild.created_at.__format__("%A, %d. %B %Y @%H:%M:%S"), inline = False)
        server_embed.set_footer(text = f"Requested by <@{ctx.author}>.", icon_url = ctx.author.avatar)
        
        await ctx.send(embed = server_embed)

        

async def setup(client):
    await client.add_cog(Serverinfo(client))