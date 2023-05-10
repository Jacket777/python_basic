import pyttsx3 as pyttsx
import pythoncom
from win32com import client


engine = client.Dispatch("SAPI.SpVoice")
engine.Speak('胡昕冉，大笨蛋')


# engine = pyttsx.init()
# engine.say('好好学习')
# engine.runAndWait()
# engine.stop()
