import discord
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,PlayerAlreadyPaused, NoVoiceChannel, PlayerNotPlayingPAUSE
class PausePre(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @commands.command(name = "Pause", description = "Pauses the song.")
    async def pause(self, ctx):
        if not ctx.voice_client:
           raise NotConnectedToChannel()
        if ctx.author.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = ctx.voice_client
        if not vc.playing and not vc.queue:
            raise PlayerNotPlayingPAUSE()
        if ctx.author.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if vc.paused:
            raise PlayerAlreadyPaused()
        await vc.pause(True)
        await  ctx.reply("Paused song.")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(PausePre(bot))