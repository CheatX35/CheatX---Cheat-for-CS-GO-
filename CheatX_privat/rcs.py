def RCS(process, client, clientState):
    oldAimPunchX = 0  # Initializing var (going to be used to store the last aimPunchX)
    oldAimPunchY = 0  # Initializing var (going to be used to store the last aimPunchY)
    global RCSPerfectPercent  # Defines how much RCS we are gonna do

    while True:
        if win32gui.GetForegroundWindow() == csgoWindow and read(process, (
                    clientState + getOffset(config,'clientStateInGameOffset'))) == 6:  # If we are actually playing in game
            localPlayer = read(process, (client + getOffset(config,'localPlayerOffset')))  # Get the localPlayer
            if read(process, (localPlayer + getOffset(config,'shotsFiredOffset'))) > 1:  # If we have fired more than 1 shots
                viewAngleX = read(process, (clientState + getOffset(config,'clientStateViewAnglesOffset')), 'float')  # Get the X viewAngle
                viewAngleY = read(process, (clientState + getOffset(config,'clientStateViewAnglesOffset') + 0x4),
                                  'float')  # Get the Y viewAngle

                aimPunchX = read(process, (localPlayer + getOffset(config,'aimPunchOffset')), 'float')  # Get the X aimPunch
                aimPunchY = read(process, (localPlayer + getOffset(config,'aimPunchOffset') + 0x4), 'float')  # Get the Y aimPunch

                viewAngleX -= (aimPunchX - oldAimPunchX) * (
                    RCSPerfectPercent * 0.02)  # Subtract our AimPunch from our ViewAngle
                viewAngleY -= (aimPunchY - oldAimPunchY) * (
                    RCSPerfectPercent * 0.02)  # Subtract our AimPunch from our ViewAngle

                viewAngleX, viewAngleY = normalizeAngles(viewAngleX, viewAngleY)  # Normalize our ViewAngles

                write(process, (clientState + getOffset(config,'clientStateViewAnglesOffset')), viewAngleX, 'float')
                write(process, (clientState + getOffset(config,'clientStateViewAnglesOffset') + 0x4), viewAngleY, 'float')

                oldAimPunchX = aimPunchX
                oldAimPunchY = aimPunchY
            else:
                oldAimPunchX = 0
                oldAimPunchY = 0
        time.sleep(0.1)
