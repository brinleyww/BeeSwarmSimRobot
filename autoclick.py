import time
import random
import pyautogui
from datetime import datetime

def clicker(x,y):
    random.seed(datetime.now())
    c=random.randint(1,5)
    time.sleep(c)
    pyautogui.moveTo(x,y)
    pyautogui.click()
def move_right_circle():
    pyautogui.keyDown('up')
    pyautogui.keyDown('right')
    time.sleep(3)
    pyautogui.keyUp('up')
    pyautogui.keyUp('right')
def move_back_left_circle():
    pyautogui.keyDown('down')
    pyautogui.keyDown('left')
    time.sleep(3)
    pyautogui.keyUp('down')
    pyautogui.keyUp('left')
while True:
    random.seed(datetime.now())
    n=random.randint(0,1)
    if n==0:
        move_right_circle()
    if n==1:
        move_back_left_circle()