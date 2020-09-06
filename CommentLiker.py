from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

like = 'likeicondm.png'
count = 0
nCount = 0

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
 
    locations = pyautogui.locateAllOnScreen(like, region=(50, 0, 200, pyautogui.size().height)) 

    for loc in locations:
        x, y = loc.left, loc.top
        click(x+8, y+8)       
        time.sleep(0.05)
        nCount+=1
        
    
    pyautogui.keyDown('pagedown')
    time.sleep(1)

    print('New: ', nCount,' Total:', count+nCount)
    count += nCount
    nCount = 0
    
    
