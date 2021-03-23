from .models import *
from .api_keys import GOOGLE_API_KEYS
from datetime import datetime, timedelta
import requests
from background_task import *




def create_object(response):
    # saving object
    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        video_thumbnails = item['snippet']['thumbnails']['default']['url']
        video_description = item['snippet']['description']
        video_channel_title = item['snippet']['channelTitle']
        video_channel_id = item['snippet']['channelId']
        video_publishing_datetime = item['snippet']['publishedAt']
        try:
            VideoData.objects.create(
                video_id=video_id,
                video_title=video_title,
                video_description=video_description,
                video_channel_id=video_channel_id,
                video_channel_title=video_channel_title,
                video_publishing_datetime=video_publishing_datetime,
                video_thumbnails=video_thumbnails,
            )
            print("object created !!")
        except:
            print("Error !!")



@background(schedule=300)
def do():

    print("scheduled !!!!")
    apiKeys = GOOGLE_API_KEYS
    time_now = datetime.now()
    last_request_time = time_now - timedelta(minutes=5)
    link = 'https://www.googleapis.com/youtube/v3/search/'
    valid = False

    for key in apiKeys:
        try:
            response = requests.get(link,
                                    params={
                                        "part": 'snippet',
                                        "maxResults": 50,
                                        "q": 'cricket',
                                        "key": key,
                                        "publishedAfter" : str(last_request_time.replace(microsecond=0).isoformat()+'Z')
                                    })
            valid = True
            response = response.json()
            if valid:
                create_object(response)
                break
            print(response)
        except:
            print("error !!")

