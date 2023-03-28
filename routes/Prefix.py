import discord
from discord.ext import commands
import json

class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the Clear command is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Prefix.py is ready!")

    #Command to set a new prefix, opening file in read mode
    @commands.command()
    async def setprefix(self, ctx, *, newprefix: str):
        with open("prefixes.json", "r") as f:
            prefix = json.load(f)

        #New prefix is decided and set
        prefix[str(ctx.guild.id)] = newprefix

        #The new prefix of the server is recorded into the json file
        with open("prefixes.json", "w") as f:
            json.dump(prefix, f, indent = 4)

        await ctx.send("The server prefix has been changed")

    @commands.Cog.listener()
    async def on_guild_join(guild):
        with open("prefixes.json", "r") as f:
            prefix = json.load(f)

        #Default set prefix is recorded on the json fle
        prefix[str(guild.id)] = "!"

        #The prefix of the server is recorded into the json file
        with open("prefixes.json", "w") as f:
            json.dump(prefix, f, indent = 4)

    #Event defining when the bot leaves the server, opening file in read mode
    @commands.Cog.listener()
    async def on_guild_remove(guild):
        with open("prefixes.json", "r") as f:
            prefix = json.load(f)

        #Removes the server once the bot has left the server
        prefix.pop(str(guild.id))

        #The status prefix of the server is recorded into the json file
        with open("prefixes.json", "w") as f:
            json.dump(prefix, f, indent = 4)


async def setup(client):
    await client.add_cog(Prefix(client))
