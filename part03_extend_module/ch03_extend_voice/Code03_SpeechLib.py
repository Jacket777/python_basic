import comtypes.gen
try:
    from comtypes.gen import SpeechLib
except ImportError:
    engine = comtypes.client.CreateObject("SAPI.SpVoice")
    stream = CreateObject('SAPI.SpFileStream')

from comtypes.client import CreateObject


# infile='demo.txt'
# outfile='demo_audio.wav'

# stream.Open(outfile,SpeechLib.SSFMCreateForWriter)
# engine.AudioOutputStream = stream
# f = open(infile,'r', enconding='utf-8')
# theText = f.read()
# f.close()
# engine.speak(theText)
# stream.close()
