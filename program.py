from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Search 1: (X: 1299 Y:  946)
# Buy Now: (X: 1446 Y:  720)
# Ok: (X:  958 Y:  602)
# Send To TL: (X: 1428 Y:  773)
# Back: (X:  129 Y:  158)
# Decrease: (X: 1037 Y:  750)

print("*****STARTING BOT*****")
time.sleep(3)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    click(1299, 946) # Search
    time.sleep(1)
    click(1446, 720) # Buy Now
    time.sleep(1)
    click(958, 602) # Ok
    click(129, 158) # Back
    time.sleep(1)
    click(1037, 750) # Decrease

if keyboard.is_pressed('q') == True:
    print("*****EXITING*****")