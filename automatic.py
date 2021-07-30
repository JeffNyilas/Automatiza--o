import pyautogui
import time

pyautogui.alert("Não use nada do seu computador enquanto o código estiver rodando. Pressione 'OK' para iniciar a execucão.")
pyautogui.PAUSE = 0.5
# abrir o google drive no meu computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.press('enter')

# entrar na minha área de trabalho
pyautogui.hotkey('winleft', 'd')
# selecionar o arquivo que eu quero fazer backup e arrastá-lo
pyautogui.moveTo(3704, 98)
pyautogui.mouseDown()
pyautogui.moveTo(2318, 1413)

# enquanto arrasta o arquivo, mudar a tela para o Google Drive
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

# soltar o arquivo no Google Drive
pyautogui.mouseUp()

# aguardar 5 segundos
time.sleep(5)

pyautogui.alert("Código executado. Computador novamente disponível para uso.")
















