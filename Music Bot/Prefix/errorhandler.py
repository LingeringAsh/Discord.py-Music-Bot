import discord
from discord.ext import commands
import wavelink
class NoTracksFound(commands.CommandError):
    pass
class NotSameVoiceChannel(commands.CommandError):
    pass
class NoVoiceChannel(commands.CommandError):
    pass
class NotConnectedToChannel(commands.CommandError):
    pass
class PlayerAlreadyPaused(commands.CommandError):
    pass
class PlayerNotPlayingPAUSE(commands.CommandError):
    pass
class PlayerAlreadyResumed(commands.CommandError):
    pass
class PlayerNotPlayingRESUME(commands.CommandError):
    pass
class QueueIsEmptySHUFFLE(commands.CommandError):
    pass
class QueueIsEmpty(commands.CommandError):
    pass
class PlayerNotPlayingSHUFFLE(commands.CommandError):
    pass
class PlayerNotPlayingSKIP(commands.CommandError):
    pass
class QueueIndexInvalid(commands.CommandError):
    pass
class QueuePageInvalid(commands.CommandError):
    pass
class PlayerNotPlayingREMOVE(commands.CommandError):
    pass
class QueueIsEmptyREMOVE(commands.CommandError):
    pass
class PlayerNotPlayingLOOP(commands.CommandError):
    pass
class InvalidLoopMode(commands.CommandError):
    pass
class ErrorHandlerPre(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        vc: wavelink.Player = ctx.voice_client
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.send("Commands are not usuable in DMs.")
        if isinstance (error, AttributeError):
            await ctx.reply(f"`{error}`. This is not a user error. Please report it to the bot owner if possible.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Missing argument: `{error.param.name}`\nRefer to the !Help or /Help command for the proper usage of commands.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.reply(f"No command with that name found.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply(f"This command cannot be used due to missing permissions. If you made any changes to my role, re-invite me or change my role to default settings.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"You don't have permission to run this command.")
        elif isinstance(error, NoTracksFound):
            await ctx.reply(f"Could not find any tracks with that query.")
        elif isinstance(error, NotSameVoiceChannel):
            await ctx.reply(f"I am bound to a different voice channel. Please join {vc.channel.mention} or disconnect me from the channel before trying again.")
        elif isinstance (error, NoVoiceChannel):
            await ctx.reply("You need to be in a voice channel to use this command.")
        elif isinstance(error, NotConnectedToChannel):
            await ctx.reply("I am not connected to a voice channel. Use the !Play or /Play command to connect me to the voice channel.")
        elif isinstance(error, PlayerAlreadyPaused):
            await ctx.reply(f"Player is already paused.")
        elif isinstance(error, PlayerNotPlayingPAUSE):
            await ctx.reply(f"Player is not playing anything. Can not pause.")
        elif isinstance(error, PlayerAlreadyResumed):
            await ctx.reply(f"Player is already resumed.")
        elif isinstance(error, PlayerNotPlayingRESUME):
            await ctx.reply(f"Player is not playing anything. Can not resume.")
        elif isinstance(error, QueueIsEmptySHUFFLE):
            await ctx.reply(f"Queue is empty. Can not shuffle the queue.")
        elif isinstance(error, PlayerNotPlayingSHUFFLE):
            await ctx.reply(f"Player is not playing anything. Can not shuffle the queue.")
        elif isinstance(error, QueueIsEmpty):
            await ctx.reply(f"Queue is empty. Use the !Play or /Play command to add songs to the queue.")
        elif isinstance(error, QueueIsEmptyREMOVE):
            await ctx.reply(f"Queue is empty. Can not remove songs from the queue")
        elif isinstance(error, PlayerNotPlayingREMOVE):
            await ctx.reply(f"Player is not playing anything. Can not remove songs from the queue.")
        elif isinstance(error, QueueIndexInvalid):
            await ctx.reply(f"Queue Entry is invalid. Use the !Queue or /Queue command to view the queue.")
        elif isinstance(error, PlayerNotPlayingSKIP):
            await ctx.reply(f"Player is not playing anything. Can not skip.")
        elif isinstance(error, PlayerNotPlayingLOOP):
            await ctx.reply(f"Player is not playing anything. Can not loop.")
async def setup(bot):
    await bot.add_cog(ErrorHandlerPre(bot))