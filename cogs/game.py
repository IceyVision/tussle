import discord
from discord.ext import commands
from discord import app_commands
import os
from discord import ui
from datetime import datetime
import mysql.connector as sql



class game(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command()
    async def test(self, ctx):
        await ctx.reply("Well clearly the test command works.")

    @app_commands.command(name="profile", description="View your profile and space colony stats.")
    async def profile(self, inter: discord.Interaction, user: discord.User = None):
        if user == None:
            user = inter.user
        profileEmbed = discord.Embed(title=f"{user.name}'s Profile", description="Basic info", color=discord.Colour.gold())
        profileEmbed.add_field(name = "Colony", value = "Elon Musk colony")
        profileEmbed.set_footer(text="Global rank #7", icon_url=user.display_avatar.url)
        await inter.response.send_message(embed=profileEmbed)
    
    @app_commands.command(name="market",description="View the market, setup trades, or accept trade offers that are available.")
    async def market(self, inter: discord.Interaction):
        await inter.response.send_message("Market will be available soon.")

async def setup(client:commands.Bot) -> None:
    await client.add_cog(game(client))
    