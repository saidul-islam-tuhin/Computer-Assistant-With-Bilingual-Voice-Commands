import webbrowser

from speech_to_text import stt
from text_to_speech import tts

def google_search_func(lang):
    if lang.lower() == 'bangla':
        speak_text = "অাপনি কি জানতে চান"
    else:
        speak_text = "What do you want to know"
    tts.speak(speak_text=speak_text,language=lang)

    search_text = stt.stt_func(selected_lang=lang)
    
    if search_text.lower() == 'can not recognize':
        tts.speak(speak_text="Check your internet connection and try again",language='english')
    else:
        link = 'https://www.google.com/search?q={}'.format(search_text)
        try:
            webbrowser.open(link)
        except Exception as e:
            print("google_search error:",e)