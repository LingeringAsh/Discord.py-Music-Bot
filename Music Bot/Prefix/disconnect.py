import discord
from discord.ext import commands
import wavelink
from .errorhandler import NotConnectedToChannel
class DisconnectPre(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
    
    @commands.command(name="Disconnect", description = "Disconnects the bot from the channel.")
    async def disconnect(self,ctx):
        if not ctx.voice_client:
           raise NotConnectedToChannel()
        else:
            vc : wavelink.Player = ctx.voice_client
            await vc.disconnect()
            await ctx.reply(f"Disconnected from channel: {vc.channel.mention}.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DisconnectPre(bot))