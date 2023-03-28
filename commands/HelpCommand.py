import discord
from discord.ext import commands

#Class for the HelpCommand command
class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the Help command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpCommand.py is ready!")

    #Help embed is defined, with all commands that can be used on this bot
    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(title = "Help Desk for Paimon Bot", description = "All commands for the bot.", color = discord.Color.random())

        help_embed.set_author(name = "Paimon Bot")
        help_embed.add_field(name = "Clear", value = "Deletes a specified amount of messages from the chat the command was activated in", inline = False)
        help_embed.add_field(name = "Embed", value = "Creates an Embeded Message containing info regarding the author of this bot", inline = False)
        help_embed.add_field(name = "Help", value = "Displays embedded message about useful commands", inline = False)
        help_embed.add_field(name = "Ping", value = "Display the network metric of the bot", inline = False)
        help_embed.add_field(name = "Setprefix", value = "Changes the prefix for the bot to execute commands", inline = False)
        help_embed.add_field(name = "Userinfo", value = "Display the information regarding a specified user", inline = False)
        help_embed.set_footer(text = f"Requested by <@{ctx.author}>.", icon_url = ctx.author.avatar)

        await ctx.send(embed = help_embed)

async def setup(client):
    await client.add_cog(HelpCommand(client))