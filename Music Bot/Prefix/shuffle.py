import discord
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel,NotSameVoiceChannel,NoVoiceChannel,QueueIsEmptySHUFFLE, PlayerNotPlayingSHUFFLE
class ShufflePre(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
    
    @commands.command(name= "Shuffle", description= "Shuffles the queue.")
    async def shuffle(self, ctx):
        if not ctx.voice_client:
           raise NotConnectedToChannel()
        if ctx.author.voice is None:
            raise NoVoiceChannel()
        vc : wavelink.Player = ctx.voice_client
        if ctx.author.voice.channel is not vc.channel:
            raise NotSameVoiceChannel()
        if not vc.playing:
            raise PlayerNotPlayingSHUFFLE()
        if not vc.queue:
            raise QueueIsEmptySHUFFLE()
        vc.queue.shuffle()
        await  ctx.reply("Shuffled queue.")
    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(ShufflePre(bot))
    