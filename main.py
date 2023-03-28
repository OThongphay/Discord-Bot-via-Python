import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
import json
from config import settings

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
@tasks.loop(seconds = 3)
async def change_status():
    await client.change_presence(activity = discord.Game(next(bot_status)))

    #Client event for the startup of the bot
@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")
    change_status.start()

#Loads the commands file containing all commands
async def load():
    for filename in os.listdir("./routes"):
        if filename.endswith(".py"):
            await client.load_extension(f"routes.{filename[:-3]}")

#Startup that loads the files associated with commands
async def main():
    async with client:
        await load()
        await client.start(f"{settings.bot_token}")

asyncio.run(main())