import discord
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,PlayerNotPlayingLOOP,InvalidLoopMode
class LoopPre(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
       
    @commands.command(name="Loop", Description="Repeats the current song.")
    async def loop(self, ctx):
        if not ctx.voice_client:
            raise NotConnectedToChannel()
        if ctx.author.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = ctx.voice_client
        if ctx.author.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing and not vc.queue:
            raise PlayerNotPlayingLOOP()
        if vc.queue.mode == wavelink.QueueMode.loop:
            vc.queue.mode = wavelink.QueueMode.normal
            await ctx.reply(f"Stopped Looping.")
        elif vc.queue.mode == wavelink.QueueMode.normal:
            vc.queue.mode = wavelink.QueueMode.loop
            await ctx.reply(f"Started Looping.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LoopPre(bot))
        