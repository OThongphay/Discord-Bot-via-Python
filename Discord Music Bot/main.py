import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
import json

#When the client is created it grabs the prefix used for any servers that the bot is on
def get_server_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

#Defines the bot prefix and intents
client = commands.Bot(command_prefix = get_server_prefix, intents = discord.Intents.all())

#The default help codeblock message is now gone, allowing the visually appealing help command be used
client.remove_command("help")

#Creates a list of bot statuses via cycle method
bot_status = cycle(["Minecraft","Genshin Impact", "Terraria", "Overwatch 2", "Stardew Valley", "Black Ops 3 Zombies"])

#Creates loop to cycle through the listed activity statuses
@tasks.loop(hours = 2)
async def change_status():
    await client.change_presence(activity = discord.Game(next(bot_status)))

#Client event for the startup of the bot
@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")
    change_status.start()

#Event defining when the bot joins the server, opening file in read mode
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    #Default set prefix is recorded on the json fle
    prefix[str(guild.id)] = "!"

    #The prefix of the server is recorded into the json file
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent = 4)

#Event defining when the bot leaves the server, opening file in read mode
@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    #Removes the server once the bot has left the server
    prefix.pop(str(guild.id))

    #The status prefix of the server is recorded into the json file
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent = 4)

#Command to set a new prefix, opening file in read mode
@client.command()
async def setprefix(ctx, *, newprefix: str):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    #New prefix is decided and set
    prefix[str(ctx.guild.id)] = newprefix

    #The new prefix of the server is recorded into the json file
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent = 4)

    await ctx.send("Prefix changed successfully")

#Loads the commands file containing all commands
async def load():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"commands.{filename[:-3]}")

#Startup that loads the files associated with commands
async def main():
    async with client:
        await load()
        await client.start("(YOUR_TOKEN_HERE)")

asyncio.run(main())