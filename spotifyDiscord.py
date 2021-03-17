scope = 'playlist-modify-public'

from youtubesearchpython import PlaylistsSearch
from spotipy.oauth2 import SpotifyOAuth
from discord.ext import commands
import spotipy.util as util
import sys
import spotipy
import discord

client = commands.Bot(command_prefix='=')
token = SpotifyOAuth(scope=scope, username='313lalyzjb4gnxfrus7icyr2dwje')
sp=spotipy.Spotify(auth_manager=token)

# def searchSong():

@client.event
async def on_ready():
    print("Bot is ready")

# @client.command(aliases=['recommends'])
# async def recommendations(ctx):
#     topSongs=sp.recommendations(limit=20 ,seed_genres='pop', seed_artists='4NHQUGzhtTLFvgF5SZesLK',seed_tracks='0c6xIDDpzE81m2q797ordA')
#     print(topSongs)

@client.command()
async def shutdown(ctx):
    if ctx.author.id == 805374385249976380: #replace OWNERID with your user id
        print("shutdown")
        try:
            await ctx.bot.logout()
        except:
            print("EnvironmentError")
            self.bot.clear()
    else:
        await ctx.send("You do not own this bot!")

@client.command(aliases=['find'])
async def findPlaylist(ctx, *, query):
        
    playlistsSearch = PlaylistsSearch(query, limit = 1)

    videoId = playlistsSearch.result()['result'][0]['id']
    playlistId = 'https://www.youtube.com/playlist?list=' + videoId
    
    await ctx.send("!p " + playlistId )

    # print(playlistsSearch.result()['result'][0]["type"])

# @client.command()
# async def removeSong(ctx,*,q):
#     allSongsString = "```"
#     allSongs=[]
#     allSongsSorted=[]
#     songsDetails=[]
#     songToBeRemoved=[]
    
#     playlistItems=sp.playlist_items(playlist_id='7ty2ERkBYbTpUibPCGP6gE')
#     for idx, item in enumerate(playlistItems['items']):
#         songsDetails.append({'idx':idx, 'name':item['track']['artists'][0]['name'], 'uri':item['track']['id']})
#     # await ctx.send(allSongsString)
#     # for details in songsDetails:
#         # print(details)
#     songToBeRemoved.append([{'uri':songsDetails[int(q)-1]['uri'], 'positions': [int(q)-1]}])
#     # songToBeRemoved.append(songsDetails[q]['uri'])
#     sp.user_playlist_remove_specific_occurrences_of_tracks('313lalyzjb4gnxfrus7icyr2dwje', '7ty2ERkBYbTpUibPCGP6gE', songToBeRemoved)


@client.command(aliases=['add','addasong','ddsongs'])
async def addSong(ctx, *, suggestion):
    # query=input("Search for a song:")
    listOfSongFound=[]
    results = sp.search(q=suggestion,limit=20)
    # for track in results['tracks']['items']:
    track = results['tracks']['items'][0]['uri']
    listOfSongFound.append(track)

    sp.user_playlist_add_tracks('313lalyzjb4gnxfrus7icyr2dwje', playlist_id='7ty2ERkBYbTpUibPCGP6gE', tracks=listOfSongFound)
    await ctx.send('Done!')

@client.command()
async def checkDailyMix(ctx):
    songName = '```'
    playlists=sp.playlist_items(playlist_id='37i9dQZF1E37ocP53m9LnZ')
    for idx, item in enumerate(playlists['items']):
        if idx == 20:
            break
        else:
            songDetails= item['track']['artists'][0]['name'] + " - " + item['track']['name'] 
            songName+=songDetails
            songName+="\n\n"
    songName+="```"
    await ctx.send(songName)

@client.command()
async def all(ctx):
    allSongsString = ""
    allSongs=[]
    allSongsSorted=[]
    songsDetails=[]
    
    playlistItems=sp.playlist_items(playlist_id='7ty2ERkBYbTpUibPCGP6gE')
    for idx, item in enumerate(playlistItems['items']):
        songFullName = item['track']['artists'][0]['name'] + " - " + item['track']['name']
        songsDetails.append({'idx':idx, 'name':item['track']['artists'][0]['name']})
        allSongs.append(songFullName)
    allSongsSorted = sorted(allSongs)
    for song in allSongsSorted:
        allSongsString += song 
        allSongsString += "\n"
    if len(allSongsString) <= 2000:
        await "```" + ctx.send(allSongsString) + "```"
    else: 
        await ctx.send("```" + allSongsString[:1985] + "```")
        await ctx.send("```"+allSongsString[1986::]+"```")

client.run('ODE5MjQwMjMwNDEzNTMzMjA0.YEju6w.4Nwd-MKo_PY0uMvjZsHo2lY_NFg')