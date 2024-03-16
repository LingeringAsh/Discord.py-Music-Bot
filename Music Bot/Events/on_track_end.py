import discord
from discord.ext import commands
import wavelink
from discord import app_commands
import asyncio



class TrackEnd(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, payload: wavelink.TrackEndEventPayload) -> None:
        vc = payload.player
        track = payload.track
        if vc.queue.mode == wavelink.QueueMode.loop:
            await vc.play(track)
            await vc.ctx.send(f"Now playing: `{track.title}` Looping Song.", delete_after = 20)
        elif vc.queue:
            next_track = vc.queue.get()
            await vc.play(next_track)
            await vc.ctx.send(f"Now playing: `{next_track}`", delete_after = 20)
        else:
            await asyncio.sleep(10)
            if vc.playing:
                return
            await vc.ctx.send(f"Disconnected from {vc.channel.mention} due to inactivity.")
            await vc.disconnect()


async def setup(bot):
    await bot.add_cog(TrackEnd(bot))