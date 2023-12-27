from pyautogui import*
import time
import keyboard
import win32api, win32con
import json

# Search 1: (X: 1299 Y:  946)
# Buy Now: (X: 1446 Y:  720)
# Ok: (X:  958 Y:  602)
# Send To TL: (X: 1428 Y:  773)
# Back: (X:  129 Y:  158)
# Decrease: (X: 1037 Y:  750)
# Increase Bid: (X:  969 Y:  751)
# Decrease Min Bid: (X:  507 Y:  754)


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

if __name__ == "__main__":

    print("*****LOADING CORDINATES*****")
    with open("buying.json", "r") as json_file:
        coordinates = json.load(json_file)
    print(coordinates)
    print("*****STARTING BOT*****")
    time.sleep(3)

    while keyboard.is_pressed('q') == False:
        
        
        click(coordinates[0][0], coordinates[0][1]) # Search
        time.sleep(1)
        click(coordinates[1][0], coordinates[1][1]) # Buy Now
        time.sleep(0.75)
        click(coordinates[2][0], coordinates[2][1]) # Ok
        time.sleep(2)
        click(coordinates[3][0], coordinates[3][1]) # Send to TL
        time.sleep(1)
        click(coordinates[4][0], coordinates[4][1]) # Back
        time.sleep(1)
        click(coordinates[5][0], coordinates[5][1]) # Increase Min Bid

        click(coordinates[0][0], coordinates[0][1]) # Search
        time.sleep(1)
        click(coordinates[1][0], coordinates[1][1]) # Buy Now
        time.sleep(0.75)
        click(coordinates[2][0], coordinates[2][1]) # Ok
        time.sleep(2)
        click(coordinates[3][0], coordinates[3][1]) # Send to TL
        time.sleep(1)
        click(coordinates[4][0], coordinates[4][1]) # Back
        time.sleep(1)
        click(coordinates[6][0], coordinates[6][1]) # Decrease Min Bid



    if keyboard.is_pressed('q') == True:
        print("*****EXITING*****")