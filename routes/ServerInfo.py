import discord
from discord.ext import commands

#Class for the ServerInfo command
class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the ServerInfo command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("ServerInfo.py is ready!")

    #Embed command defining the formatting of the embedded message
    @commands.command()
    async def serverinfo(self, ctx):

        server_embed = discord.Embed(title="Server Information")
        server_embed.set_thumbnail(url=ctx.guild.icon)
        server_embed.add_field(name = "Server Name", value = ctx.guild.name, inline=False)
        server_embed.add_field(name = "Server ID", value = ctx.guild.id, inline=False)
        server_embed.add_field(name = "Owner", value = ctx.guild.owner, inline=False)
        server_embed.add_field(name = "Member Count", value = ctx.guild.member_count, inline=False)
        server_embed.add_field(name = "Role Count", value = len(ctx.guild.roles), inline=False)
        server_embed.add_field(name = "Boosters", value = ctx.guild.premium_subscription_count, inline=False)
        server_embed.add_field(name = "Booster Level", value = ctx.guild.premium_tier, inline=False)
        server_embed.add_field(name = "NSFW Level", value = ctx.guild.explicit_content_filter.name.capitalize(), inline=False)
        server_embed.add_field(name = "MFA Level", value = ctx.guild.mfa_level, inline=False)
        server_embed.add_field(name = "Creation Date", value = ctx.guild.created_at.__format__("%A, %d. %B %Y @%H:%M:%S"), inline=False)
        server_embed.set_footer(text = f"Requested by <@{ctx.author}>.", icon_url = ctx.author.avatar)
        

        await ctx.send(embed = server_embed)

async def setup(client):
    await client.add_cog(ServerInfo(client))