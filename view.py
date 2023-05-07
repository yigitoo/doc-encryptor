import webview
import threading
from wsgi import app
import os
import platform
import pynput
from gtts import gTTS
from playsound import playsound
if platform.system().lower() not in ['linux', 'darwin', 'windows']:
    print("PLATFORM DESTEKLENMİYOR!\nPlatform: " + platform.system())

playsound("static/giris.mp3")

class KeyPressed(Exception): pass

"""
@brief: Deprecated code
def detect_keys():
    keys = ['alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'right alt', 'right ctrl', 'right shift', 'shift', 'windows']
    while True:
        if keyboard.read_key() in keys:
            window.destroy()
            raise SystemExit(1)
"""

def detect_keys():
    '@brief: Key Listener'
    def on_press(key):
        if key in [
        pynput.keyboard.Key.print_screen,
        pynput.keyboard.Key.alt,
        pynput.keyboard.Key.alt_l,
        pynput.keyboard.Key.alt_r,
        pynput.keyboard.Key.alt_gr,
        pynput.keyboard.Key.cmd,
        pynput.keyboard.Key.cmd_l,
        pynput.keyboard.Key.cmd_r,
        pynput.keyboard.Key.ctrl,
        pynput.keyboard.Key.ctrl_l,
        pynput.keyboard.Key.ctrl_r,
        pynput.keyboard.Key.shift,
        pynput.keyboard.Key.shift_l,
        pynput.keyboard.Key.shift_r,
    ]:
            raise KeyPressed(key)
    
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyPressed as event:
            window.destroy()
            os.system('cls || clear')
            print(f'Şüpheli bir tuşa basıldığı için program açılamıyor.')
            raise SystemExit(1)
        
keyboard_event = threading.Thread(target=detect_keys, daemon=True)
keyboard_event.start()

window = webview.create_window(
    'EFELER TOPYATAĞI İÇME SUYU ARITMA 2023 | DOKÜMAN İZLEME PANELİ',
    app,
    fullscreen=True)

webview.start()
