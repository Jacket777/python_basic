import subprocess
import time

calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
# 程序启动之后 或关闭均为 calcProc.poll() 为 0
time.sleep(2)
while True:
    if not calcProc.poll() is None:
        print("程序仍在运行")
    else:
        exit_code = calcProc.poll()
        print("程序结束, 退出码为 " + str(exit_code))
        break



