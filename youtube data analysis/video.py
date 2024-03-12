from googleapiclient.discovery import build
import credentials
from playlist import video_ids
import csv

api_service_name = "youtube"
api_version = "v3"

# Create an empty list to store video details
video_details = []

# Loop through video IDs in batches of 50
for i in range(0, len(video_ids), 50):
    youtube = build(api_service_name, api_version, developerKey=credentials.api_key)
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=','.join(video_ids[i:i+50])
    )
    response = request.execute()
    
    # Append video details to the list
    video_details.extend(response['items'])

# Write video details to a CSV file
with open('video_details.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['video_id', 'video_title', 'video_views', 'video_likes', 'video_comment', 'video_duration', 'video_published_date'])
    for item in video_details:
        video_id = item['id']
        video_title = item['snippet']['title']
        video_views = item['statistics']['viewCount']
        video_likes = item['statistics'].get('likeCount', 0)
        video_comment = item['statistics'].get('commentCount', 0)
        video_duration = item['contentDetails']['duration']
        video_published_date = item['snippet']['publishedAt']
        csv_writer.writerow([video_id, video_title, video_views, video_likes, video_comment, video_duration, video_published_date])

print("Success...!")














