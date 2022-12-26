from time import sleep
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# abrir whatsapp

botaoIniciar = pyautogui.hotkey('win')
sleep(2)
procurarWhat = pyautogui.write('whatsapp')
sleep(2)
entrarWhat = pyautogui.hotkey('enter')
sleep(2)
procuraGrupo = pyautogui.write('bot')
sleep(2)
pyautogui.hotkey('left')
sleep(2)
entrarGrupo = pyautogui.hotkey('enter')
sleep(2)
pyautogui.click(518,642, duration=1)
sleep(2)
escreMens = pyautogui.write('Oi, a conta precisa passar por uma verificacao de captcha! Voce tem apenas 60 segundos para realiza-la.')
sleep(2)
pyautogui.hotkey('enter')
sleep(2)
pyautogui.hotkey('alt', 'f4')

# print do codigo

navegador = webdriver.Chrome()

navegador.get("https://twice.jype.com/")

tirarPrint = pyautogui.hotkey('win', 'prtsc')

botaoIniciar = pyautogui.hotkey('win')
sleep(2)
procurarWhat = pyautogui.write('whatsapp')
sleep(2)
entrarWhat = pyautogui.hotkey('enter')
sleep(2)
procuraGrupo = pyautogui.write('bot')
sleep(2)
pyautogui.hotkey('left')
sleep(2)
entrarGrupo = pyautogui.hotkey('enter')
sleep(2)
pyautogui.click(518,642, duration=1)
sleep(2)

colarPrint = pyautogui.hotkey('ctrl', 'v')
sleep(2)
pyautogui.hotkey('enter')



