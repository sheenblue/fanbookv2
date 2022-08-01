# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-07-26
# @FILE   : test.py
import pyperclip
import pyautogui
import time
#time.sleep(3)
img = r'D:\pythonProject\fanbook-v2\venv\fanbook-v2\pic\1.png'

t = pyautogui.locateCenterOnScreen(img)
print(t)
# pyautogui.moveTo(t)
# pyautogui.click()
# pyperclip.copy('joyce')
# pyautogui.hotkey('ctrl','v')
# time.sleep(0.4)
img = r'D:\pythonProject\fanbook-v2\venv\fanbook-v2\pic\9.png'
t = pyautogui.locateCenterOnScreen(img)
print(t)
# pyautogui.moveTo(t)
# pyautogui.click()
# pyperclip.copy('nft')
# pyautogui.hotkey('ctrl','v')
img = r'D:\pythonProject\fanbook-v2\venv\fanbook-v2\pic\19.png'
#Point(x=292, y=932)
t = pyautogui.locateCenterOnScreen(img)
print(t)