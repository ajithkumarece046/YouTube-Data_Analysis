from googleapiclient.discovery import build

import credentials

import pandas as pd

api_service_name = "youtube"
api_version = "v3"


    
youtube = build(api_service_name, api_version, developerKey=credentials.api_key)

request = youtube.channels().list(part="snippet,contentDetails,statistics",id="UCJcCB-QYPIBcbKcBQOTwhiA")
response = request.execute()

channel_name=response['items'][0]['snippet']['title']
playlist_id=response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
viewscount=response['items'][0]['statistics']['viewCount']
videoscount=response['items'][0]['statistics']['videoCount']
channel_published_date=response['items'][0]['snippet']['publishedAt']