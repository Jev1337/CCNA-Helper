import time
from pynput import keyboard
from bs4 import BeautifulSoup
import pyautogui
import pyperclip
import json
from pystray import MenuItem as item
import pystray
from PIL import Image
import threading


def load_settings():
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    return settings


def on_press(key):
    if key == COMBINATION:
        pyautogui.click(clicks=3)
        pyautogui.hotkey('ctrl', 'c')
        #Method 1
        #time.sleep(0.2)
        #with pyautogui.hold('ctrl'):
        #    pyautogui.click()
        # press mouse button 3
        #Method 2
        #pyautogui.mouseDown(button='middle')
        #pyautogui.mouseUp(button='middle')
        #pyautogui.mouseDown(button='middle')
        #pyautogui.mouseUp(button='middle')
        #Method 3
        curpos = pyautogui.position()
        pyautogui.click(x=pyautogui.position()[0] - 400, y=pyautogui.position()[1])
        pyautogui.moveTo(curpos)
        time.sleep(0.1)
        search_text = pyperclip.paste()
        search_text = search_text.strip()
        print(f'Searching for: {search_text}')
        search_in_html(search_text)
    if key == PANIC_KEY:
        icon.stop()
        return False
    if key == keyboard.Key.f4:
        return False


def search_in_html(text):
    answers = []
    with open(SOURCE, 'r', encoding='utf-8') as f:
        contents = f.read()
    contents = contents.replace('<b>', '<strong>').replace('</b>', '</strong>')
    soup = BeautifulSoup(contents, 'html.parser')
    questions = []
    questions = soup.find_all('strong')
    questions = [question for question in questions if question.text[0].isdigit()]
    i = 0
    for question in questions:
        if text in question.text.replace(u'\xa0', u' '):
            answer = question.find_next('li', class_='correct_answer')
            while i < 5 and answer is not None:
                answers.append(answer.text)
                answer = answer.find_next('li', class_='correct_answer')
                if answer.find_previous('strong') != question:
                    break
                i += 1
            break
        
    if answers:
        print(f'Answers: {answers}')
        pyperclip.copy('\n'.join(answers))
    else:
        print('No answers found for this question!')

def exit_action(icon, item):
    icon.stop()
    pyautogui.press('f4')

def show_gui(icon, item):
    res = pyautogui.confirm(text='Cisco Packet Tracer v8.2.2 Loader.\nAll rights reserved. Cisco Systems, Inc.', title='About', buttons=['OK'])
def showup(icon, item):
    icon.stop()
    pyautogui.press('f4')

print('Only Tested on CCNA 2 v7 FRENCH')
image = Image.open("icon.png")  # replace "icon.png" with the path to your icon
icon = pystray.Icon("name", image, "PacketTracerLoader", (item('Show', showup) , item('About', show_gui),item('Exit', exit_action)))
settings = load_settings()
print('Settings loaded successfully.')
SOURCE = settings['CCNA_HTML_LOCATION']
print(f'CCNA HTML location set to {SOURCE}')
COMBINATION = keyboard.Key[settings['HOTKEY']]
print(f'Hotkey set to {settings["HOTKEY"]}')
PANIC_KEY = keyboard.Key[settings['PANIC_KEY']]
print(f'Panic key set to {settings["PANIC_KEY"]}')
print('OVERRIDE: Press F4 to exit the program.')

try:
    with keyboard.Listener(on_press=on_press) as listener:
        threading.Thread(target=icon.run).start()
        listener.join()
except Exception as e:
    print("An error occurred: ", e)
    icon.stop()



