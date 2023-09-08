import pyautogui
import webbrowser
import time
from time import sleep
#import numero

webbrowser.open('https://web.whatsapp.com/send?phone=+5493804700572;+5493804277078')

time.sleep(2)

for i in range (2):
    pyautogui.typewrite('Hola capo', interval=0.5)
    time.sleep(2)
    pyautogui.press('enter')