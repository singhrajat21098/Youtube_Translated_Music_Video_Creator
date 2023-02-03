from code.download_yt_video import Youtube_Video
from code.subtitle_processing import Generate_Translated_Subtitles
from code.render import Render
import config 
import os 
import glob
from os import listdir
from os.path import isfile, join
import shutil
import threading




# Removes old files from the Newly created video folder if any
try:
    shutil.rmtree(config.video_save_path)
except:
    pass

os.makedirs(config.video_save_path)




# Creates a object og Youtube_Video class
# This class is used to download youtube video and the transcript
yt_v = Youtube_Video(config.youtube_video_url, config.video_save_path)


# Creating a thread to download video from youtube
download_video_thread = threading.Thread(target = yt_v.download_youtube_video(), name = "download_video_thread" )

# thread to download transcript of youtube video
download_transcript_thread = threading.Thread(target= yt_v.download_video_transcript(), name = "download_transcript_thread")

# Starting both the thread
download_video_thread.start()
download_transcript_thread.start()

# Joining transcript thread with main thread
download_transcript_thread.join()

# Creating new object to translate subtitles
gts = Generate_Translated_Subtitles(yt_v.subtitles, config.language)

# Creating new thread to translate the subtitles and starting the thread
translate_subtitle_thread = threading.Thread(target= gts.get_translated_srt_json(), name = "translate_subtitle_thread")
translate_subtitle_thread.start()

# Joining all the remaining threads
download_video_thread.join()
translate_subtitle_thread.join()

# The folder should only contain one video. This code helps to find the path of that video
onlyfiles = [join(config.video_save_path, f) for f in listdir(config.video_save_path) if isfile(join(config.video_save_path, f))]


# Creating a New video with subtitles
r = Render(onlyfiles[0], gts.srt , config.font_style, config.language)
r.convert_srt_to_moviepy_frmt()
r.render_movie()







