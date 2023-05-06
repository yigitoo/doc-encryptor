import webview
import keyboard
import threading
from wsgi import app
import sys
def detect_keys():
    keys = ['alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'right alt', 'right ctrl', 'right shift', 'shift', 'windows']
    while True:
        if keyboard.read_key() in keys:
            window.destroy()
            raise SystemExit

keyboard_event = threading.Thread(target=detect_keys, daemon=True)
keyboard_event.start()

window = webview.create_window(
    'EFELER TOPYATAĞI İÇME SUYU ARITMA 2023 | DOKÜMAN İZLEME PANELİ',
    app,
    fullscreen=True)

webview.start()