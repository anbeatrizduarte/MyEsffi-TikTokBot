from time import sleep
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# abrir instagram

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
escreMens = pyautogui.write('Oi, foi concluída a criação de uma conta no TikTok, entre pelo acesso remoto para mais informacoes. O sistema será encerrado daqui a 3 minutos')
sleep(2)
pyautogui.hotkey('enter')
sleep(2)
pyautogui.hotkey('alt', 'f4')





