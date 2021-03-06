import webbrowser
import time

import sql
import conf
from text_to_speech import tts
from speech_to_text import stt

def main(text,lang):
    data = sql.run_query(query="select * from Folders")
    if lang.lower() == 'bangla':
        speak_text = "দয়া করে ফোল্ডারটি নাম বলুন"
        wait_text = "দয়া করে কিছুক্ষন অপেক্ষা করুন"
        error_text = "{} খুজে পাওয়া যায় নি"
    else:
        speak_text = "please say the folder name"
        wait_text = "please wait for some moment"
        error_text = "{} folder not found"

    tts.speak(speak_text=speak_text,language=lang)
    time.sleep(2)
    folder_name = stt.stt_func(selected_lang='english')
    textFormatted='<b>{}: </b><span style=" font-size:16pt; font-weight:600; color:#33c4ff;">{}</span>'.format(conf.USER_NAME.capitalize(), folder_name)
    conf.CHAT_OBJ.appendHtml(textFormatted)

    print(folder_name)

    try:
        index_num = data['FolderName'].index(folder_name.lower())
        folder_path = data['Path'][index_num]
        tts.speak(speak_text=wait_text,language=lang)
        webbrowser.open(folder_path)

    except ValueError:
        tts.speak(error_text.format(folder_name),language=lang)
