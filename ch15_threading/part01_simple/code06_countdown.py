# code06 应用 秒表
import time, subprocess


def countdown():
    timeLeft = 60
    while timeLeft > 0:
        print(timeLeft, end=' ')
        time.sleep(1)
        timeLeft = timeLeft - 1
    subprocess.Popen(['start', 'alarm.wav'], shell=True)


if __name__ == '__main__':
    countdown()