
# python -m pip install selenium
# py -m pip install pyautogui
# python -m pip install Pillow pyscreenshot

import webbrowser
import pyautogui
import selenium
import time

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# abrir o TikTok
abrirFirefox = webdriver.Firefox()

abrirTikTok = abrirFirefox.get('https://www.tiktok.com/pt-BR/')
sleep(2)

pyautogui.FAILSAFE = False

# abrir Temp Mail
abrirFirefox.execute_script("window.open('');") 
abrirFirefox.switch_to.window(abrirFirefox.window_handles[1])
new_url = "https://temp-mail.org/pt/"
abrirTempMail = abrirFirefox.get(new_url)
sleep(5)

# copia email gerado
copyEmail = pyautogui.click(879,324, duration=1)
sleep(2)

# voltar pro TikTok e clicar em Login
abrirFirefox.switch_to.window(abrirFirefox.window_handles[0])
clicarLogin = pyautogui.click(1124,118,duration=1)
sleep(4)

# clicar em criar nova conta
clickCriarConta = pyautogui.click(757,628,duration=1)
sleep(2)

# clicar em continuar com Twitter
clicarTwitter = pyautogui.click(654,475,duration=1)
sleep(2)

# clicar em criar entrar
criarTwitter = pyautogui.click(59,275, duration=1)
sleep(1)

maximizarTela = pyautogui.click(417,15, duration=1)
sleep(1)

inscreverTw = pyautogui.click(709,626, duration=1)
pyautogui.click(672,436, duration=1)

# nome da conta
escreNomeConta = pyautogui.write('Teste')
sleep(1)

criarComEmail = pyautogui.click(830,402)
sleep(1)

pyautogui.click(659,356, duration=1)

# endereço de email
colarEndereço = pyautogui.hotkey('ctrl', 'v')
sleep(2)

mes = pyautogui.click(583,561, duration=1), pyautogui.click(535,293, duration=1) 
sleep(2)
dia = pyautogui.click(736,561, duration=1), pyautogui.click(693,296, duration=1)
sleep(2)
selecAno = pyautogui.click(831,560, duration=1)

numRepet = 8

def funcao_para_repetir():
    pyautogui.click(874,534)
    
for numero in range(0, numRepet):
    funcao_para_repetir()

ano = pyautogui.click(823,350, duration=1)
sleep(2)
pyautogui.click(694,648, duration=1)
sleep(2)
pyautogui.click(694,648, duration=1)

# tirar print para salvar nome e email do Twitter
import pyscreenshot 
image = pyscreenshot.grab()
image.show()
image.save('screenshot.png','png')

# salvando print

pyautogui.click(501,57, duration=1)
pyautogui.click(357,234, duration=1)
pyautogui.click(566,478, duration=1)
pyautogui.click(823,46, duration=1)

# apertando em inscrever-se

pyautogui.click(678,639, duration=1)
sleep(2)

# enviando mensagem para o celular sobre o captcha

import instacaptcha

sleep(240)


escreSenha = pyautogui.write('bialinda1.')
pyautogui.click(687,645, duration=1)
sleep(2)

pyautogui.click(687,645, duration=1)
sleep(3)

# tirando print dos dados da conta

instaprint

#copiando nome de usuário

pyautogui.hotkey('ctrl', 'a')
sleep(2)
pyautogui.hotkey('ctrl', 'c')
sleep(2)

# finalizando cadastro do twitter

pyautogui.click(687,645, duration=1)
sleep(1)
pyautogui.click(689,518, duration=1)
sleep(1)
pyautogui.click(679,641, duration=1)
sleep(1)
pyautogui.click(536,354, duration=1)
sleep(1)
pyautogui.click(685,349, duration=1)
sleep(1)
pyautogui.click(826,363, duration=1)
sleep(1)
pyautogui.click(834,645, duration=1)
sleep(1)
pyautogui.click(834,645, duration=1)
sleep(1)
pyautogui.click(837,369, duration=1)
sleep(1)
pyautogui.click(834,645, duration=1)
sleep(1)

# fechando aba da criação de conta Twitter

pyautogui.click(1340,9, duration=1)
sleep(1)

# voltando para o TikTok

abrirFirefox.switch_to.window(abrirFirefox.window_handles[0])

# continuar com o Twitter

pyautogui.click(748,627, duration=1)
sleep(2)
pyautogui.click(658,541, duration=1)
sleep(2)

# limpando cache e cookies

abrirFirefox.delete_all_cookies()

# autorizar

pyautogui.click(97,335, duration=1)
sleep(2)


botaoIniciar = pyautogui.hotkey('win')
sleep(2)
procurarWhat = pyautogui.write('firefox')
sleep(2)
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

pyautogui.hotkey('ctrl', 'v')
sleep(2)
pyautogui.hotkey('enter')
sleep(2)
escreSenha = pyautogui.write('bialinda1.')
pyautogui.hotkey('enter')
sleep(2)

# abrindo tiktok manualmente


pyautogui.hotkey('ctrl', 't')
sleep(2)
entrarTikTok = pyautogui.write('tiktok')
sleep(2)
pyautogui.hotkey('enter')
sleep(4)

# fazendo login com twitter

pyautogui.click(1130,110, duration=1)
sleep(2)
pyautogui.click(678,537, duration=1)
sleep(2)

# criando conta do twitter

import instacaptcha

sleep(60)

pyautogui.click(556,323, duration=1)
sleep(2)
pyautogui.click(515,505, duration=1)
sleep(2)
pyautogui.click(701,323, duration=1)
sleep(2)
pyautogui.click(661,540, duration=1)
sleep(2)

numRepet2 = 4

def funcao_para_repetir_secon():
    pyautogui.click(855,591,duration=1)
    
for numero in range(0, numRepet2):
    funcao_para_repetir_secon()

sleep(2)
pyautogui.click(773,492, duration=1)
sleep(2)

# avançar

pyautogui.click(673,412, duration=1)
sleep(2)

pyautogui.click(672,332, duration=1)
sleep(2)



colarCriarUsuario = pyautogui.hotkey('ctrl', 'v')
pyautogui.click(686,416, duration=1)
sleep(2)

sleep(60)

# ver perfil e mandar print

pyautogui.click(1213,116, duration=1)
sleep(2)
pyautogui.click(1126,173, duration=1)
sleep(2)

import instaprint

sleep(2)

import instafinal


sleep(300)