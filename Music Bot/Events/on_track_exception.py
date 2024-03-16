import discord
from discord.ext import commands
import wavelink
from discord import app_commands
import asyncio

class TrackException(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_wavelink_track_exception(self, payload: wavelink.TrackExceptionEventPayload):
        vc = payload.player
        await vc.ctx.send(f"Unexpected Error:`{Exception}` Try again.")

async def setup(bot):
    await bot.add_cog(TrackException(bot))