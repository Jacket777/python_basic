# 代码清单02: SAPI 文本到语音的转换
from win32com import client


def say():
    engine = client.Dispatch("SAPI.SpVoice")
    # engine.Speak('')
    engine.Speak('测试结束,执行106条，失败2条，请检查')

if __name__ == '__main__':
    while True:
        say()
    