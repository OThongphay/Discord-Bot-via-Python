import discord
from discord.ext import commands

#Class for the Role system
class Self_Role(commands.Cog, discord.ui.View):
    def __init__(self, client):
        self.client = client
        super().__init__(timeout = None)

    #Event defining that the Role system is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Role.py is ready!")

    #Creating the button with a label and color
    @discord.ui.button(label = "Blurple", style = discord.ButtonStyle.blurple)
    async def blurple_color(self, interaction: discord.Interaction, Button: discord.ui.Button):

        #Defines the role in the variable after retrieving from the guild    
        blurple_role = discord.utils.get(interaction.guild.roles, name = "Blurple")

        role = role.is_assignable()

        print(role)

        await interaction.user.add_roles(blurple_role)

    #Creating the button with a label and color
    @discord.ui.button(label = "Grey", style = discord.ButtonStyle.grey)
    async def grey_color(self, interaction: discord.Interaction, Button: discord.ui.Button):

        #Defines the role in the variable after retrieving from the guild
        grey_role = discord.utils.get(interaction.guild.roles, name = "Grey")

        await interaction.user.add_roles(grey_role)

    #Creating the button with a label and color
    @discord.ui.button(label = "Green", style = discord.ButtonStyle.green)
    async def green_color(self, interaction: discord.Interaction, Button: discord.ui.Button):

        #Defines the role in the variable after retrieving from the guild
        green_role = discord.utils.get(interaction.guild.roles, name = "Green")

        await interaction.user.add_roles(green_role)

    #Creating the button with a label and color
    @discord.ui.button(label = "Red", style = discord.ButtonStyle.red)
    async def red_color(self, interaction: discord.Interaction, Button: discord.ui.Button):

        #Defines the role in the variable after retrieving from the guild
        red_role = discord.utils.get(interaction.guild.roles, name = "Red")

        await interaction.user.add_roles(red_role)

    @commands.command()
    async def selfrole(self, ctx):
        await ctx.send(content = "Click a button coresponding to the role you want!", view = Self_Role(self.client))


async def setup(client):
    await client.add_cog(Self_Role(client))