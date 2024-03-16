import discord
from discord import app_commands
from discord import Interaction
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel, NotSameVoiceChannel, NoVoiceChannel, PlayerNotPlayingREMOVE,QueueIsEmptyREMOVE,QueueIndexInvalid
class RemoveInter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def remove(self, interaction: Interaction, queue_entry: int):
        if not interaction.guild.voice_client:
            raise NotConnectedToChannel()
        if interaction.user.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = interaction.guild.voice_client
        if interaction.user.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing:
            raise PlayerNotPlayingREMOVE()
        if not vc.queue:
            raise QueueIsEmptyREMOVE()
        if queue_entry > len(vc.queue._queue):
            raise QueueIndexInvalid()
        trackindex = vc.queue._queue[queue_entry - 1]
        del vc.queue._queue[queue_entry - 1]
        await interaction.response.send_message(f'Removed `{trackindex.title}` from the queue.')
    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(RemoveInter(bot))
    