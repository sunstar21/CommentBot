import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import threading
import requests
import json
from google.oauth2.credentials import Credentials
from datetime import datetime
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
my_date = datetime.now()
url = 'https://www.googleapis.com//youtube/v3/search?key=AIzaSyDHxUC5OnFc8zKoxKpoR9GtKby-pNvncI0&channelId=UCke6I9N4KfC968-yRcd5YRg&part=snippet,id&order=date&maxResults=1'
x = requests.get(url)
yy = json.loads(x.text)

def callfunc():
    api_service_name = "youtube"
    api_version = "v3"
    creds = Credentials.from_authorized_user_file('token.json', scopes)
    youtube = googleapiclient.discovery.build(
       api_service_name, api_version, credentials=creds)
    request = youtube.commentThreads().insert(
        part="snippet",
        body={
          "snippet": {
            "topLevelComment": {
              "snippet": {
                "textOriginal": "If you sub to me, ill sub to you too!! Plz sub!"
              }
            },
            "channelId": "UCke6I9N4KfC968-yRcd5YRg",
            "videoId": yy['items'][0]["id"]["videoId"]
          }
        }
    )
    response = request.execute()
    print(response)
callfunc()