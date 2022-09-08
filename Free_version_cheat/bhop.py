import os
import time
from tkinter import *
import requests
import threading
import pymem
import keyboard
import shutil


tk = Tk()
tk.title('BHOP')
canvas = Canvas(tk, width=300, height=350)


# получаем оффсеты
offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(offsets).json()

dwForceJump = int(response["signatures"]["dwForceJump"])
dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
m_fFlags = int(response["netvars"]["m_fFlags"])


def BHOP_checked():
    pm = pymem.Pymem("csgo.exe")
    _client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    appdata_p = os.environ['AppData']
    file = '%s\\CheatX\\cheatx-free\\settings\\b\\tr.cfg' % (appdata_p)
    while True:
        check_1 = os.path.isfile(file)
        if not check_1 == True:
            break

        while keyboard.is_pressed("space"):
            player = pm.read_int(_client + dwLocalPlayer)
            jump = _client + dwForceJump
            player_state = pm.read_int(player + m_fFlags)

            if player_state == 257 or player_state == 263:  # 257 - player on ground, 263 - crouch
                pm.write_int(jump, 5)
                time.sleep(0.01)  # Чем меньше задержка - тем лучше bhop, но большая нагрузка на процессор
                pm.write_int(jump, 4)
            time.sleep(0.01)
        time.sleep(0.003)

        #time.sleep(0.01)


def BHOP_not_checked():
    pm = pymem.Pymem("csgo.exe")
    _client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    appdata_p = os.environ['AppData']
    file = '%s\\CheatX\\cheatx-free\\settings\\b\\tr.cfg' % (appdata_p)
    while True:
        check_1 = os.path.isfile(file)
        if not check_1 == True:
            break
        while keyboard.is_pressed("space"):
            player = pm.read_int(_client + dwLocalPlayer)
            jump = _client + dwForceJump
            player_state = pm.read_int(player + m_fFlags)

            if player_state == 257 or player_state == 263:  # 257 - player on ground, 263 - crouch
                pm.write_int(jump, 5)
                time.sleep(0.01)  # Чем меньше задержка - тем лучше bhop, но большая нагрузка на процессор
                pm.write_int(jump, 4)



def start_bhop_checked():
    threading.Thread(target=BHOP_checked, daemon=True).start()

def start_bhop_not_checked():
    threading.Thread(target=BHOP_not_checked, daemon=True).start()