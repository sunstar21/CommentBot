
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import threading

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

#var videoid;
#var options = {
 #   host: 'www.googleapis.com',
  #  port: 443,
   # path: '/youtube/v3/search?key=AIzaSyDHxUC5OnFc8zKoxKpoR9GtKby-pNvncI0&channelId=UCke6I9N4KfC968-yRcd5YRg&part=snippet,id&order=date&maxResults=1',
    #method: "GET",
#}
import requests
import json
from datetime import datetime
my_date = datetime.now()

url = 'https://www.googleapis.com//youtube/v3/search?key=AIzaSyDHxUC5OnFc8zKoxKpoR9GtKby-pNvncI0&channelId=UCke6I9N4KfC968-yRcd5YRg&part=snippet,id&order=date&maxResults=1'
x = requests.get(url)
yy = json.loads(x.text);

def callfunc(youtube):
    print("in call func")
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

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "cs.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    callfunc(youtube)

if __name__ == "__main__":
    main()



