import discord
from discord.ext import commands

#Class defining this as the events command
class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Event defining that the Events command is ready
    @commands.Cog.listener()
    async def on_ready(self):
    
        print("Events.py is ready!")
    
    #Listener that logs when a member has joined the server, they are logged in an embed
    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = discord.utils.get(member.guild.channels, name = "log-channel")

        event_embed = discord.Embed(title = "Arrival Logged", description = "This user has joined the server.", color = discord.Color.green())

        event_embed.add_field(name = "User Joined: ", value = member.author.mention, inline = False)
    
        await log_channel.send(embed = event_embed)

    #Listener that logs when a member has left the server, they are logged in an embed
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = discord.utils.get(member.guild.channels, name = "log-channel")

        event_embed = discord.Embed(title = "Departure Logged", description = "This user has left the server.", color = discord.Color.green())

        event_embed.add_field(name = "User Left: ", value = member.author.mention, inline = False)
    
        await log_channel.send(embed = event_embed)


async def setup(client):
    await client.add_cog(Events(client))