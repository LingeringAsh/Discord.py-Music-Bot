import discord
from discord.ext import commands
import wavelink
import datetime
import asyncio
from .errorhandler import NotConnectedToChannel,QueueIsEmpty
class QueueInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="queue", description='Displays the queue.')
    async def queue(self, ctx, page: int = 1):
        if not ctx.voice_client:
            raise NotConnectedToChannel()
        vc: wavelink.Player = ctx.guild.voice_client
        queue = vc.queue
        if not vc.playing and not vc.paused:
            raise QueueIsEmpty()
        items_per_page = 8
        total_pages = max((len(queue) - 1) // items_per_page + 1, 1)
        if not (1 <= page <= total_pages):
            await ctx.reply(f"Page is invalid. Please pick a page from 1 to {total_pages}.")    
        start_index = (page - 1) * items_per_page
        end_index = min(start_index + items_per_page, len(queue))
        em = discord.Embed(title="**__Queue__**", color=0x000000)
        em.add_field(
            name=f"**Now Playing 🎶:** \n{vc.current.title}",
            value=f"**Duration:** `{str(datetime.timedelta(milliseconds=round((vc.position), -3)))}` **/** `{str(datetime.timedelta(milliseconds=(vc.current.length)))}` **|** **Channel:** `{vc.current.author}`",
            inline=False)
        if not queue:
            em.add_field(name="**In Queue 📃:**", value='**The Queue is Empty. \n Use the command `/play <song name>` to queue something.**')
        else:
            em.add_field(name="**In Queue 📃:**", value='***These songs will be played next:***')
            for index in range(start_index, end_index):
                track = queue[index]
                em.add_field(name=f"`{index + 1}.` {track.title}", value=f"**Duration:** `{str(datetime.timedelta(milliseconds=track.length))}` **|** **Channel:** `{track.author}`", inline=False)
        if total_pages > 1:
            em.set_footer(icon_url=ctx.author.avatar.url, text=f"Command executed by: {ctx.author.name} | Page {page}/{total_pages}")
        message = await ctx.reply(embed=em)
        if page > 1:
            await message.add_reaction("◀️")
        if page < total_pages:
            await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=15, check=check)
            await message.delete()
            if str(reaction.emoji) == "◀️" and page > 1:
                await self.queue(ctx, page - 1)
            elif str(reaction.emoji) == "▶️" and page < total_pages:
                await self.queue(ctx, page + 1)
        except asyncio.TimeoutError:
            pass

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(QueueInter(bot))