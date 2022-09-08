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
import os

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
antivac = "foqnmwordqowjm333q3q3q3q5q4q3"
print(antivac)
print(antivacv2)

user32 = ctypes.windll.user32


def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex

    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey


def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY


def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True


def nanchecker(first, second):
    if isnan( first ) or isnan( second ):
        return False
    else:
        return True


def Distance(src_x, src_y, src_z, dst_x, dst_y, dst_z):
    try:
        diff_x = src_x - dst_x
        diff_y = src_y - dst_y
        diff_z = src_z - dst_z
        return sqrt( diff_x * diff_x + diff_y * diff_y + diff_z * diff_z )
    except:
        pass


def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    try:
        delta_x = localpos1 - enemypos1
        delta_y = localpos2 - enemypos2
        delta_z = localpos3 - enemypos3
        hyp = sqrt( delta_x * delta_x + delta_y * delta_y + delta_z * delta_z )
        x = asin( delta_z / hyp ) * 57.295779513082
        y = atan( delta_y / delta_x ) * 57.295779513082
        if delta_x >= 0.0:
            y += 180.0
    except:
        return 0,0
    return x, y






appdata_p = os.environ['AppData']
rcse = True
file = '%s\\CheatX\\cheatx-free\\settings\\r\\tr.cfg' % (appdata_p)
def rcs():

        pm = pymem.Pymem( "csgo.exe" )
        client = pymem.process.module_from_name( pm.process_handle, "client.dll" ).lpBaseOfDll
        engine = pymem.process.module_from_name( pm.process_handle, "engine.dll" ).lpBaseOfDll
        player = pm.read_int( client + dwLocalPlayer )
        engine_pointer = pm.read_int( engine + dwClientState )
        oldpunchx = 0.0
        oldpunchy = 0.0
        while True:
            if rcse:
                check_1 = os.path.isfile(file)
                if not check_1 == True:
                    break
                if pm.read_int( player + m_iShotsFired ) > 2:
                    rcs_x = pm.read_float( engine_pointer + dwClientState_ViewAngles )
                    rcs_y = pm.read_float( engine_pointer + dwClientState_ViewAngles + 0x4 )
                    punchx = pm.read_float( player + m_aimPunchAngle )
                    punchy = pm.read_float( player + m_aimPunchAngle + 0x4 )
                    newrcsx = rcs_x - (punchx - oldpunchx) * 2
                    newrcsy = rcs_y - (punchy - oldpunchy) * 2
                    oldpunchx = punchx
                    oldpunchy = punchy
                    if nanchecker( newrcsx, newrcsy ) and checkangles( newrcsx, newrcsy ):
                        pm.write_float( engine_pointer + dwClientState_ViewAngles, newrcsx )
                        pm.write_float( engine_pointer + dwClientState_ViewAngles + 0x4, newrcsy )
                else:
                    oldpunchx = 0.0
                    oldpunchy = 0.0
                    newrcsx = 0.0
                    newrcsy = 0.0


def start_rcs():
    threading.Thread(target=rcs, daemon=True).start()