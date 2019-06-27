import speech_recognition as sr 

r = sr.Recognizer()

#audio = 'audio-[AudioTrimmer.com].wav'

#with sr.AudioFile(audio) as source:
with sr.Microphone() as source:
    #print("starting")
    #audio = r.record(source)
    #print("Done")
    r.adjust_for_ambient_noise(source, duration=1)
    print(r.energy_threshold)
    #print("Chucking rate: ", source.CHUNK)
    #print("format rate :", source.format)
    print("Say something!...")
    print(r.energy_threshold)
    r.energy_threshold += 280
    #audio = r.record(source)
    audio = r.listen(source)
    print("Over")
# recognize speech using Google Cloud Speech

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

try:
    print("Google Cloud Speech thinks you said " + r.recognize_google(audio, language='en-US'))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
"""
try:
    en_text = r.recognize_google(audio)
    text = r.recognize_google(audio, language='bn-BD')
    print(en_text)
    print(text)
    with open('output.txt','w') as f:
        print("converotr:{}\n{}".format(en_text,text), file=f)
        
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except sr.HTTPError as e:
    print("Couldn't connect to the websites perhaps , Hyper text transfer protocol error",e)

"""
"""
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print(r.energy_threshold)
    print("Chucking rate: ", source.CHUNK)
    print("format rate :", source.format)
    print("Say something!...")
    print(r.energy_threshold)
    r.energy_threshold += 280
    audio = r.listen(source)
    print("Over")

try:
    print("Parsing ...")  # Debugging To
    # for testing purposes, we're just using the default API key
    text = r.recognize_google(audio, language='en-GB')
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except sr.HTTPError as e:
    print("Couldn't connect to the websites perhaps , Hyper text transfer protocol error",e)


# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio,language='en-GB'))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language='en-GB'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

"""
# recognize speech using Google Cloud Speech
# GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
# try:
#     print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='en-GB'))
# except sr.UnknownValueError:
#     print("Google Cloud Speech could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
# WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
# try:
#     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
# except sr.UnknownValueError:
#     print("Wit.ai could not understand audio")
# exce

# pt sr.RequestError as e:
#     print("Could not request results from Wit.ai service; {0}".format(e))

# # recognize speech using Microsoft Bing Voice Recognition
# BING_KEY = "INSERT BING API KEY HERE" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY,language='en-GB'))
# except sr.UnknownValueError:
#     print("Microsoft Bing Voice Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Houndify
# HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE" # Houndify client IDs are Base64-encoded strings
# HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE" # Houndify client keys are Base64-encoded strings
# try:
#     print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY,language='en-GB'))
# except sr.UnknownValueError:
#     print("Houndify could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
# IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
# IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
# try:
#     print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='en-GB'))
# except sr.UnknownValueError:
#     print("IBM Speech to Text could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from IBM Speech to Text service; {0}".format(e))```
