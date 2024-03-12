from snowflake.connector import connect
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
import credentials
from transformations import video_df


conn=connect(
    user=credentials.snowflake_username,
    password=credentials.snowflake_password,
    account='hbafdvi-ri17181',
    warehouse='COMPUTE_WH',
    database='youtube',
    schema='VJSIDDHU_VLOGS',
    role='ACCOUNTADMIN'
)


cur=conn.cursor()



cur.execute('CREATE OR REPLACE TABLE video_data ("video_id" VARCHAR,"video_title" VARCHAR,"video_views" INTEGER,"video_likes" INTEGER,"video_comment" INTEGER,"video_duration" VARCHAR,"video_published_date" TIMESTAMP)')

print("Table created Sucessfully")

write_pandas(conn,video_df,table_name="VIDEO_DATA",use_logical_type = True)

print("Sucessfully loaded a video data to snowflake")


