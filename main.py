import time # Время чтобы спать
import requests # Запросы, чтобы узнавать у сайта цифру актуальной версии
import keyboard # Клавиши для основного процесса

response = requests.get('http://f1051093.xsph.ru/data1.json') # Узнаем у сайта цифру актуальной версии
data = response.json()
version = data['version'] # Цифра актуальной версии
can = data['can']

program_version = 110 # Цифра версия ЭТОЙ программы
infinity = 1 # Переменная для выполнения основного процесса
first_try = 1 # Первая попытка

if can == 1:
    print("Загружемся...")
else:
    exit()

if program_version < version: # Сравниваем цифру нашей версии и цифру версии, которую мы получили с сайта
    print("Пожалуйста, обновите AutoCatSkin или скачайте подлинную версию.")

print("AutoCatSkin v1.1.0") # Название и версия
print("author: @karuchkar") # Авторство
print("")

i1 = input('Пожалуйста, введите интервал между сообщениями в секундах(def = 901сек(15мин)): ')
i2_word = input('Пожалуйста, укажите слово, которое нужно писать: ')

if i1 == "def": # Если человек выставил def (по умолчанию), то мы присваиваем переменной interval значение по умолчанию
    interval = 901
elif i1 == "": # Если человек ничего не ввел, то пусть пойдёт и подумает перед тем, как ничего не указывать!
    exit()
else:
    interval = int(i1) # Если человек ввел что-то иное, то мы присваиваем переменной interval то значение, которое ввел человек

print("Через 10сек запустится бот. Успейте кликнуть на поле ввода")

if first_try == 1: # Функция первой попытки
    time.sleep(10) # Спим 10 сек
    keyboard.write(i2_word) # Пишем слово
    keyboard.press("ctrl") # Нажимаем ctrl
    keyboard.press_and_release("enter") # Нажимаем и отпускаем одновременно enter
    keyboard.release("ctrl") # Отпускаем ctrl
    print('Первая попытка увенчалась успехом.')
    first_try = 0 # Аннулируем первую попытку

while infinity == 1: # Основной процесс
    time.sleep(interval) # Спим по интервалу
    keyboard.write(i2_word) # Пишем слово
    keyboard.press("ctrl") # Нажимаем ctrl
    keyboard.press_and_release("enter") # Нажимаем и отпускаем одновременно enter
    keyboard.release("ctrl") # Отпускаем ctrl
    print(f'Команда введена, ждем {interval} сек...')

#Чай татарский бик тэмлэ, бик тэмлэ