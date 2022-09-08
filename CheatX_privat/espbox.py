import sys
from pymeow import *
from requests import get
import os
import matplotlib.colors as colors
from PyQt5.QtWidgets import QColorDialog
from random import *
from string import ascii_uppercase
import pymem



offsets = 'https://raw.githubusercontent.com/kadeeq/ProjectX/main/offsets/offsets.json'
response = get( offsets ).json()
bhop_taste = "space"
m_iCompetitiveWins = int(response["netvars"]["m_iCompetitiveWins"])
dwEntityList = int( response["signatures"]["dwEntityList"] )
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

appdata_p = os.environ['AppData']

class Offsets:
    pass


def enemy():
    pm = pymem.Pymem("csgo.exe")

    client = pymem.process.module_from_name( pm.process_handle, "client.dll" ).lpBaseOfDll
    for i in range(1, 32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)
        if entity:
            entity_team_id = pm.read_int(entity + m_iTeamNum)
            print(entity_team_id)
            if entity_team_id == 2:
                print(1231231)
            elif entity_team_id == 3:
                print(9090)

class Colors:
    white = rgb("white")
    black = rgb("black")
    blue = rgb("blue")
    red = rgb("red")
    cyan = rgb("cyan")
    orange = rgb("orange")
    silver = rgb("silver")
    chooser = (rgb("orange"))
    inv = 255, 255, 255, .4



class Entity:
    def __init__(self, addr, mem, gmod):
        self.wts = None
        self.addr = addr
        self.mem = mem
        self.gmod = gmod

        self.id = read_int(self.mem, self.addr + 0x64)
        self.health = read_int(self.mem, self.addr + Offsets.m_iHealth)
        self.dormant = read_int(self.mem, self.addr + Offsets.m_bDormant)
        self.team = read_int(self.mem, self.addr + Offsets.m_iTeamNum)
        self.bone_base = read_int(self.mem, self.addr + Offsets.m_dwBoneMatrix)
        self.pos = read_vec3(self.mem, self.addr + Offsets.m_vecOrigin)

    @property
    def name(self):
        radar_base = read_int(self.mem, self.gmod + Offsets.dwRadarBase)
        hud_radar = read_int(self.mem, radar_base + 0x78)
        return read_string(self.mem, hud_radar + 0x300 + (0x174 * (self.id - 1)))

    def bone_pos(self, bone_id):
        return vec3(
            read_float(self.mem, self.bone_base + 0x30 * bone_id + 0x0C),
            read_float(self.mem, self.bone_base + 0x30 * bone_id + 0x1C),
            read_float(self.mem, self.bone_base + 0x30 * bone_id + 0x2C),
        )

    def glow(self):
        """
        Should be used in a thread.
        """
        glow_addr = (
            read_int(self.mem, self.gmod + Offsets.dwGlowObjectManager)
            + read_int(self.mem, self.addr + Offsets.m_iGlowIndex) * 0x38
        )

        color = Colors.cyan if self.team != 2 else Colors.orange
        write_floats(self.mem, glow_addr + 4, color + [1.5])
        write_bytes(self.mem, glow_addr + 0x24, [1, 0])


def trigger_bot(mem, local, ent):
    cross = read_int(mem, local.addr + Offsets.m_iCrosshairId)
    if cross == ent.id and ent.team != local.team:
        print(ent.team)
        return ent.team



