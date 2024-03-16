import discord
from discord import app_commands
from discord import Interaction
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,QueueIsEmptySHUFFLE, PlayerNotPlayingSHUFFLE

class ShuffleInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @app_commands.command(name='shuffle', description='Shuffles the queue.')
    async def shuffle(self, interaction: Interaction):
        if not interaction.guild.voice_client:
            raise NotConnectedToChannel()
        if interaction.user.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = interaction.guild.voice_client
        if interaction.user.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing:
            raise PlayerNotPlayingSHUFFLE()
        if not vc.queue:
            raise QueueIsEmptySHUFFLE()
        vc.queue.shuffle()
        await interaction.response.send_message("Shuffled the queue.")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(ShuffleInter(bot))