##−∗−coding :  utf−8−∗−

import os
import sys
import time

import speech_recognition as sr

import logging

LOG_FORMAT = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="test.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w",
                    )
logger = logging.getLogger(__name__)

def stt_func(selected_lang):
    
    r = sr.Recognizer()
    text = None

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print(r.energy_threshold)
        #print("Chucking rate: ", source.CHUNK)
        #print("format rate :", source.format)
        os.system("mpg321 beep.mp3")
        #time.sleep(2)
        print("Say something!...")
        #print(r.energy_threshold)
        r.energy_threshold += 280
        audio = r.listen(source)
        print("Over! Starting recognize.....")

    try:
        
        if selected_lang.lower() == 'bangla':
            speech_text = r.recognize_google(audio, language='bn-BD')
            logger.debug(str(speech_text.encode()))

            text_into_byte = speech_text.encode('utf-8')

            # b'\xe0\xa7\x9f' = য়
            normalized_text_byte = text_into_byte.replace(b'\xe0\xa6\xaf\xe0\xa6\xbc', b'\xe0\xa7\x9f')
            text = normalized_text_byte.decode('utf-8')
            
        elif selected_lang.lower() == 'english':
            text = r.recognize_google(audio, language='en-US')
        
        else:
            pass
       
        #with open('output.txt','w') as f:
        #    print("convertor:{}\n{}".format(en_text,bn_text), file=f)  
        #print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='bn-BD'))
        
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))

    if text:
        print("Google Cloud Speech thinks you said: " + text)  
    else:
        text = "Can not Recognize."
        print(text)

    return text
