import discord
from discord import app_commands
from discord import Interaction
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,PlayerNotPlayingLOOP

class LoopInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
    
    @app_commands.command(name='loop', description='Loops the current song.')
    async def loop(self, interaction: Interaction):
        if not interaction.guild.voice_client:
            raise NotConnectedToChannel()
        if interaction.user.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = interaction.guild.voice_client
        if interaction.user.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing and not vc.queue:
            raise PlayerNotPlayingLOOP()
        if vc.queue.mode == wavelink.QueueMode.loop:
            vc.queue.mode = wavelink.QueueMode.normal
            await interaction.response.send_message(f"Stopped Looping.")
        elif vc.queue.mode == wavelink.QueueMode.normal:
            vc.queue.mode = wavelink.QueueMode.loop
            await interaction.response.send_message(f"Started Looping.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LoopInter(bot))