import discord
from discord.ext import commands

class HelpPre(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.hybrid_command(name="help", description="Displays the help menu.")
    async def help(self,ctx, command: str.lower = None):
        if command is None:
            embed = discord.Embed(title = "**__Help__ __Menu__**", description = "**Here is a list of commands you can use 📃:**", color = discord.Color.random())
            embed.add_field(name = "**Play**", value = "``!help play``\n``/help play``") 
            embed.add_field(name = "**Resume**", value = "``!help resume``\n``/help resume``")
            embed.add_field(name = "**Pause**", value = "``!help pause``\n``/help pause``")
            embed.add_field(name = "**Skip**", value = "``!help skip``\n``/help skip``")
            embed.add_field(name= "**Disconnect**", value = "``!help disconnect``\n``/help disconnect``")
            embed.add_field(name="**Loop**", value = "``!help loop``\n``/help loop``")
            embed.add_field(name = "**Queue**", value = "``!help queue``\n``/help queue``")
            embed.add_field(name = "**Remove**", value = "``!help remove``\n``/help remove``")
            embed.add_field(name = "**Shuffle**",value= "``!help shuffle``\n``/help shuffle``")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == "play":
            embed = discord.Embed(title = "**Play Command**", description = "**This command will play the specified track requested by the user.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!play <search>`` | ``/play <search>``\n\n*Where <search> is the name or URL of the track. Takes YouTube, YouTubeMusic and SoundCloud URLs. Will default to YouTube in case of string search. If there is already a track playing it will add the requested track to the queue.*")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == "resume":
            embed = discord.Embed(title = "**Resume Command**", description = "**This command will resume the bot in case it is paused.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!resume`` | ``/resume``")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == "pause":
            embed = discord.Embed(title = "**Pause Command**", description = "**This command will pause the bot in case it is playing.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!pause`` | ``/pause``")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == "skip":
            embed = discord.Embed(title = "**Skip Command**", description = "**This command will skip the currently playing track.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!skip`` | ``/skip``")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == "disconnect":
            embed = discord.Embed(title = "**Disconnect Command**", description = "**This command will disconnect the bot from the voice channel.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!disconnect`` | ``/disconnect``")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == 'loop':
            embed = discord.Embed(title = "**Loop Command**", description = "**This command will loop the currently playing track.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!loop`` | ``/loop``\n\n*Will only loop the current track. Can not be used to loop the queue (Limitation of Wavelink Library).*")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == 'queue':
            embed = discord.Embed(title = "**Queue Command**", description = "**This command will display the current queue.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!queue<page>`` | ``/queue<page>``\n\n*Where <page> is an optional input. Defaults to '1'. Only takes integer as input (1,2,3..etc).*")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command == 'remove':
            embed = discord.Embed(title = "**Remove Command**", description = "**This command will remove the currently playing track from the queue.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!remove <queue entry>`` | ``/remove <queue entry>``\n\n*Where <queue entry> is the placement of the track in the queue. Only takes integer as input (1,2,3..etc).*")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        if command =='shuffle':
            embed = discord.Embed(title = "**Shuffle Command**", description = "**This command will shuffle the queue.**", color = discord.Color.random())
            embed.add_field(name = "**Usage:**", value = "``!shuffle`` | ``/shuffle``")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Command executed by: {ctx.author.name}")
            await ctx.reply(embed = embed)
        


async def setup(bot:commands.Bot)->None:
    await bot.add_cog(HelpPre(bot))
