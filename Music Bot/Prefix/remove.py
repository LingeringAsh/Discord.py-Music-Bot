import discord
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel, NotSameVoiceChannel, NoVoiceChannel, PlayerNotPlayingREMOVE,QueueIsEmptyREMOVE,QueueIndexInvalid
class RemovePre(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @commands.command(name= "Remove", description= "Removes the specified queue entry from the queue.")
    async def remove(self, ctx, queue_entry:int):
        if not ctx.voice_client:
            raise NotConnectedToChannel()
        if ctx.author.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = ctx.voice_client
        if ctx.author.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing:
            raise PlayerNotPlayingREMOVE()
        if not vc.queue:
            raise QueueIsEmptyREMOVE()
        if queue_entry > len(vc.queue._queue):
            raise QueueIndexInvalid()
        trackindex = vc.queue._queue[queue_entry - 1]
        del vc.queue._queue[queue_entry - 1]
        await  ctx.reply(f'Removed `{trackindex.title}` from the queue.')

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(RemovePre(bot))
