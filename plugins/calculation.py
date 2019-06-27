import datetime

from text_to_speech import tts
from speech_to_text import stt

def cal_func(text, lang):
    # datetime.date.today()
    text = "Say it"
    tts.speak(speak_text=text, language=lang)

    
    eqn = eval(stt.stt_func(lang))
    tts.speak(speak_text=eval, language=lang)
    


"""
TODO:
calculate normal arithmetic.
Check any word contain in equation.
"""