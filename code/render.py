from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy import editor


class Render:

    def __init__(self, video_path, subtitle_list, font, lang):

        self.video_path = video_path
        self.subtitle_list = subtitle_list
        self.generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
        self.font = font
        self.lang = lang

    def convert_srt_to_moviepy_frmt(self):

        """ The movie py library has a different format to embedd subtitles into the video than youtube. This function converts the youtube subtile to movie py subtitle"""

        self.srt = [((sub['start'], sub['start']+sub['duration']), sub['text']) for sub in self.subtitle_list]
        self.subtitles = SubtitlesClip(self.srt)
        #self.subtitles.write_srt("abc.srt")




    def render_movie(self):

        """
        This function renders the final movie.
        """
        color = 'white'

        generator = lambda txt: TextClip(txt, font= self.font, fontsize=40, color=color)

        video = editor.VideoFileClip(self.video_path)
        self.convert_srt_to_moviepy_frmt()

        subtitles = SubtitlesClip(self.srt)

        result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

        video_save_path = str(self.video_path).split('.mp4')[0] + "_with_" + str(self.lang)+".mp4" 

        result.write_videofile(video_save_path)


    
