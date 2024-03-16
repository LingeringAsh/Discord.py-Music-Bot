import discord
from discord.ext import commands
from discord import Interaction 
from discord import app_commands
import wavelink
from .errorhandler import NotConnectedToChannel
class DisconnectInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
        
    @app_commands.command(name= 'disconnect', description= 'Disconnects the bot.')
    async def disconnect(self, interaction: Interaction):
        if not interaction.guild.voice_client:
            raise NotConnectedToChannel()
        else:
            vc : wavelink.Player = interaction.guild.voice_client 
            await interaction.response.send_message(f"Disconnected from channel: {vc.channel.mention}.")
            await vc.disconnect()
           
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(DisconnectInter(bot))