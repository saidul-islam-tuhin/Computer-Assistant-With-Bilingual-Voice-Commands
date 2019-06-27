from text_to_speech import tts
from chat_box import App

class TextApeend(App):
    def __init__(self, bot_text):
        super().__init__()
        
        textFormatted='<p style=" font-size:8pt; font-weight:600; color:#00BC6C;">{}</p></br>'.format(bot_text)
        self.chat.append(textFormatted)


def greeting_func(text, lang):
    #obj = TextApeend(text)
    
    tts.speak(speak_text=text, language=lang)


