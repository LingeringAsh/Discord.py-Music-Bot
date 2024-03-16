import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction
import wavelink
class NoTracksFound(app_commands.AppCommandError):
    pass
class NotSameVoiceChannel(app_commands.AppCommandError):
    pass
class NoVoiceChannel(app_commands.AppCommandError):
    pass
class NotConnectedToChannel(app_commands.AppCommandError):
    pass
class PlayerAlreadyPaused(app_commands.AppCommandError):
    pass
class PlayerNotPlayingPAUSE(app_commands.AppCommandError):
    pass
class PlayerAlreadyResumed(app_commands.AppCommandError):
    pass
class PlayerNotPlayingRESUME(app_commands.AppCommandError):
    pass
class QueueIsEmptySHUFFLE(app_commands.AppCommandError):
    pass
class QueueIsEmpty(app_commands.AppCommandError):
    pass
class PlayerNotPlayingSHUFFLE(app_commands.AppCommandError):
    pass
class PlayerNotPlayingSKIP(app_commands.AppCommandError):
    pass
class QueueIndexInvalid(app_commands.AppCommandError):
    pass
class QueuePageInvalid(app_commands.AppCommandError):
    pass
class PlayerNotPlayingREMOVE(app_commands.AppCommandError):
    pass
class QueueIsEmptyREMOVE(app_commands.AppCommandError):
    pass
class PlayerNotPlayingLOOP(app_commands.AppCommandError):
    pass

class ErrorHandlerInter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    async def on_app_command_error(self, interaction : Interaction, error: app_commands.AppCommandError):
        vc: wavelink.Player = interaction.guild.voice_client
        if isinstance(interaction.channel, discord.DMChannel):
            await interaction.response.send_message("Commands are not usuable in DMs.")
        if isinstance (error, AttributeError):
            await interaction.response.send_message(f"`{error}`. This is not a user error. Please report it to the bot owner if possible.")
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(f"This command cannot be used due to missing permissions. If you made any changes to my role, re-invite me or change my role to default settings.")
        elif isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(f"You don't have permission to run this command.")
        elif isinstance(error, NoTracksFound):
            await interaction.response.send_message(f"Could not find any tracks with that query.")
        elif isinstance(error, NotSameVoiceChannel):
            await interaction.response.send_message(f"I am bound to a different voice channel. Please join {vc.channel.mention} or disconnect me from the channel before trying again.")
        elif isinstance (error, NoVoiceChannel):
            await interaction.response.send_message("You need to be in a voice channel to use this command.")
        elif isinstance(error, NotConnectedToChannel):
            await interaction.response.send_message("I am not connected to a voice channel. Use the!Play or /Play command to connect me to the voice channel.")
        elif isinstance(error, PlayerAlreadyPaused):
            await interaction.response.send_message(f"Player is already paused.")
        elif isinstance(error, PlayerNotPlayingPAUSE):
            await interaction.response.send_message(f"Player is not playing anything. Can not pause.")
        elif isinstance(error, PlayerAlreadyResumed):
            await interaction.response.send_message(f"Player is already resumed.")
        elif isinstance(error, PlayerNotPlayingRESUME):
            await interaction.response.send_message(f"Player is not playing anything. Can not resume.")
        elif isinstance(error, QueueIsEmptySHUFFLE):
            await interaction.response.send_message(f"Queue is empty. Can not shuffle the queue.")
        elif isinstance(error, PlayerNotPlayingSHUFFLE):
            await interaction.response.send_message(f"Player is not playing anything. Can not shuffle the queue.")
        elif isinstance(error, QueueIsEmpty):
            await interaction.response.send_message(f"Queue is empty. Use the !Play or /Play command to add songs to the queue.")
        elif isinstance(error, QueueIsEmptyREMOVE):
            await interaction.response.send_message(f"Queue is empty. Can not remove songs from the queue")
        elif isinstance(error, PlayerNotPlayingREMOVE):
            await interaction.response.send_message(f"Player is not playing anything. Can not remove songs from the queue.")
        elif isinstance(error, QueueIndexInvalid):
            await interaction.response.send_message(f"Queue Entry is invalid. Use the !Queue or /Queue command to view the queue.")
        elif isinstance(error, PlayerNotPlayingSKIP):
            await interaction.response.send_message(f"Player is not playing anything. Can not skip.")
        elif isinstance(error, PlayerNotPlayingLOOP):
            await interaction.response.send_message(f"Player is not playing anything. Can not loop.")
        
async def setup(bot):
    await bot.add_cog(ErrorHandlerInter(bot))
