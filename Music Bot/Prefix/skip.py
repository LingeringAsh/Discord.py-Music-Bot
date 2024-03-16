import discord
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,PlayerNotPlayingSKIP
class SkipPre(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @commands.command(name= "Skip",description = "Skips the currently playing song.")
    async def skip(self, ctx):
        if not ctx.voice_client:
           raise NotConnectedToChannel()
        if ctx.author.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = ctx.voice_client
        if ctx.author.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing:
            raise PlayerNotPlayingSKIP()
        await vc.skip()
        await  ctx.reply("Skipped song.")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(SkipPre(bot))