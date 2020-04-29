from displays.display import Display
from entities.entity import Entity
from entities.gui import buttons
from entities.gui.checkbox import CheckBox
from entities.gui.labels import Label
from tools.eztext import Input,InputBox
import json
import pygame
import constants as C
class SettingsMenu(Display):
    def __init__(self):
        super().__init__(C.GAME.SCREEN,[])

        # Conf Files
        p1ConfFile = C.P1_CONF_FILE
        p2ConfFile = C.P2_CONF_FILE
        p3ConfFile = C.P3_CONF_FILE
        p4ConfFile = C.P4_CONF_FILE

        self.textInputs = {}

        entities = []
        with open(C.SETTINGS_FILE,'r') as f:
            data = f.read()
        loadedSettings = json.loads(data)
        centerx = C.GAME.SCREEN.get_rect().centerx
        centery = C.GAME.SCREEN.get_rect().centery
        screenHeight = C.GAME.SCREEN.get_rect().height
        screenWidth = C.GAME.SCREEN.get_rect().width
        # Title
        title = Label("Settings",centerx=centerx,centery=screenHeight*.1)
        entities.append(title)
        # Round length (in seconds)

        # Pre-round countdown (in seconds)

        # Players
        playerRowY = screenHeight *.2
        # Player1
        p1Label = Label("Player 1:",centerx=screenWidth*.1,centery=playerRowY)
        entities.append(p1Label)
        p1Check = CheckBox(valueKey='player1',x=p1Label.rect.right+10,centery=playerRowY,checked=True,disabled=True)
        entities.append(p1Check)
        # Config
        p1Config = buttons.KeysButton('Player 1 Keys',p1ConfFile)
        p1Config.rect.centerx = p1Label.rect.centerx
        p1Config.rect.centery = playerRowY + p1Config.rect.height * 1.5
        entities.append(p1Config)

        # Player2
        p2Label = Label("Player 2:",centerx=screenWidth*.35,centery=playerRowY)
        entities.append(p2Label)
        p2Check = CheckBox(valueKey='player2',x=p2Label.rect.right+10,centery=playerRowY,checked=True,disabled=True)
        entities.append(p2Check)
        # Config
        p2Config = buttons.KeysButton('Player 2 Keys',p2ConfFile)
        p2Config.rect.centerx = p2Label.rect.centerx
        p2Config.rect.centery = playerRowY + p2Config.rect.height * 1.5
        entities.append(p2Config)

        # Player3
        p3Label = Label("Player 3:",centerx=screenWidth*.65,centery=playerRowY)
        entities.append(p3Label)
        p3Check = CheckBox(valueKey='player3',x=p3Label.rect.right+10,checked=loadedSettings['player3'],centery=playerRowY)
        entities.append(p3Check)
        # Config
        p3Config = buttons.KeysButton('Player 3 Keys',p3ConfFile)
        p3Config.rect.centerx = p3Label.rect.centerx
        p3Config.rect.centery = playerRowY + p3Config.rect.height * 1.5
        entities.append(p3Config)

        # Player4
        p4Label = Label("Player 4:",centerx=screenWidth*.9,centery=playerRowY)
        entities.append(p4Label)
        p4Check = CheckBox(valueKey='player4',x=p4Label.rect.right+10,checked=loadedSettings['player4'],centery=playerRowY)
        entities.append(p4Check)
        # Config
        p4Config = buttons.KeysButton('Player 4 Keys',p4ConfFile)
        p4Config.rect.centerx = p4Label.rect.centerx
        p4Config.rect.centery = playerRowY + p4Config.rect.height * 1.5
        entities.append(p4Config)

        # Game seconds
        restricted = '0123456789'
        gameSecondsLabel = Label("Game Length (seconds):",centerx=screenWidth*.5,centery=screenHeight*.4)
        entities.append(gameSecondsLabel)
        gameSecondsInput = Input(bg=C.WHITE,maxlength=3,color=C.BLACK,restricted=restricted)
        gameSecondsInput.value = loadedSettings['gameLength']
        gameSecondsInput.rect.x = gameSecondsLabel.rect.right + 10
        gameSecondsInput.rect.centery = gameSecondsLabel.rect.centery
        self.textInputs['gameLength'] = gameSecondsInput
        entities.append(InputBox(gameSecondsInput))
        entities.append(gameSecondsInput)


        # Countdown seconds
        countdownSecondsLabel = Label("Countdown (seconds):",centerx=screenWidth*.5,centery=screenHeight*.45)
        entities.append(countdownSecondsLabel)
        countdownSecondsInput = Input(bg=C.WHITE,maxlength=2,color=C.BLACK,restricted=restricted)
        countdownSecondsInput.rect.x = countdownSecondsLabel.rect.right + 10
        countdownSecondsInput.rect.centery = countdownSecondsLabel.rect.centery
        countdownSecondsInput.value = loadedSettings['countdown']
        self.textInputs['countdown'] = countdownSecondsInput
        entities.append(InputBox(countdownSecondsInput))
        entities.append(countdownSecondsInput)

        # Save Button
        save = buttons.SaveSettingsButton()
        save.rect.centerx = centerx
        save.rect.top = screenHeight*.6
        entities.append(save)

        # Back to Main Menu
        mainMenu = buttons.MainBackButton()
        mainMenu.rect.x = 30
        mainMenu.rect.y = 30
        entities.append(mainMenu)

        self.entities = entities

    def tick(self):
        super().tick()
