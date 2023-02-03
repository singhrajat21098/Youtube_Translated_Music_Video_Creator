
from code.constants_values import language_code_dict
import re
from translate import Translator



class Generate_Translated_Subtitles:

    def __init__(self, subtitles, language):
        self.srt = subtitles
        self.language = language
        

    def remove_music_symbol(self):
        """In the transcripts, it might contain a music symbol. this function removes that"""

        for s in self.srt:
            s['text'] =  s['text'].replace("♪", "")


    def get_language_code(self):
        """
        Every language have a language code for the translator. This parser is made to translate name of the language to corresponding code.
        """
        if self.language in language_code_dict.values():
            return self.language
        else:
            lang = str(self.language).title()
            try:
                return language_code_dict[lang]
            except:
                print('language code not found')


    

    def get_translated_srt_json(self):

        """ This function generates translated transcriptions."""

        self.remove_music_symbol()
        lang_code = self.get_language_code()
        translator = Translator(to_lang= lang_code)
        


        for s in self.srt:
            s['text'] = translator.translate(s['text'])
            print(s['text'])

        


        
        
        










