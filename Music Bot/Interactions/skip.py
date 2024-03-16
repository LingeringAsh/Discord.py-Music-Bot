import discord
from discord.ext import commands
from discord import Interaction 
from discord import app_commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,PlayerNotPlayingSKIP
class SkipInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @app_commands.command(name='skip', description='Skips the current song.')
    async def skip(self, interaction: Interaction):
        if not interaction.guild.voice_client:
            raise NotConnectedToChannel()
        if interaction.user.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = interaction.guild.voice_client
        if interaction.user.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing:
            raise PlayerNotPlayingSKIP()
        await vc.skip()
        await interaction.response.send_message("Skipped song.")
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(SkipInter(bot))