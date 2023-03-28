import discord
from discord.ext import commands

#Class for the ping command
class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the Ping command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready!")

    #Ping command that multiplies the latency by 1000 and displays it
    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        await ctx.send(f"Your latency is {bot_latency} ms.")

async def setup(client):
    await client.add_cog(Ping(client))