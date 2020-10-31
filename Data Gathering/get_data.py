

import pandas as pd
import os
import site
from youtube_api import YoutubeDataApi
from youtube_transcript_api import YouTubeTranscriptApi

site.addsitedir(os.path.relpath('../../DontUpload'))
import youtube_creds as yc

def loadTranscript(video_id):

    transcript = ''
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    for text_block in transcript_list:
        text = text_block['text']
        transcript += " " + text
    return(transcript)


def loadPlaylist(playlist_id):

    YT_KEY = yc.load_creds()
    yt = YoutubeDataApi(YT_KEY)
    playlist = yt.get_videos_from_playlist_id(playlist_id=playlist_id)
    video_ids = []
    for video in playlist:
        video_ids.append(video['video_id'])
    return(video_ids)


def loadTranscriptsForPlaylist(playlist_id):

    video_ids = loadPlaylist(playlist_id=playlist_id)
    playlist_transcripts = {}
    for video_id in video_ids:
        print(video_id)
        try:
            playlist_transcripts[video_id] = loadTranscript(video_id)
        except:
            pass
    return(playlist_transcripts)









