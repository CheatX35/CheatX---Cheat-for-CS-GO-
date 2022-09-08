#esp

import time
import threading
import keyboard
import pymem
import pymem.process
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from math import *
import ctypes
import random
from random import choice
from string import ascii_uppercase
import matplotlib.colors as colors
import os
from PyQt5.QtWidgets import QColorDialog



offsets = 'https://raw.githubusercontent.com/kadeeq/ProjectX/main/offsets/offsets.json'
response = requests.get( offsets ).json()
bhop_taste = "space"
m_iCompetitiveWins = int(response["netvars"]["m_iCompetitiveWins"])
dwEntityList = int( response["signatures"]["dwEntityList"] )
dwGlowObjectManager = int( response["signatures"]["dwGlowObjectManager"] )
m_iGlowIndex = int( response["netvars"]["m_iGlowIndex"] )
m_iTeamNum = int( response["netvars"]["m_iTeamNum"] )
dwForceJump = int( response["signatures"]["dwForceJump"] )
dwLocalPlayer = int( response["signatures"]["dwLocalPlayer"] )
m_fFlags = int( response["netvars"]["m_fFlags"] )
dwForceAttack = int( response["signatures"]["dwForceAttack"] )
m_iCrosshairId = int( response["netvars"]["m_iCrosshairId"] )
m_flFlashMaxAlpha = int( response["netvars"]["m_flFlashMaxAlpha"] )
m_iDefaultFOV = (0x332C)
dwClientState = int( response["signatures"]["dwClientState"] )
m_iHealth = int( response["netvars"]["m_iHealth"] )
dwViewMatrix = int( response["signatures"]["dwViewMatrix"] )
m_dwBoneMatrix = int( response["netvars"]["m_dwBoneMatrix"] )
dwClientState_ViewAngles = int( response["signatures"]["dwClientState_ViewAngles"] )
m_vecOrigin = int( response["netvars"]["m_vecOrigin"] )
m_vecViewOffset = int( response["netvars"]["m_vecViewOffset"] )
dwbSendPackets = int( response["signatures"]["dwbSendPackets"] )
dwInput = int( response["signatures"]["dwInput"] )
clientstate_net_channel = int( response["signatures"]["clientstate_net_channel"] )
clientstate_last_outgoing_command = int( response["signatures"]["clientstate_last_outgoing_command"] )
m_bSpotted = int( response["netvars"]["m_bSpotted"] )
m_iShotsFired = int( response["netvars"]["m_iShotsFired"] )
m_aimPunchAngle = int( response["netvars"]["m_aimPunchAngle"] )
m_bGunGameImmunity = int( response["netvars"]["m_bGunGameImmunity"] )
m_bIsDefusing = int( response["netvars"]["m_bIsDefusing"] )
m_bDormant = int( response["signatures"]["m_bDormant"] )
dwClientState_PlayerInfo = int( response["signatures"]["dwClientState_PlayerInfo"] )
dwPlayerResource = int( response["signatures"]["dwPlayerResource"] )
m_iCompetitiveRanking = int( response["netvars"]["m_iCompetitiveRanking"] )
eteam = False
antivacv2 = random.randint(1,100)

rnd_text = ''.join(choice(ascii_uppercase) for x in range(100))
rnd_text_settings_esp_color = ''.join(choice(ascii_uppercase) for p in range(10))
rnd_text_settings_true_choose = ''.join(choice(ascii_uppercase) for p in range(10))

antivac = rnd_text
print(antivac)
print(antivacv2)


user32 = ctypes.windll.user32

