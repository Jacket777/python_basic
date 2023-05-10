import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1  # 每次函数调用暂停一秒
pyautogui.FAILSAFE = True  # 启动自动防故障功能

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)


# 移动鼠标--绝对位置
def move_mouse():
    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)


# 移动鼠标--相对位置
def moveMouseRel():
    for i in range(10):
        pyautogui.moveRel(100, 100, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)


# 获取鼠标的位置
def getMousePosition():
    x, y = pyautogui.position()
    print(x, y)


def mouseFun():
    print("Press Ctr-C to quit: ")
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print("\nDone.")


def mouseClick():
    pyautogui.click(10, 5)
    pyautogui.click(100, 150, button='left')
    pyautogui.click(200, 250, button='right')
    pyautogui.doubleClick()
    pyautogui.mouseUp()
    pyautogui.rightClick()
    pyautogui.middleClick()


def mouseDraw():
    time.sleep(10)
    pyautogui.click()
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.2)
        pyautogui.dragRel(-distance, 0, duration=0.2)
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.2)


# 滚动鼠标
def mouseScroll():
    numbers = ''
    for i in range(200):
        numbers = numbers + str(i) + '\n'
    pyperclip.copy(numbers)
    time.sleep(8)
    pyautogui.scroll(200)


if __name__ == '__main__':
    move_mouse()
    