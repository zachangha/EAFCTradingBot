from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# SELLING
# List: (X: 1351 Y:  591)
# Buy Now Price: (X: 1395 Y:  790)
# Confirm Listing: (X: 1425 Y:  921)

print("*****STARTING BOT*****")
time.sleep(3)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def putPrice():
    pyautogui.write("500", 0.25)

while keyboard.is_pressed('q') == False:
    click(1351, 591)
    sleep(1)
    click(1395, 790)
    sleep(1)
    putPrice()
    sleep(1)
    click(1425, 921)

if keyboard.is_pressed('q') == True:
    print("*****EXITING*****")