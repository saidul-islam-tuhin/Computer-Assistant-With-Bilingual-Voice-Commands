import requests

from googletrans import Translator

import conf
from text_to_speech import tts
from speech_to_text import stt

def translate_func(lang):

    if lang.lower() == 'english':
        asking_text = "Please say the word or sentence"
    else:
        asking_text = "দয়া করে শব্দটি অথবা বাক্যটি বলেন "
    tts.speak(speak_text=asking_text,language=lang)

    text = stt.stt_func(selected_lang=lang)
    textFormatted='<b>{}: </b><span style=" font-size:16pt; font-weight:600; color:#33c4ff;">{}</span>'.format(conf.USER_NAME.capitalize(), text)
    conf.CHAT_OBJ.appendHtml(textFormatted)

    translator = Translator()

    if lang.lower() == 'english':
        translation = translator.translate(text, dest='bn')
        tts.speak(speak_text=translation.text,language='bangla')
    else:
        translation = translator.translate(text, dest='en')
        tts.speak(speak_text=translation.text,language='english')

    print(translation.text)
