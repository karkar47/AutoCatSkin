#***************************************************
# author: @karuchkar. Do not erase the authorship! *
#***************************************************
import time
import requests
import pyautogui
import py_win_keyboard_layout

response = requests.get('http://f1051093.xsph.ru/data1.json')

programm_version = 110
data = response.json()
name = data['name']
version = data['version']
can = data['can']
a = 1
t = 1

if can == 1:
    print("Загружемся...")
else:
    exit()

if programm_version < version:
    print("Пожалуйста, обновите AutoCatSkin или скачайте подлинную версию.")

print('  ___        _        _____       _   _____ _    _       ')
print(' / _ \      | |      /  __ \     | | /  ___| |  (_)      ')
print('/ /_\ \_   _| |_ ___ | /  \/ __ _| |_\ `--.| | ___ _ __  ')
print("|  _  | | | | __/ _ \| |    / _` | __|`--. \ |/ / | '_ \ ")
print('| | | | |_| | || (_) | \__/\ (_| | |_/\__/ /   <| | | | |')
print('\_| |_/\__,_|\__\___/ \____/\__,_|\__\____/|_|\_\_|_| |_|')
print("author: @karuchkar")
print("")

i1 = input('Пожалуйста, введите интервал между сообщениями в секундах(def = 901сек(15мин)).')
i2 = input('Пожалуйста, укажите слово, которое нужно писать(def = Кошка скин).')
i3 = input('Укажите язык, который вы предпочитаете для вашего слова(Русский - 1, Английский - 2).')

if i1 == "def":
    interval = 901
elif i1 == "":
    exit()
else:
    interval = int(i1)
    pass

if i2 == "def":
    word = "Кошка скин"
elif i2 == "":
    exit()
else:
    word = i2
    pass

if i3 == 1:
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04190419)
elif i3 == "":
    exit()
else:
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    pass

print("Через 10сек запустится бот. Успейте переключить раскладку на нужный вам язык и кликнуть на поле ввода в телеграм")

if t == 1:
    time.sleep(10)
    pyautogui.write(word)
    with pyautogui.hold('ctrl'):
        pyautogui.press('enter')
        #kb.release(Key.enter)
    print('Первая попытка увенчалась успехом.')
    t = 2
else:
    pass

while a == 1:
    time.sleep(interval)
    pyautogui.write(word)
    with pyautogui.hold('ctrl'):
        pyautogui.press('enter')
        #kb.release(Key.enter)
    print('Команда введена, ждем 15 мин...')

# Чай татарский бик тэмлэ, бик тэмлэ