# -- coding: utf-8 --
import pandas as pd
import json
from apiclient.discovery import build
import os


youTubeApiKey = os.environ.get('YouTubeAPI')
youtube=build('youtube','v3',developerKey=youTubeApiKey)
channelId='UCRWfQs1NzGqUOTF77MWHO_g'

fr_videos = pd.read_csv("Data/FRvideos.csv")
video_ids = fr_videos['video_id']
video_ids = video_ids[0:100]

for i in range(video_ids.shape[0]//40+1):
    fichier = "test/contentDetails-" + str(i) + ".json"
    with open(fichier, "a") as file:
        res = (youtube).videos().list(id=','.join(video_ids[(i*40):(i*40+40)]),part='contentDetails').execute()
        file.write(json.dumps(res))
file.close()