appdata_p = os.environ['AppData']
def color_choose():
    color = QColorDialog.getColor()
    if color.isValid():
        print(color.name())
        color_esp = color.name()
        appdata_p = os.environ['AppData']
        file = '%s\\CheatX\\cheatx-free\\settings\\%s' % (appdata_p, rnd_text_settings_esp_color + '.cfg')
        write_color_settings = open(file, 'w')
        write_color_settings.write(color_esp)
        write_color_settings.close()
    else:
        color_esp = '1.0'
        appdata_p = os.environ['AppData']
        file = '%s\\CheatX\\cheatx-free\\settings\\%s' % (appdata_p, rnd_text_settings_esp_color + '.cfg')
        write_color_settings = open(file, 'w')
        write_color_settings.write(color_esp)
        write_color_settings.close()
        file_settings_true_choose = '%s\\CheatX\\cheatx-free\\settings\\%s' % (appdata_p, rnd_text_settings_true_choose + '.cfg')






def GetWindowText(handle, length=100):

    window_text = ctypes.create_string_buffer(length)
    user32.GetWindowTextA(
        handle,
        ctypes.byref(window_text),
        length
    )

    return window_text.value


def GetForegroundWindow():

    return user32.GetForegroundWindow()

whc = True
def esp():
        # getting color esp
        file_color_esp = '%s\\CheatX\\cheatx-free\\settings\\%s' % (appdata_p, rnd_text_settings_esp_color + '.cfg')
        file_check = os.path.isfile(file_color_esp)
        file = '%s\\CheatX\\cheatx-free\\settings\\e\\tr.cfg' % (appdata_p)
        if file_check == True:
            file_esp = open(file_color_esp)
            read_esp_color = file_esp.read()
            print(read_esp_color)
            if read_esp_color == '1.0':
                color = 1.0
                color_1 = 1
                color_2 = 0
                color_3 = 0
            else:
                color = colors.hex2color(read_esp_color)
                color_1 = color[0]
                color_2 = color[1]
                color_3 = color[2]
                print(color_1)
                print(color_2)
                print(color_3)
        elif file_check == False:
            color_1 = 1.0
            color_2 = 0
            color_3 = 0

        pm = pymem.Pymem( "csgo.exe" )
        client = pymem.process.module_from_name( pm.process_handle, "client.dll" ).lpBaseOfDll
        engine = pymem.process.module_from_name( pm.process_handle, "engine.dll" ).lpBaseOfDll
        player = pm.read_int( client + dwLocalPlayer )
        engine_pointer = pm.read_int( engine + dwClientState )
        oldpunchx = 0.0
        oldpunchy = 0.0
        while True:

            check_1 = os.path.isfile(file)
            if not check_1 == True:
                break

            if not GetWindowText(GetForegroundWindow()).decode('cp1252') == "Counter-Strike: Global Offensive":
                time.sleep(1)
                continue

            pm.write_uchar( engine + dwbSendPackets, 1 )
            target = None
            olddistx = 111111111111
            olddisty = 111111111111
            if client and engine and pm:
                try:
                    player = pm.read_int( client + dwLocalPlayer )
                    engine_pointer = pm.read_int( engine + dwClientState )
                    glow_manager = pm.read_int( client + dwGlowObjectManager )
                    crosshairID = pm.read_int( player + m_iCrosshairId )
                    getcrosshairTarget = pm.read_int( client + dwEntityList + (crosshairID - 1) * 0x10 )
                    immunitygunganme = pm.read_int( getcrosshairTarget + m_bGunGameImmunity )
                    localTeam = pm.read_int( player + m_iTeamNum )
                    crosshairTeam = pm.read_int( getcrosshairTarget + m_iTeamNum )
                except:
                    print( "Round not started yet" )
                    time.sleep( 5 )
                    continue

            for i in range( 1, 64 ):
                entity = pm.read_int( client + dwEntityList + i * 0x10 )

                if entity:
                    try:
                        entity_glow = pm.read_int( entity + m_iGlowIndex )
                        entity_team_id = pm.read_int( entity + m_iTeamNum )
                        entity_isdefusing = pm.read_int( entity + m_bIsDefusing )
                        entity_hp = pm.read_int( entity + m_iHealth )
                        entity_dormant = pm.read_int( entity + m_bDormant )
                    except:
                        print( "Could not load Players Infos (Should only do this once)" )
                        time.sleep( 2 )
                        continue

                    if entity_hp > 50:
                        if color_1 > 0 and color_2 > 0 and color_3 > 0:
                            if color_1 > color_2 and color_2 > color_3:
                                r, g, b = float(1), float(1), float(0)
                            elif color_1 > color_2 and color_2 < color_3:
                                r, g, b = float(1), float(0), float(1)
                            elif color_1 > color_3 and color_3 > color_2:
                                r, g, b = float(1), float(0), float(1)
                            elif color_2 > color_1 and color_1 > color_3:
                                r, g, b = float(0), float(1), float(1)
                            elif color_2 > color_1 and color_1 < color_3:
                                r, g, b = float(0), float(1), float(1)
                            elif color_2 > color_3 and color_3 > color_1:
                                r, g, b = float(0), float(1), float(1)
                            elif color_3 > color_1 and color_1 > color_2:
                                r, g, b = float(1), float(0), float(1)
                            elif color_3 > color_1 and color_1 < color_2:
                                r, g, b = float(0), float(1), float(1)
                            elif color_3 > color_2 and color_2 > color_1:
                                r, g, b = float(0), float(1), float(1)
                            elif color_3 > color_1 and color_1 < color_2:
                                r, g, b = float(0), float(1), float(1)
                        else:
                            r, g, b = float(color_1), float(color_2), float(color_3)
                    elif entity_hp < 50:
                        if color_1 > 0 and color_2 > 0 and color_3 > 0:
                            if color_1 > color_2 and color_2 > color_3:
                                r, g, b = float(1), float(1), float(0)
                            elif color_1 > color_2 and color_2 < color_3:
                                r, g, b = float(1), float(0), float(1)
                            elif color_1 > color_3 and color_3 > color_2:
                                r, g, b = float(1), float(0), float(1)
                            elif color_2 > color_1 and color_1 > color_3:
                                r, g, b = float(0), float(1), float(1)
                            elif color_2 > color_1 and color_1 < color_3:
                                r, g, b = float(0), float(1), float(1)
                            elif color_2 > color_3 and color_3 > color_1:
                                r, g, b = float(0), float(1), float(1)
                            elif color_3 > color_1 and color_1 > color_2:
                                r, g, b = float(1), float(0), float(1)
                            elif color_3 > color_1 and color_1 < color_2:
                                r, g, b = float(0), float(1), float(1)
                            elif color_3 > color_2 and color_2 > color_1:
                                r, g, b = float(0), float(1), float(1)
                            elif color_3 > color_1 and color_1 > color_2:
                                r, g, b = float(0), float(1), float(1)


                    #elif entity_hp < 50:
                       # r, g, b = float(color_1), float(color_2), float(color_3)
                    #elif entity_hp == 100 and entity_team_id == 2:
                        #r, g, b = float(color_1), float(color_2), float(color_3)
                    #else:
                        #r, g, b = float(color_1), float(color_2), float(color_3)

                    if whc and entity_team_id == 2 and (
                            eteam or localTeam != 2) and not entity_dormant:  # Terrorist Glow
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float( r ) )  # R
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float( g ) )  # G
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float( b ) )  # B
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0x14, float( 255 ) )  # A

                        pm.write_int( glow_manager + entity_glow * 0x38 + 0x28, 1 )  # Enable


                    elif whc and entity_team_id == 3 and (
                            eteam or localTeam != 3) and not entity_dormant:  # Anti Glow
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float( r ) )  # R
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float( g ) )  # G
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float( b ) )  # B
                        pm.write_float( glow_manager + entity_glow * 0x38 + 0x14, float( 255 ) )  # A

                        pm.write_int( glow_manager + entity_glow * 0x38 + 0x28, 1 )  # Enable

                    else:
                        pass



def start_esp():
    threading.Thread(target=esp, daemon=True).start()