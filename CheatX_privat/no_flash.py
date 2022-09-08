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

import pymem
import pymem.process
import time




def main():
    print("Emerald has launched.")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(0))
                print(11)
        time.sleep(1)


if __name__ == '__main__':
    main()