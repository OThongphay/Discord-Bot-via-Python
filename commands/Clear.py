import discord
from discord.ext import commands

#Class for the Clear command
class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the Clear command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear.py is ready!")

    #Clear command elimintaing a specified integer amount of messages
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit = count)
        await ctx.send(f"{count} messages have been deleted")

async def setup(client):
    await client.add_cog(Clear(client))