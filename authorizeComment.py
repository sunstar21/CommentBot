import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import threading
import requests
import base64
import json

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    client_secrets_file = "cs.json"
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    t = open('token.json', 'w')
    t.write(credentials.to_json())

if __name__ == "__main__":
    main()



