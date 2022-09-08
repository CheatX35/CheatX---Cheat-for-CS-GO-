import ctypes
import requests 
import keyboard
import pymem
import pymem.process
import time
from win32gui import GetWindowText, GetForegroundWindow
from win32gui import FindWindow, GetWindowRect
import os
import threading

offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(offsets).json()

dwEntityList = int(response["signatures"]["dwEntityList"])
dwForceAttack = int(response["signatures"]["dwForceAttack"])
dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
m_fFlags = int(response["netvars"]["m_fFlags"])
m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])


appdata_p = os.environ['AppData']


def trig():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    trig_key = open('%s\\CheatX\\cheatx-free\\settings\\t_k.cfg' % (appdata_p))
    read_key = trig_key.read()
    trigger_key = read_key

    file_work = '%s\\CheatX\\cheatx-free\\settings\\t\\tr.cfg' % (appdata_p)
    print(" Sapphire has launched.")
    while True:
        check_1 = os.path.isfile(file_work)
        if check_1 == False:
            break
        if not keyboard.is_pressed(trigger_key):
            time.sleep(0.001)

        if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
            continue

        if keyboard.is_pressed(trigger_key):
            if check_1 == False:
                break
            player = pm.read_int(client + dwLocalPlayer)
            entity_id = pm.read_int(player + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

            entity_team = pm.read_int(entity + m_iTeamNum)
            player_team = pm.read_int(player + m_iTeamNum)

            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                pm.write_int(client + dwForceAttack, 6)

            time.sleep(0.006)

def start_trigger():
    threading.Thread(target=trig, daemon=True).start()
