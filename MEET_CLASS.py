import pyautogui
import time
import datetime

now = datetime.datetime.now()
hora = now.hour 
minuto = now.minute
print("Para usar o programa feche ou minimize todas as janelas")
print("Qual o dia da semana de hoje: ")
print("seg/ter/qua/qui/sex")

#dia da semana 
dia = str.lower(input()) 
time.sleep(5)
#abre chrome
pyautogui.click(885,753)
time.sleep(4)
#clica no perfil escola
pyautogui.click(416,408)
time.sleep(2)
#clica na barra de pesquisa
pyautogui.click(320,50)

"""
        links das aulas   
        linguagem e programação https://classroom.google.com/c/MjY3MTE5NjM5MDQ3
        web https://classroom.google.com/c/MjY1MTE1NTYxODI1
        fund e suporte https://classroom.google.com/c/MjY1MDk5MzIyMzA3
        sociologia https://classroom.google.com/c/MjY1MDk5ODI4NjI4
        geografia https://classroom.google.com/c/MjU0NDY3NDU2NzM5
        historia https://classroom.google.com/c/MjU0NDY2ODM3NTEx
        matemática https://classroom.google.com/c/MjY3MTU2ODM4NjQ4
        portugues https://classroom.google.com/c/MjY0MTQzNDY5OTMx
        inglês https://classroom.google.com/c/MjU0NDI1NTgwODU1
        filosofia https://classroom.google.com/c/MjYzNTIwODg1NzQx
        biologia https://classroom.google.com/c/MjYzMTEzMTE3ODMw
        educação fisica https://classroom.google.com/c/MjU0MzQwMjUxNjE3
"""
if (dia == "seg"): 
    if (hora == 19 and (minuto >=14 and minuto <=50)): #primeira aula
        pyautogui.write('https://classroom.google.com/c/MjY1MDk5MzIyMzA3') #FUND E SUPOR
        pyautogui.press('enter')
    if (hora == 19 and minuto >=51): #segunda aula
        pyautogui.write('https://classroom.google.com/c/MjY3MTE5NjM5MDQ3') #PROGRAMAÇÃO
        pyautogui.press('enter')
    if (hora == 20 and minuto >=44 ): #terceira aula
        pyautogui.write('https://classroom.google.com/c/MjU0NDI1NTgwODU1') #INGLES
        pyautogui.press('enter')
    if (hora == 21 and minuto >=29 ): #quarta aula
        pyautogui.write('https://classroom.google.com/c/MjYzMTEzMTE3ODMw') #BIOLOGIA
        pyautogui.press('enter')
    if (hora == 22 and minuto >=14): #quinta aula
        pyautogui.write('https://classroom.google.com/c/MjY0MTQzNDY5OTMx') #PORTUGUES
        pyautogui.press('enter')
elif (dia == "ter"): 
    if (hora == 19 and (minuto >=14 and minuto <=50)): #primeira aula
        pyautogui.write('https://classroom.google.com/c/MjYzMTEzMTE3ODMw') #BIOLOGIA
        pyautogui.press('enter')
    if (hora == 19 and minuto >=51): #segunda aula
        pyautogui.write('https://classroom.google.com/c/MjY1MDk5MzIyMzA3') #FUND E SUPOR
        pyautogui.press('enter')
    if (hora == 20 and minuto >=44 ): #terceira aula
        pyautogui.write('https://classroom.google.com/c/MjU0NDY3NDU2NzM5') #GEOGRAFIA
        pyautogui.press('enter')
    if (hora == 21 and minuto >=29 ): #quarta aula
        pyautogui.write('https://classroom.google.com/c/MjU0MzQwMjUxNjE3') #ED FISICA
        pyautogui.press('enter')
    if (hora == 22 and minuto >=14): #quinta aula
        pyautogui.write('https://classroom.google.com/c/MjY3MTU2ODM4NjQ4') #MATEMATICA
        pyautogui.press('enter')
elif (dia == "qua"):
    if (hora == 19 and (minuto >=14 and minuto <=50)): #primeira aula
        pyautogui.write('https://classroom.google.com/c/MjY1MDk5MzIyMzA3') #FILOSOFIA
        pyautogui.press('enter')
    if (hora == 19 and minuto >=51): #segunda aula
        pyautogui.write('https://classroom.google.com/c/MjY3MTE5NjM5MDQ3') #PROGRAMAÇÃO
        pyautogui.press('enter')
    if (hora == 20 and minuto >=44 ): #terceira aula
        pyautogui.write('https://classroom.google.com/c/MjY1MDk5MzIyMzA3') #FUND E SUPOR
        pyautogui.press('enter')
    if (hora == 21 and minuto >=29 ): #quarta aula
        pyautogui.write('https://classroom.google.com/c/MjY3MTU2ODM4NjQ4') #MATEMATICA
        pyautogui.press('enter')
    if (hora == 22 and minuto >=14): #quinta aula
        pyautogui.write('https://classroom.google.com/c/MjY1MTE1NTYxODI1') #WEB
        pyautogui.press('enter')
elif (dia == "qui"): 
    if (hora == 19 and (minuto >=14 and minuto <=50)): #primeira aula
        pyautogui.write('https://classroom.google.com/c/MjY0MTQzNDY5OTMx') #PORTUGUES
        pyautogui.press('enter')
    if (hora == 19 and minuto >=51): 
        pyautogui.write('https://classroom.google.com/c/MjY1MDk5MzIyMzA3') #FILOSOFIA
        pyautogui.press('enter')
    if (hora == 20 and minuto >=44 ):
        pyautogui.write('https://classroom.google.com/c/MjY1MTE1NTYxODI1') #WEB
        pyautogui.press('enter')
    if (hora == 21 and minuto >=29 ):
        pyautogui.write('https://classroom.google.com/c/MjU0MzQwMjUxNjE3') #ED FISICA
        pyautogui.press('enter')
    if (hora == 22 and minuto >=14): 
        pyautogui.write('https://classroom.google.com/c/MjU0NDI1NTgwODU1') #INGLES
        pyautogui.press('enter')
elif (dia == "sex"): 
    if (hora == 19 and (minuto >=14 and minuto <=50)): 
        pyautogui.write('https://classroom.google.com/c/MjU0NDY2ODM3NTEx') #HISTORIA
        pyautogui.press('enter')
    if (hora == 19 and minuto >=51): 
        pyautogui.write('https://classroom.google.com/c/MjU0NDY2ODM3NTEx') #HISTORIA
        pyautogui.press('enter')
    if (hora == 20 and minuto >=44 ): 
        pyautogui.write('https://classroom.google.com/c/MjY1MDk5ODI4NjI4') #SOCIOLOGIA
        pyautogui.press('enter')
    if (hora == 21 and minuto >=29 ): 
        pyautogui.write('https://classroom.google.com/c/MjY1MDk5ODI4NjI4') #SOCIOLOGIA
        pyautogui.press('enter')
    if (hora == 22 and minuto >=14): 
        pyautogui.write('https://classroom.google.com/c/MjU0NDY3NDU2NzM5') #GEOGRAFIA
        pyautogui.press('enter')
else:
    print("ERROR")


