import discord
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,PlayerAlreadyResumed,PlayerNotPlayingRESUME
class ResumePre(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
    
    @commands.command(name= "Resume",description = "Resumes the song.")
    async def resume(self, ctx):
        if not ctx.voice_client:
           raise NotConnectedToChannel()
        if ctx.author.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = ctx.voice_client
        if not vc.playing and not vc.queue:
            raise PlayerNotPlayingRESUME()
        if ctx.author.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.paused:
            raise PlayerAlreadyResumed()
        await vc.pause(False)
        await  ctx.reply("Resumed song.")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(ResumePre(bot))
    