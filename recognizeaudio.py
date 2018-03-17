import subprocess
import speech_recognition as sr
from os import path
from rake_nltk import Rake
def convert_to_audio( VIDEO_PATH , AUDIO_PATH ):
	command = "ffmpeg -i " + VIDEO_PATH +" -ab 160k -ac 2 -ar 44100 -vn " + AUDIO_PATH 
	subprocess.call(command, shell=True)

def get_text( AUDIO_PATH):
	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), AUDIO_PATH )
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)
	BING_KEY = "5f181bd398174981b21bf2b147180ee6"
	try:
		ans=r.recognize_bing(audio, key=BING_KEY)
		print("Microsoft Bing Voice Recognition thinks you said " + ans)
		return ans
	except sr.UnknownValueError:
		print("Microsoft Bing Voice Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

def extract_keywords( text ):
	r = Rake()
	r.extract_keywords(text)
	r.get_ranked_phrases()

convert_to_audio("PRIVATE_VIDEO_3_What_are_you_passionate_about.mp4","video3.wav")
analyze =get_text("video3.wav")
print(get_text("video3.wav"))
extract_keywords(text)

#
#command = "ffmpeg -i c.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
#subprocess.call(command, shell=True)
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")
#r = sr.Recognizer()
#with sr.AudioFile(AUDIO_FILE) as source:
    #audio = r.record(source)  # read the entire audio file
#BING_KEY = "5f181bd398174981b21bf2b147180ee6"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
#try:
    #print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
#except sr.UnknownValueError:
    #print("Microsoft Bing Voice Recognition could not understand audio")
#except sr.RequestError as e:
    #print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))