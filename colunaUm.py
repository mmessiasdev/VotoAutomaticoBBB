import pyautogui
import time


# while True:
#     pyautogui.displayMousePosition()


# 678, 323

# 668, 400 - Arthur
#      604, 510

pyautogui.hotkey("alt", "tab")

while True:

    pyautogui.hotkey("f5")
    time.sleep(3)
    pyautogui.moveTo(668, 400)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(604, 510)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(683, 283)
    pyautogui.click()
    time.sleep(3)