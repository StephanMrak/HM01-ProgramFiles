
def main():
    global mausx, mausy, xHit, iPoints, xReset, iCountRound, Biathlon_tmpScore, xBiathlon, iRound
    import pygame
    import time
    import hmsysteme
    import os
    import platform
    import pygame.freetype
    hmsysteme.put_button_names(["10m Pistole", "10m Gewehr", "15m Gewehr", "Biathlon", "Back", "Reset", "BlindShot"])
    print(platform.uname())
    # some colors to use
    BLACK = (0, 0, 0)
    FIREARMS = (80,80,80)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 191, 255)
    RED = (255, 0, 0)
    HIMMELBLAU = (120, 210, 255)
    YELLOW = (255, 255, 0)
    iBackgroundAnimation = 0
    framerate = 30
    frames = 0
    # Pygame init
    pygame.init()
    Players = []
    offsetDiabolo = 9
    xHit = False
    iPoints = 0
    xReset = False
    go = True
    xIntro = True
    xPistol10m = False
    xRifle10m = False
    xRifle15m = False
    xBackbutton = False
    xBiathlon = False
    Biathlon_tmpScore = [False, False, False, False, False]
    iGetAction = 0
    mausx = 0
    mausy = 0

    iCountRound = 2
    iRound = 0

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #size = [1366, 768]
    size = hmsysteme.get_size()
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    names = hmsysteme.get_playernames()
    if not names:
        names = ["Stephan", "Marion", "Flori", "Peter Mafai"]

    path = os.path.realpath(__file__)
    print(path)

    if 'Linux' in platform.uname():
        path = path.replace('Scheiben.py', '')
    else:
        path = path.replace('Scheiben.py', '')

    screen = pygame.display.set_mode(size)
    #screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    pygame.display.set_caption("Scheiben")

    sPfad = "C:/Users/flori"
    #"C:/Users/fs_sl"
    #"C:/Users/flori"

    #Bilder
    #Rifle 10m
    pic_Scheibe_rifle10m = [pygame.image.load(os.path.join(path, "pics/Scheibe/Rifle_10m/Kreis1.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis2.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis3.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis4.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis5.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis6.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis7.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis8.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis9.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Kreis10.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_10m/Reckteck.png"))]
    pic_Rifle = pygame.image.load(os.path.join(path,"pics/Scheibe/gewehr10m.png"))
    pic_Rifle_scale = pygame.transform.scale(pic_Rifle, (170,56))
    pic_pickrifle10m = pygame.image.load(os.path.join(path,"pics/Scheibe/gewehr10mw.png"))
    pic_pickrifle10m_sc = pygame.transform.scale(pic_pickrifle10m, (200,65))

    #Rifle 15m
    pic_Scheibe_rifle15m = [pygame.image.load(os.path.join(path, "pics/Scheibe/Rifle_15m/Kreis1.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis2.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis3.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis4.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis5.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis6.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis7.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis8.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis9.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Kreis10.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Rifle_15m/Rechteck.png"))]
    pic_Rifle15m = pygame.image.load(os.path.join(path,"pics/Scheibe/gewehr15m.png"))
    pic_Rifle15m_scale = pygame.transform.scale(pic_Rifle15m, (170,56))
    pic_pickrifle15m = pygame.image.load(os.path.join(path,"pics/Scheibe/gewehr15mw.png"))
    pic_pickrifle15m_sc = pygame.transform.scale(pic_pickrifle15m, (200,65))

    #Pistol 10m
    pic_Scheibe_pistol10m = [pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis1.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis2.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis3.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis4.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis5.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis6.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis7.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis8.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis9.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Kreis10.png")),
                   pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/Rechteck.png"))]
    pic_Pistol = pygame.image.load(os.path.join(path,"pics/Scheibe/Pistol_10m/pistol.png"))
    pic_Pistol_scale = pygame.transform.scale(pic_Pistol, (100,95))
    pic_pickpistol10m = pygame.image.load(os.path.join(path,"pics/Scheibe/pistolw.png"))
    pic_pickpistol10m_sc = pygame.transform.scale(pic_pickpistol10m, (100,85))
    pic_backbutton = pygame.image.load(os.path.join(path,"pics/Background/Scheiben/back_button.png"))
    pic_backbutton_scale = pygame.transform.scale(pic_backbutton, (100,40))
    pic_ButtonBlindShot = pygame.image.load(os.path.join(path,"pics/Background/Scheiben/Blindshot.png"))
    pic_ButtonBlindShot_scale = pygame.transform.scale(pic_ButtonBlindShot, (100,66))
    pic_ButtonReset = pygame.image.load(os.path.join(path, "pics/Background/Scheiben/reset_button.png"))
    pic_ButtonReset_scale = pygame.transform.scale(pic_ButtonReset, (100, 38))

    #Biathlon
    pic_Biathlon = pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Biathlon.png"))
    pic_Biathlon_sc = pygame.transform.scale(pic_Biathlon, (100,146))
    """
    pic_Biathlon_scheiben = [pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/1.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/2.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/3.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/4.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/5.png"))]
    pic_Biathlon_target = [pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/11.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/21.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/31.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/41.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/51.png"))]
    pic_Biathlon_Rechteck = pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Rechteck.png"))
    """
    #!!!!!!!!!Scheiben Schwer!!!!!!########
    pic_Biathlon_scheiben = [pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Schwer/1.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Schwer/2.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Schwer/3.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Schwer/4.png")),
                    pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Schwer/5.png"))]
    pic_Biathlon_target = [pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/Schwer/11.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/Schwer/21.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/Schwer/31.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/Schwer/41.png")),
                    pygame.image.load(os.path.join(path, "pics/Scheibe/Biathlon/Schwer/51.png"))]
    pic_Biathlon_Rechteck = pygame.image.load(os.path.join(path,"pics/Scheibe/Biathlon/Schwer/Rechteck.png"))

#Create Masks
    #pistol 10m
    Mask_Pistol10m_1 = pygame.mask.from_surface(pic_Scheibe_pistol10m[0])
    Mask_Pistol10m_2 = pygame.mask.from_surface(pic_Scheibe_pistol10m[1])
    Mask_Pistol10m_3 = pygame.mask.from_surface(pic_Scheibe_pistol10m[2])
    Mask_Pistol10m_4 = pygame.mask.from_surface(pic_Scheibe_pistol10m[3])
    Mask_Pistol10m_5 = pygame.mask.from_surface(pic_Scheibe_pistol10m[4])
    Mask_Pistol10m_6 = pygame.mask.from_surface(pic_Scheibe_pistol10m[5])
    Mask_Pistol10m_7 = pygame.mask.from_surface(pic_Scheibe_pistol10m[6])
    Mask_Pistol10m_8 = pygame.mask.from_surface(pic_Scheibe_pistol10m[7])
    Mask_Pistol10m_9 = pygame.mask.from_surface(pic_Scheibe_pistol10m[8])
    Mask_Pistol10m_10 = pygame.mask.from_surface(pic_Scheibe_pistol10m[9])
    Mask_Pistol10m_0 = pygame.mask.from_surface(pic_Scheibe_pistol10m[10])
    #rifle 10m
    Mask_rifle10m_1 = pygame.mask.from_surface(pic_Scheibe_rifle10m[0])
    Mask_rifle10m_2 = pygame.mask.from_surface(pic_Scheibe_rifle10m[1])
    Mask_rifle10m_3 = pygame.mask.from_surface(pic_Scheibe_rifle10m[2])
    Mask_rifle10m_4 = pygame.mask.from_surface(pic_Scheibe_rifle10m[3])
    Mask_rifle10m_5 = pygame.mask.from_surface(pic_Scheibe_rifle10m[4])
    Mask_rifle10m_6 = pygame.mask.from_surface(pic_Scheibe_rifle10m[5])
    Mask_rifle10m_7 = pygame.mask.from_surface(pic_Scheibe_rifle10m[6])
    Mask_rifle10m_8 = pygame.mask.from_surface(pic_Scheibe_rifle10m[7])
    Mask_rifle10m_9 = pygame.mask.from_surface(pic_Scheibe_rifle10m[8])
    Mask_rifle10m_10 = pygame.mask.from_surface(pic_Scheibe_rifle10m[9])
    Mask_rifle10m_0 = pygame.mask.from_surface(pic_Scheibe_rifle10m[10])
    #rifle 15m
    Mask_rifle15m_1 = pygame.mask.from_surface(pic_Scheibe_rifle15m[0])
    Mask_rifle15m_2 = pygame.mask.from_surface(pic_Scheibe_rifle15m[1])
    Mask_rifle15m_3 = pygame.mask.from_surface(pic_Scheibe_rifle15m[2])
    Mask_rifle15m_4 = pygame.mask.from_surface(pic_Scheibe_rifle15m[3])
    Mask_rifle15m_5 = pygame.mask.from_surface(pic_Scheibe_rifle15m[4])
    Mask_rifle15m_6 = pygame.mask.from_surface(pic_Scheibe_rifle15m[5])
    Mask_rifle15m_7 = pygame.mask.from_surface(pic_Scheibe_rifle15m[6])
    Mask_rifle15m_8 = pygame.mask.from_surface(pic_Scheibe_rifle15m[7])
    Mask_rifle15m_9 = pygame.mask.from_surface(pic_Scheibe_rifle15m[8])
    Mask_rifle15m_10 = pygame.mask.from_surface(pic_Scheibe_rifle15m[9])
    Mask_rifle15m_0 = pygame.mask.from_surface(pic_Scheibe_rifle15m[10])
    #Biathlon
    Mask_Bia_1 = pygame.mask.from_surface(pic_Biathlon_scheiben[0])
    Mask_Bia_2 = pygame.mask.from_surface(pic_Biathlon_scheiben[1])
    Mask_Bia_3 = pygame.mask.from_surface(pic_Biathlon_scheiben[2])
    Mask_Bia_4 = pygame.mask.from_surface(pic_Biathlon_scheiben[3])
    Mask_Bia_5 = pygame.mask.from_surface(pic_Biathlon_scheiben[4])

    # Variablen init
    Players = []

    class Player:
        def __init__(self, name):
            self.name = name
            self.score = 0
            self.score_Biathlon = 0


    def Evaluation():
        global iPoints, xHit, Biathlon_tmpScore, xBiathlon, mausx, mausy
        xHit = True
        #Create Mask
        offset_Mask = ((mausx - offsetDiabolo), int(mausy - offsetDiabolo))
        # target evaluation pistol 10m
        if xPistol10m:
            if Mask_Pistol10m_10.overlap(MaskDiabolo, offset_Mask):
                iPoints = 10
            elif Mask_Pistol10m_9.overlap(MaskDiabolo, offset_Mask):
                iPoints = 9
            elif Mask_Pistol10m_8.overlap(MaskDiabolo, offset_Mask):
                iPoints = 8
            elif Mask_Pistol10m_7.overlap(MaskDiabolo, offset_Mask):
                iPoints = 7
            elif Mask_Pistol10m_6.overlap(MaskDiabolo, offset_Mask):
                iPoints = 6
            elif Mask_Pistol10m_5.overlap(MaskDiabolo, offset_Mask):
                iPoints = 5
            elif Mask_Pistol10m_4.overlap(MaskDiabolo, offset_Mask):
                iPoints = 4
            elif Mask_Pistol10m_3.overlap(MaskDiabolo, offset_Mask):
                iPoints = 3
            elif Mask_Pistol10m_2.overlap(MaskDiabolo, offset_Mask):
                iPoints = 2
            elif Mask_Pistol10m_1.overlap(MaskDiabolo, offset_Mask):
                iPoints = 1
            elif Mask_Pistol10m_0.overlap(MaskDiabolo, offset_Mask):
                iPoints = 0
        # target evaluation rifle 10m
        if xRifle10m:
            if Mask_rifle10m_10.overlap(MaskDiabolo, offset_Mask):
                iPoints = 10
            elif Mask_rifle10m_9.overlap(MaskDiabolo, offset_Mask):
                iPoints = 9
            elif Mask_rifle10m_8.overlap(MaskDiabolo, offset_Mask):
                iPoints = 8
            elif Mask_rifle10m_7.overlap(MaskDiabolo, offset_Mask):
                iPoints = 7
            elif Mask_rifle10m_6.overlap(MaskDiabolo, offset_Mask):
                iPoints = 6
            elif Mask_rifle10m_5.overlap(MaskDiabolo, offset_Mask):
                iPoints = 5
            elif Mask_rifle10m_4.overlap(MaskDiabolo, offset_Mask):
                iPoints = 4
            elif Mask_rifle10m_3.overlap(MaskDiabolo, offset_Mask):
                iPoints = 3
            elif Mask_rifle10m_2.overlap(MaskDiabolo, offset_Mask):
                iPoints = 2
            elif Mask_rifle10m_1.overlap(MaskDiabolo, offset_Mask):
                iPoints = 1
            elif Mask_rifle10m_0.overlap(MaskDiabolo, offset_Mask):
                iPoints = 0
        # target evaluation rifle 15m
        if xRifle15m:
            if Mask_rifle15m_10.overlap(MaskDiabolo, offset_Mask):
                iPoints = 10
            elif Mask_rifle15m_9.overlap(MaskDiabolo, offset_Mask):
                iPoints = 9
            elif Mask_rifle15m_8.overlap(MaskDiabolo, offset_Mask):
                iPoints = 8
            elif Mask_rifle15m_7.overlap(MaskDiabolo, offset_Mask):
                iPoints = 7
            elif Mask_rifle15m_6.overlap(MaskDiabolo, offset_Mask):
                iPoints = 6
            elif Mask_rifle15m_5.overlap(MaskDiabolo, offset_Mask):
                iPoints = 5
            elif Mask_rifle15m_4.overlap(MaskDiabolo, offset_Mask):
                iPoints = 4
            elif Mask_rifle15m_3.overlap(MaskDiabolo, offset_Mask):
                iPoints = 3
            elif Mask_rifle15m_2.overlap(MaskDiabolo, offset_Mask):
                iPoints = 2
            elif Mask_rifle15m_1.overlap(MaskDiabolo, offset_Mask):
                iPoints = 1
            elif Mask_rifle15m_0.overlap(MaskDiabolo, offset_Mask):
                iPoints = 0
        #target evaluation Biathlon
        if xBiathlon:
            if Mask_Bia_1.overlap(MaskDiabolo, offset_Mask):
                Biathlon_tmpScore[0] = True
            if Mask_Bia_2.overlap(MaskDiabolo, offset_Mask):
                Biathlon_tmpScore[1] = True
            if Mask_Bia_3.overlap(MaskDiabolo, offset_Mask):
                Biathlon_tmpScore[2] = True
            if Mask_Bia_4.overlap(MaskDiabolo, offset_Mask):
                Biathlon_tmpScore[3] = True
            if Mask_Bia_5.overlap(MaskDiabolo, offset_Mask):
                Biathlon_tmpScore[4] = True

    def zeichnen():
        global xBiathlon
        screen.fill(FIREARMS)
        iVerticalName = 50
        #Main Menu
        if xIntro:
            screen.blit(pic_pickpistol10m_sc, (300, 250))
            screen.blit(pic_pickrifle10m_sc, (420, 251))
            screen.blit(pic_pickrifle15m_sc, (420, 331))
            screen.blit(pic_Biathlon_sc, (635, 250))

        #10m Pistole
        if xPistol10m:
            for i in range(0, len(pic_Scheibe_pistol10m)):
                screen.blit(pic_Scheibe_pistol10m[i], (0, 0))
            screen.blit(pic_Pistol_scale, (350, 50))
            screen.blit(pic_backbutton_scale, (20, 20))
            screen.blit(pic_ButtonBlindShot_scale, (220, 650))
            screen.blit(pic_ButtonReset_scale, (110, 650))
            screen.blit(txtActivePlayer, (50, 90))
            #Player Score
            for i in range(0, len(names)):
                txtPlayerNames = GAME_FONT.render(Players[i].name, True, (240, 255, 240))
                txtPlayerScore = GAME_FONT.render(str(Players[i].score), True, (240, 255, 240))
                screen.blit(txtPlayerNames, (1050, iVerticalName))
                screen.blit(txtPlayerScore, (1050, iVerticalName +50))
                iVerticalName += 100
        #10m Rifle
        if xRifle10m:
            for i in range(0, len(pic_Scheibe_rifle10m)):
                screen.blit(pic_Scheibe_rifle10m[i], (0, 0))
            screen.blit(pic_Rifle_scale, (490, 240))
            screen.blit(pic_backbutton_scale, (20, 20))
            screen.blit(pic_ButtonBlindShot_scale, (220, 650))
            screen.blit(pic_ButtonReset_scale, (110, 650))
            screen.blit(txtActivePlayer, (150, 50))
            # Player Score
            for i in range(0, len(names)):
                txtPlayerNames = GAME_FONT.render(Players[i].name, True, (240, 255, 240))
                txtPlayerScore = GAME_FONT.render(str(Players[i].score), True, (240, 255, 240))
                screen.blit(txtPlayerNames, (1050, iVerticalName))
                screen.blit(txtPlayerScore, (1050, iVerticalName +50))
                iVerticalName += 100
        #15m Rifle
        if xRifle15m:
            for i in range(0, len(pic_Scheibe_rifle15m)):
                screen.blit(pic_Scheibe_rifle15m[i], (0, 0))
            screen.blit(pic_Rifle15m_scale, (465, 215))
            screen.blit(pic_backbutton_scale, (20, 20))
            screen.blit(pic_ButtonBlindShot_scale, (220, 650))
            screen.blit(pic_ButtonReset_scale, (110, 650))
            screen.blit(txtActivePlayer, (150, 50))
            # Player Score
            for i in range(0, len(names)):
                txtPlayerNames = GAME_FONT.render(Players[i].name, True, (240, 255, 240))
                txtPlayerScore = GAME_FONT.render(str(Players[i].score), True, (240, 255, 240))
                screen.blit(txtPlayerNames, (1050, iVerticalName))
                screen.blit(txtPlayerScore, (1050, iVerticalName +50))
                iVerticalName += 100

        #Biathlon
        if xBiathlon:
            # Player Score and Buttonms
            for i in range(0, len(names)):
                txtPlayerNames = GAME_FONT.render(Players[i].name, True, (240, 255, 240))
                txtPlayerScore = GAME_FONT.render(str(Players[i].score_Biathlon), True, (240, 255, 240))
                screen.blit(txtPlayerNames, (1150, iVerticalName))
                screen.blit(txtPlayerScore, (1150, iVerticalName + 50))
                iVerticalName += 100
            screen.blit(pic_backbutton_scale, (20, 20))
            screen.blit(pic_ButtonBlindShot_scale, (220, 650))
            screen.blit(pic_ButtonReset_scale, (110, 650))
            screen.blit(txtActivePlayer, (150, 50))

            screen.blit(pic_Biathlon_Rechteck, (0, 0))
            for i in range(0, len(pic_Biathlon_scheiben)):
                screen.blit(pic_Biathlon_scheiben[i], (0, 0))
                if Biathlon_tmpScore[i]:
                    screen.blit(pic_Biathlon_target[i], (0, 0))


    def resetDiabolo():
        global mausx,mausy,Diabolo_Rect,Schuss
        Diabolo_Rect = [0, 0]
        mausx = 0
        mausy = 0

    def resetStats():
        global iCountRound, iRound
        for i in range(0, len(names)):
            Players[i].score = 0
            Players[i].score_Biathlon = 0
            iCountRound = 2
            iRound = 0

    #define masks
    Mask_Pistol10m = pygame.mask.from_surface(pic_pickpistol10m_sc)
    Mask_Rifle10m = pygame.mask.from_surface(pic_pickrifle10m_sc)
    Mask_Rifle15m = pygame.mask.from_surface(pic_pickrifle10m_sc)
    Diabolo = pygame.image.load(os.path.join(path,"pics/Schuss.png"))
    MaskDiabolo = pygame.mask.from_surface(Diabolo)
    Diabolo_Rect = Diabolo.get_rect()
    Mask_backbutton = pygame.mask.from_surface(pic_backbutton_scale)
    Mask_blindshotbutton = pygame.mask.from_surface(pic_ButtonBlindShot_scale)
    Mask_resetbutton = pygame.mask.from_surface(pic_ButtonReset_scale)
    Mask_Biathlon = pygame.mask.from_surface(pic_Biathlon_sc)

    #Create Playerclasses
    for i in range(0,len(names)):
        Players.append(Player(names[i]))

    #Font
    GAME_FONT = pygame.font.SysFont("Times", 35)
    hit_for_screenshot = False
    screenshot_delay = 0

    # Start Game
    while hmsysteme.game_isactive():

        for event in pygame.event.get():
            # Beenden bei [ESC] oder [X]
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                hit_for_screenshot = True
                mausx = event.pos[0]  # pos = pygame.mouse.get_pos() MAUSPOSITION ingame
                mausy = event.pos[1]
                print("X:", mausx, "Y:", mausy)
                Diabolo_Rect = pygame.Rect(mausx-9, mausy-9, 18, 18)
                screen.blit(Diabolo, Diabolo_Rect)

                if xPistol10m or xRifle10m or xRifle15m or xBiathlon and not xIntro and not xReset:
                    Evaluation()

        if hmsysteme.hit_detected():
            hit_for_screenshot = True
            pos = hmsysteme.get_pos()
            mausx = pos[0]
            mausy = pos[1]
            Diabolo_Rect = pygame.Rect(pos[0] - 9, pos[1] - 9, 18, 18)
            screen.blit(Diabolo, Diabolo_Rect)

            if xPistol10m or xRifle10m or xRifle15m or xBiathlon and not xIntro and not xReset:
                Evaluation()

        #ButtonHandler
        iGetAction = hmsysteme.get_action()
        if iGetAction > 0:
            #Button 10m Pistole
            if iGetAction == 1 and xIntro:
                xPistol10m = True
                xIntro = False
            #Button 10m Gehwer
            if iGetAction == 2 and xIntro:
                xRifle10m = True
                xIntro = False
            #Button 15m Gewehr
            if iGetAction == 3 and xIntro:
                xRifle15m = True
                xIntro = False
            #Button Biathlon
            if iGetAction == 4 and xIntro:
                xBiathlon = True
                xIntro = False
            #Button Back
            if iGetAction == 5:
                xRifle10m = False
                xRifle15m = False
                xPistol10m = False
                xBiathlon = False
                xIntro = True
            #Button Reset
            if iGetAction == 6:
                xReset = True
                resetStats()
            #Button BlindShot
            if iGetAction == 7:
                xHit = True
                iPoints = 0

        #Active Player
        txtActivePlayer = GAME_FONT.render(Players[iRound].name + ": " + str(iCountRound), True, (255, 255, 255))

        #add points to players and count rounds
        if xHit:
            Players[iRound].score = Players[iRound].score + iPoints
            iCountRound -= 1
            xHit = False
            iPoints = 0
        if iCountRound == 0:
            iCountRound = 2
            iRound += 1
        if iRound == len(names):
            iRound = 0

        #Screenshot
        if hit_for_screenshot:
            screenshot_delay+=1
            if screenshot_delay==10:
                screen.blit(Diabolo, Diabolo_Rect)
                pygame.display.flip()
                start=time.time()
                hmsysteme.take_screenshot(screen)
                screenshot_delay=0
                hit_for_screenshot=False

        zeichnen()
        resetDiabolo()
        xReset = False
        pygame.display.flip()
        clock.tick(framerate)



if __name__ == '__main__':
    main()

