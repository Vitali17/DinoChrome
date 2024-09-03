import pyautogui
import time

time.sleep(2)
pyautogui.moveTo(310,355 )
while 1:
    x, y = pyautogui.position()
    r, g ,b = pyautogui.pixel(x, y)   
    if r<=200 and r>=70 and g<=200 and g>=70 and b<=200 and b>=70:
        pyautogui.press('space') 
        print(x,y)                   