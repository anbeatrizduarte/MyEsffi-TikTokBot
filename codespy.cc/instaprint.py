from time import sleep
import time
import pyautogui
import instacaptcha
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# abrir instagram


tirarPrint = pyautogui.hotkey('win', 'prtsc')

botaoIniciar = pyautogui.hotkey('win')
sleep(2)
procurarWhat = pyautogui.write('instagram')
sleep(2)
entrarWhat = pyautogui.hotkey('enter')
sleep(2)
procurarDirect = pyautogui.click(52,396, duration=1)
sleep(2)
pyautogui.click(281,206, duration=1)
sleep(2)
colarPrint = pyautogui.hotkey('ctrl', 'v')
sleep(2)
pyautogui.click(562,518, duration=1)
sleep(2)
pyautogui.hotkey('alt', 'f4')





