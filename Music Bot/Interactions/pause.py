import discord
from discord.ext import commands
from discord import Interaction 
from discord import app_commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,PlayerAlreadyPaused, NoVoiceChannel, PlayerNotPlayingPAUSE
class PauseInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
    
    @app_commands.command(name='pause', description='Pauses the current song.')
    async def pause(self, interaction: Interaction):
        if not interaction.guild.voice_client:
           raise NotConnectedToChannel()
        if interaction.user.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = interaction.guild.voice_client
        if not vc.playing and not vc.queue:
            raise PlayerNotPlayingPAUSE()
        if interaction.user.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if vc.paused:
            raise PlayerAlreadyPaused()
        await vc.pause(True)
        await interaction.response.send_message("Paused.")
            
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(PauseInter(bot))