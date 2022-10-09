import pyautogui
import time
import cv2
full=False
for i in range(4):
    time.sleep(1)
    print("x")
while True:
    for i in range(60):
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
    for i in range(40):
        pyautogui.keyDown("d")
        pyautogui.keyUp("d")
    for i in range(60):
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
    pyautogui.mouseDown(button='left')
    while full==False:
        
        for i in range(17):
            pyautogui.keyDown("w")
            pyautogui.keyUp("w")
        for i in range(31):
            pyautogui.keyDown("a")
            pyautogui.keyUp("a")
        for i in range(17):
            pyautogui.keyDown("s")
            pyautogui.keyUp("s")
        for i in range(31):
            pyautogui.keyDown("d")
            pyautogui.keyUp("d")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("screen1.png")
        sample_image = cv2.imread("screen1.png")
        e=sample_image[6,1558][2]
        if e>240:
            full=True

    for i in range(60):
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")
    for i in range(40):
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
    for i in range(60):
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")
    pyautogui.keyDown("e")
    pyautogui.keyUp("e")