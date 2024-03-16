import discord
from discord.ext import commands
from discord import Interaction 
from discord import app_commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,PlayerAlreadyResumed,PlayerNotPlayingRESUME
class ResumeInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @app_commands.command(name='resume', description='Resumes the current song.')
    async def resume(self, interaction: Interaction):
        if not interaction.guild.voice_client:
           raise NotConnectedToChannel()
        if interaction.user.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = interaction.guild.voice_client
        if not vc.playing and not vc.queue:
            raise PlayerNotPlayingRESUME()
        if interaction.user.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.paused:
            raise PlayerAlreadyResumed()
        await vc.pause(False)
        await interaction.response.send_message("Resumed song.")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(ResumeInter(bot))