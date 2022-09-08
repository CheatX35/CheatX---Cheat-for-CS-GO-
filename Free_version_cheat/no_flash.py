import pymem
import pymem.process
import requests
import threading
from time import sleep
import os

offsets = 'https://raw.githubusercontent.com/kadeeq/ProjectX/main/offsets/offsets.json'
response = requests.get( offsets ).json()


dwLocalPlayer = int( response["signatures"]["dwLocalPlayer"] )
m_flFlashMaxAlpha = int( response["netvars"]["m_flFlashMaxAlpha"] )

def no_flash():
    appdata_p = os.environ['AppData']
    file = '%s\\CheatX\\cheatx-free\\settings\\n\\tr.cfg' % (appdata_p)
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    check_1 = os.path.isfile(file)
    player = pm.read_int( client + dwLocalPlayer )
    flash_value = player + m_flFlashMaxAlpha
    if check_1 == False:
        if flash_value:
            pm.write_float(flash_value, float(250))
    if check_1 == True:
        if flash_value:
            pm.write_float(flash_value, float(0))

def start_no_flash():
    threading.Thread(target=no_flash, daemon=True).start()