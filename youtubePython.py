import youtubesearchpython
import vlc
import pafy
import time
import pyttsx3

# print(result.result())

def playSongFromLocal():

    url = r"C:\Users\User\Music\Adele - Hello.mp3"
    # Over here playurl is best URL to play. Then we use VLC to play it.

    vlc.MediaPlayer(url).play()
    while True:
        pass
# playSong()

def playSongInternet(q):
    engine = pyttsx3.init()
    query = youtubesearchpython.VideosSearch(q)
    url = query.result()["result"][0]["link"]
    print(url)
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    # Over here playurl is best URL to play. Then we use VLC to play it.

    Instance = vlc.Instance()

    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    while True: 
        if player.get_state() == vlc.State.Ended:
            break
        pass
    engine.say("Finished playing")
    import my_telegram
    my_telegram.putMethod()
