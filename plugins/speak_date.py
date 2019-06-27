import datetime

from text_to_speech import tts

bangla_weekday_name = ["সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার", "শনিবার", "রবিবার"]

def date_format(datetime_obj,lang):
    if lang == 'bangla':
        today = 'অাজ '+ bangla_weekday_name[datetime_obj.weekday()] + str(datetime_obj.strftime( '%d, %B %Y'))
    else:
        today = str(datetime_obj.strftime('it is %A, %d, %B %Y'))
    return today


def date_func(text, lang):
    now = datetime.datetime.now()
    today_date = date_format(now, lang)
    tts.speak(speak_text=today_date, language=lang)


"""
TODO:
tell whats the day.
"""
