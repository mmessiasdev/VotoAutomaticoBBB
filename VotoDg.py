import pyautogui
import time

# Deixe o Editor de código em primeira tela e o browser com a tela de votação do BBB aberta em segunda tela.




# while True:
#     pyautogui.displayMousePosition()

pyautogui.hotkey("win", "s")
pyautogui.write("Vivaldi")
pyautogui.hotkey("enter")
time.sleep(4)
pyautogui.write("https://gshow.globo.com/realities/bbb/bbb22/votacao/vote-na-final-do-bbb-22-quem-voce-quer-que-venca-15b3ec29-4d06-4db3-8bd7-d4d4bd050057.ghtml")
pyautogui.hotkey("enter")
time.sleep(3)


while True:

    proxVotacao = pyautogui.locateAllOnScreen('votarNovamente.png')

    time.sleep(2)
    pyautogui.click('Dg.png')
    time.sleep(1.5)
    pyautogui.click('captha.png')
    time.sleep(1)
    pyautogui.hotkey("f5")