
import webbrowser
import pyautogui
import selenium
import time

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys




botaoIniciar = pyautogui.hotkey('win')
sleep(2)
procurarWhat = pyautogui.write('firefox')
sleep(2)
pyautogui.hotkey('ctrl', 'a')
sleep(1)
pyautogui.hotkey('ctrl', 'c')
entrarWhat = pyautogui.hotkey('enter')
sleep(3)

# entrar no site Twitter

entrarTwitter = pyautogui.write('twitter')
sleep(2)
pyautogui.hotkey('enter')
sleep(2)

pyautogui.click(1118,688, duration=1)
sleep(2)

pyautogui.click(627,448, duration=1)

# colocando endereço de email da conta

#pyautogui.hotkey('ctrl', 'v')

pyautogui.write('myesffi')
sleep(2)
pyautogui.hotkey('enter')
sleep(2)
escreSenha = pyautogui.write('sakurasato22')
pyautogui.hotkey('enter')
sleep(2)

# abrindo tiktok manualmente


pyautogui.hotkey('ctrl', 't')
sleep(2)
pyautogui.write('tiktok')
sleep(2)
pyautogui.hotkey('enter')
sleep(4)

# fazendo login com twitter

pyautogui.click(1130,110, duration=1)
sleep(2)
pyautogui.click(678,537, duration=1)


sleep(100)