import pyautogui
import time

time.sleep(8)
add = ["123", "shart", "cloven", "123", "10"]

for word in add:
    pyautogui.write(word)
    pyautogui.press("tab")