import discord
from discord.ext import commands

#Class for the Userinfo command
class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Event defining that the Userinfo command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Userinfo.py is ready!")

    #Discord bot command that gathers the information of a user
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):

    #If statement if there is
        if member is None:
            member = ctx.author
        elif member is not None:
            member = member

        #Embed that formats and gathers all that information
        info_embed = discord.Embed(title = f"{member.name}'s User Information", description = "All information about this user.", color = member.color)
        info_embed.set_thumbnail(url = member.display_avatar)
        info_embed.add_field(name = "Name:", value = member.name, inline = False)
        info_embed.add_field(name = "Nickname:", value = member.display_name, inline = False)
        info_embed.add_field(name = "Discriminator:", value = member.discriminator, inline = False)
        info_embed.add_field(name = "ID:", value = member.id, inline = False)
        info_embed.add_field(name = "Top Role:", value = member.top_role, inline = False)
        info_embed.add_field(name = "Status:", value = member.status, inline = False)
        info_embed.add_field(name = "Bot User?", value = member.bot, inline = False)
        info_embed.add_field(name = "Creation Date:", value = member.created_at.__format__("%A, %d. %B %Y @%H:%M:%S"), inline = False)
    
        await ctx.send(embed = info_embed)

async def setup(bot):
    await bot.add_cog(Userinfo(bot))