def esp_box1():
    try:
        # Credits to https://github.com/frk1/hazedumper
        haze = get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()

        [setattr(Offsets, k, v) for k, v in haze["signatures"].items()]
        [setattr(Offsets, k, v) for k, v in haze["netvars"].items()]
    except:
        sys.exit("Unable to fetch Hazedumper's Offsets")

    csgo_proc = process_by_name("csgo.exe")
    game_module = csgo_proc["modules"]["client.dll"]["baseaddr"]
    overlay = overlay_init() # Windowed Fullscreen
    font = font_init(10, "Tahoma")
    set_foreground("Counter-Strike: Global Offensive")

    while overlay_loop(overlay):
        try:
            local_player_addr = read_int(csgo_proc, game_module + Offsets.dwLocalPlayer)
            local_ent = Entity(local_player_addr, csgo_proc, game_module)
        except:
            # No local player
            continue

        # files
        file_box = os.path.isfile('%s\\CheatX\\cheatx-private\\settings\\eb\\tr.cfg' % (appdata_p))
        file_hp = os.path.isfile('%s\\CheatX\\cheatx-private\\settings\\eh\\tr.cfg' % (appdata_p))
        file_line = os.path.isfile('%s\\CheatX\\cheatx-private\\settings\\l\\tr.cfg' % (appdata_p))
        file_name = os.path.isfile('%s\\CheatX\\cheatx-private\\settings\\nm\\tr.cfg' % (appdata_p))
        if file_box == False:
            if file_hp == False:
                if file_line == False:
                    if file_name == False:
                        break
        if local_player_addr:
            ent_addrs = read_ints(csgo_proc, game_module + Offsets.dwEntityList, 128)[0::4]
            view_matrix = read_floats(csgo_proc, game_module + Offsets.dwViewMatrix, 16)
            for ent_addr in ent_addrs:
                if ent_addr > 0 and ent_addr != local_player_addr:
                    ent = Entity(ent_addr, csgo_proc, game_module)
                    if not ent.dormant and ent.health > 0:
                        try:
                            if file_box == True:
                                trigger_bot(csgo_proc, local_ent, ent)
                                ent.wts = wts_dx(overlay, view_matrix, ent.pos)
                                # ent.glow()
                                head_pos = wts_dx(overlay, view_matrix, ent.bone_pos(8))
                                head = head_pos["y"] - ent.wts["y"]
                                width = head / 2
                                center = width / -2
                                # бокс
                                if ent.team == 2:
                                    print(ent.team)
                                    corner_box(
                                        ent.wts["x"] + center,
                                        ent.wts["y"],
                                        width,
                                        head + 30,
                                        Colors.chooser if ent.team == 2 else Colors.cyan,
                                        Colors.black,
                                        0.15,
                                    )
                                if ent.team != 2:
                                    print(ent.team)
                                    corner_box(
                                        ent.wts["x"] + center,
                                        ent.wts["y"],
                                        width,
                                        head + 30,
                                        Colors.cyan if ent.team == 3 else Colors.chooser,
                                        Colors.black,
                                        0.15,
                                    )
                            if file_hp == True:
                                # здоровье
                                ent.wts = wts_dx(overlay, view_matrix, ent.pos)
                                head_pos = wts_dx(overlay, view_matrix, ent.bone_pos(8))
                                head = head_pos["y"] - ent.wts["y"]
                                width = head / 2
                                center = width / -2
                                if os.path.isfile('tr.txt'):
                                    value_bar(
                                        ent.wts["x"] + center - 5,
                                        ent.wts["y"],
                                        ent.wts["x"] + center - 5,
                                        head_pos["y"] + 5,
                                        2,
                                        100, ent.health if ent.team == 2 else 100
                                    )
                                if not os.path.isfile('tr.txt'):
                                    value_bar(
                                        ent.wts["x"] + center - 5,
                                        ent.wts["y"],
                                        ent.wts["x"] + center - 5,
                                        head_pos["y"] + 5,
                                        2,
                                        100, ent.health if ent.team == 2 else 100
                                    )
                            if file_name == True:
                                # имя
                                font_print(
                                    font,
                                    ent.wts["x"] - len(ent.name) * 1.5,
                                    ent.wts["y"] - 10,
                                    ent.name,
                                    Colors.white,
                                )
                            if file_line == True:
                                # дистанция
                                font_print(
                                    font,
                                    ent.wts["x"] - 2,
                                    ent.wts["y"] - 20,
                                    str(int(vec3_distance(ent.pos, local_ent.pos) / 20)),
                                    Colors.white,
                                )
                        except:
                            pass

    overlay_deinit(overlay)



