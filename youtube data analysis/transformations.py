import pandas as pd
import isodate


video_df=pd.read_csv('video_details.csv')

#convert the duration in time format
video_df['video_duration'] = video_df['video_duration'].apply(lambda x: isodate.parse_duration(x))
video_df['video_duration'] = video_df['video_duration'].astype('timedelta64[s]')
video_df['video_published_date'] = video_df['video_published_date'].apply(lambda x: pd.to_datetime(x))

print(video_df.dtypes)
print(video_df)

