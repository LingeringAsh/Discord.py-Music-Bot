import discord
from discord.ext import commands
from discord import Interaction 
from discord import app_commands
import wavelink
import datetime
from .errorhandler import NoTracksFound, NotSameVoiceChannel, NoVoiceChannel

class PlayInter(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot

    @app_commands.command(name = "play", description = "Plays the song you search for.")
    async def play(self, interaction: Interaction ,*, search : str):
        if interaction.user.voice is None:
             raise NoVoiceChannel()
        if not interaction.guild.voice_client:
            vc: wavelink.Player = await interaction.user.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = interaction.guild.voice_client
        tracks: wavelink.Search = await wavelink.Playable.search(search)
        vc.ctx = interaction.channel
        if not tracks:
            raise NoTracksFound()
        if interaction.user.voice.channel is not vc.channel:
             raise NotSameVoiceChannel()
        if isinstance(tracks, wavelink.Playlist):
            plist = await wavelink.Playable.search(search)
            for track in plist.tracks:
                        vc.queue.put(track)
                        no_of_tracks = len(plist.tracks)
            if not vc.playing:
                    await vc.play(vc.queue.get())
                    embed = discord.Embed(title="Now Playing 🎶", description=f"[**{plist.name}**]({str(search)}).", color= 0x0c100)
                    embed.add_field(name="**__Channel:__**", value=f'`{track.author}`')
                    embed.add_field(name="**__Tracks:__**", value=f"`{no_of_tracks}`")
                    embed.set_thumbnail(url=track.artwork)
                    embed.set_footer(icon_url=interaction.user.avatar.url, text=f"Command requested by: {interaction.user.name}")
                    return await interaction.response.send_message(embed=embed)
            if vc.playing:
                    embed = discord.Embed(title="Added to the queue 📃", description=f"[**{plist.name}**]({str(search)}).", color=0x0c100)
                    embed.add_field(name="**__Channel:__**", value=f'`{track.author}`' )
                    embed.add_field(name="**__Tracks:__**", value=f"`{no_of_tracks}`")
                    embed.set_thumbnail(url=track.artwork)
                    embed.set_footer(icon_url=interaction.user.avatar.url, text=f"Command requested by: {interaction.user.name}")
                    await interaction.response.send_message(embed=embed)
                    return await vc.queue.put_wait(track)
        track: wavelink.Playable = tracks[0]
        if not vc.playing:
            await vc.queue.put_wait(track)
            embed =  discord.Embed(title="Now Playing 🎶", description=f"[**{track.title}**]({str(track.uri)}).", color= 0x0c100)
            embed.add_field(name="**__Channel:__**", value=f'`{track.author}`')
            embed.add_field(name="**__Duration:__**", value=f'`{str(datetime.timedelta(milliseconds=round((track.length), -3)))}`')
            embed.set_thumbnail(url = track.artwork)
            embed.set_footer(icon_url= interaction.user.avatar.url, text=f"Command executed by: {interaction.user.name}")
            await interaction.response.send_message(embed = embed)
            await vc.play(vc.queue.get())
        else:
            await vc.queue.put_wait(track)
            embed =  discord.Embed(title="Added to queue 📃", description=f"[**{track.title}**]({str(track.uri)}).", color= 0x0c100)
            embed.add_field(name="**__Channel:__**", value=f'`{track.author}`')
            embed.add_field(name="**__Duration:__**", value=f'`{str(datetime.timedelta(milliseconds=round((track.length), -3)))}`')
            embed.set_thumbnail(url = track.artwork)
            embed.set_footer(icon_url= interaction.user.avatar.url, text=f"Command executed by: {interaction.user.name}")
            await interaction.response.send_message(embed = embed)

        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(PlayInter(bot))