api_key = 'AIzaSyDJmDpWYIediUKmrwYXnv4pacm6fispYn4'

from googleapiclient.discovery import build
import urllib
import json
import urllib.request

youtube = build('youtube','v3',developerKey= api_key)
videosTitles=[]
requestList= []

def getSongs():

    request = youtube.playlistItems().list(maxResults=50, part="contentDetails", pageToken=None, playlistId='PLgIoMZYcl8MO3WkWYx7YTm7VxoonMmJXg').execute()
    
    nextPageToken = request.get('nextPageToken')
    
    requestList.append(request)

    while nextPageToken != None:

        request = youtube.playlistItems().list(maxResults=50, part="contentDetails", pageToken=nextPageToken, playlistId='PLgIoMZYcl8MO3WkWYx7YTm7VxoonMmJXg').execute()

        nextPageToken = request.get('nextPageToken')

        requestList.append(request)

        for item in requestList:

            for itemsInList in item["items"]:

                videoId = itemsInList["contentDetails"]["videoId"]
                
                params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % videoId}
                url = "https://www.youtube.com/oembed"
                query_string = urllib.parse.urlencode(params)
                url = url + "?" + query_string

                with urllib.request.urlopen(url) as response:
                    response_text = response.read()
                    data = json.loads(response_text.decode())
                    if '"' in data['title']:
                        newTitle = data['title'].replace('"','')
                        videosTitles.append(str.capitalize(newTitle))
                    else:
                        videosTitles.append(str.capitalize(data['title']))
            videosTitles.sort()
getSongs()

print("Number of songs in playlist: %s" %len(videosTitles) + "\n")

try:
    for j in videosTitles:
        print(j)
except:
    pass

#print(vidIds)