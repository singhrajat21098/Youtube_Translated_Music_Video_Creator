from pytube import YouTube
from googleapiclient.discovery import build
import re
from youtube_transcript_api import YouTubeTranscriptApi


class Youtube_Video:
    
    def __init__(self, url, video_save_path) -> None:
        self.url = url
        self.video_id = Youtube_Video.get_video_id(url)
        self.video_save_path = video_save_path
        self.subtitles = None


    def download_youtube_video(self):

        """ This function downloads a video from Youtube"""
        
        print('Starting to download youtube video')
        yt = YouTube(self.url)

        video =  yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        video.download(self.video_save_path)
        print('Youtube Video Downloaded')


    def get_video_id(url):
        """ This functions returns video id of a youtube video based on url"""
        return re.search(r'(?<=v=)[^&#]+', url).group(0)

    
    def download_video_transcript(self):

        """ THis function downloads the transcripts"""
        
        srt = YouTubeTranscriptApi.get_transcript(self.video_id)
        
        self.subtitles = srt

        



    


    

    