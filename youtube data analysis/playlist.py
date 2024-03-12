import channel
import credentials
from googleapiclient.discovery import build

video_ids = []

api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client
youtube = build(api_service_name, api_version, developerKey=credentials.api_key)
request = youtube.playlistItems().list(part="snippet,contentDetails", maxResults=50, playlistId=channel.playlist_id)
response = request.execute()

# Extract video IDs from the first page
for item in response['items']:
    video_ids.append(item['contentDetails']['videoId'])

# Check if there are more pages to fetch
while 'nextPageToken' in response:
    next_page_token = response['nextPageToken']
    request = youtube.playlistItems().list(part="snippet,contentDetails", maxResults=50, playlistId=channel.playlist_id, pageToken=next_page_token)
    response = request.execute()

    # Extract video IDs from the current page
    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])

print(len(video_ids))
print("Success...!")


