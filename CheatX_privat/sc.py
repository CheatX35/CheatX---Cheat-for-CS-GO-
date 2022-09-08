import ctypes
import requests
import keyboard
import pymem
import pymem.process
import time
import win32api
from win32gui import GetWindowText, GetForegroundWindow
from win32gui import FindWindow, GetWindowRect
import threading
import os

offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(offsets).json()

dwForceAttack = int(response["signatures"]["dwForceAttack"])



def get_value():
    appdata_p = os.environ['AppData']
    file_v = '%s\\CheatX\\cheatx-private\\settings\\sc\\v.cfg' % (appdata_p)
    file = open(file_v)
    read = int(file.read())
    if read > 0 and read < 10 or read == 10 or read == 0:
        number = 0.006
        return number

    if read > 10 and read < 20 or read == 20:
        number = 0.01
        return number

    if read > 20 and read < 30 or read == 30:
        number = 0.03
        return number

    if read > 30 and read < 40 or read == 40:
        number = 0.08
        return number

    if read > 40 and read < 50 or read == 50:
        number = 0.12
        return number

    if read > 50 and read < 60 or read == 60:
        number = 0.16
        return number

    if read > 60 and read < 70 or read == 70:
        number = 0.25
        return number

    if read > 70 and read < 80 or read == 80:
        number = 0.35
        return number

    if read > 80 and read < 90 or read == 90:
        number = 0.45
        return number

    if read > 90 and read < 100 or read == 100:
        number = 0.5
        return number
def sc():
    pm = pymem.Pymem("csgo.exe")
    appdata_p = os.environ['AppData']
    file = '%s\\CheatX\\cheatx-private\\settings\\sc\\tr.cfg' % (appdata_p)


    set = get_value()
    print(set)
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    while True:
        check_t = os.path.isfile(file)
        if check_t == False:
            break
        mouse4 = win32api.GetKeyState(0x01)
        if mouse4 < 0:
            pm.write_int(client + dwForceAttack, 6)

        time.sleep(set)

def start_sc():
    threading.Thread(target=sc, daemon=True).start()