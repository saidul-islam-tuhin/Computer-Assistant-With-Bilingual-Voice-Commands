from gtts import gTTS
import os
import time
import conf
import multiprocessing

def speak(speak_text, language):
    try:
        textFormatted='<b>{}: </b><span style=" font-size:16pt; font-weight:600; color:#f53164;">{}</span>'.format('System', speak_text)
        conf.CHAT_OBJ.appendHtml(textFormatted)

        if language.lower() == 'bangla':
            tts = gTTS(text=speak_text, lang='bn')
        else:
            tts = gTTS(text=speak_text, lang='en')

        tts.save("good.mp3")
        os.system("mpg321 good.mp3") # DEPENDENCY: need to install mpg321
        #time.sleep(2)
        #os.remove('good.mp3')
        # BOT message

        # task = multiprocessing.Process(target=append_text, args=(textFormatted, ))
        # task.start()
        # task = multiprocessing.Process(target=play, args=(tts, ))
        # task.start()

    except Exception as e:
        print("gtts error:",e)

def play(tts):
    try:
        tts.save("good.mp3")
        os.system("mpg321 good.mp3") # DEPENDENCY: need to install mpg321
        os.remove('good.mp3')
    except Exception as e:
        print("Play error",e)

def append_text(text):
    print(text)
    print(conf.CHAT_OBJ)
    conf.CHAT_OBJ.appendHtml(text)
    print(conf.CHAT_OBJ.toPlainText())
    print("done")
