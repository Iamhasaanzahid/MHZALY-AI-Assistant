import os
import time
import pyautogui

print("WhatsApp Call Test Shuru Ho Raha Hai...")
os.system("start whatsapp:")
time.sleep(2)

pyautogui.hotkey('win', 'up') # Maximize
time.sleep(1)

pyautogui.hotkey('ctrl', '1') # Go to Chats Tab
time.sleep(0.5)

pyautogui.hotkey('ctrl', 'f')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')

pyautogui.write("Noor Fatimah", interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

pyautogui.hotkey('ctrl', 'shift', 'c')
print("Call command bhej di gayi hai.")