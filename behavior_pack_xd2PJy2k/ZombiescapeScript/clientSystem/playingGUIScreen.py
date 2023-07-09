# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()

class playingGUIScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.InitComponentPath()
        self.gameTime = [0, 0, 0, 0]
        self.cdTime = [0.0, 0.0, 0.0, 0.0] # A B C attack

    def InitComponentPath(self):
        print("init component")
        self.health_bar = "/underPanel/health_bar"
        self.energy_bar = "/underPanel/energy_bar"
        self.Inventory = "/underPanel/Inventory"

        self.abilityA = "/controlPanel/abilityA"
        self.abilityB = "/controlPanel/abilityB"
        self.abilityC = "/controlPanel/abilityC"
        self.attack = "/controlPanel/attack"
        self.lie = "/controlPanel/lie"
        self.sneak = "/controlPanel/sneak"
        self.jump = "/controlPanel/jump"

        self.directionLabel = "/topPanel/backImg/directionLabel"
        self.progress_bar = "/topPanel/progress_bar"
        self.timeLabel = "/topPanel/timeLabel"
        self.zombieNum = "/topPanel/backImgNum/zombieNum"
        self.surviveNum = "/topPanel/backImgNum/surviveNum"
        self.setting = "/topPanel/setting"

        self.backImg = "/backImg"
        self.label = "/backImg/label"
    
    def Create(self):
        self.InitData()
        timeCallLater = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId()).AddRepeatedTimer(0.1, self.AutoTimer)
        timeCallLater

    def InitData(self):
        self.health_bar_uiNode = self.GetBaseUIControl(self.health_bar).asProgressBar()
        self.health_bar_text_uiNode = self.GetBaseUIControl(self.health_bar+"/progressLabel").asLabel()
        self.energy_bar_uiNode = self.GetBaseUIControl(self.energy_bar).asProgressBar()
        self.energy_bar_text_uiNode = self.GetBaseUIControl(self.energy_bar+"/progressLabel").asLabel()

        self.Inventory_uiNode = self.GetBaseUIControl(self.Inventory).asButton()
        self.Inventory_uiNode.AddTouchEventParams({"isSwallow": True})

        self.abilityA_uiNode = self.GetBaseUIControl(self.abilityA).asButton()
        self.abilityA_uiNode.AddTouchEventParams({"isSwallow": True})
        self.abilityA_uiNode.SetButtonTouchDownCallback(self.ability)
        self.abilityA_cdImg_uiNode = self.GetBaseUIControl(self.abilityA+"/cdImg").asImage()

        self.abilityB_uiNode = self.GetBaseUIControl(self.abilityB).asButton()
        self.abilityB_uiNode.AddTouchEventParams({"isSwallow": True})
        self.abilityB_uiNode.SetButtonTouchDownCallback(self.ability)
        self.abilityB_cdImg_uiNode = self.GetBaseUIControl(self.abilityB+"/cdImg").asImage()

        self.abilityC_uiNode = self.GetBaseUIControl(self.abilityC).asButton()
        self.abilityC_uiNode.AddTouchEventParams({"isSwallow": True})
        self.abilityC_uiNode.SetButtonTouchDownCallback(self.ability)
        self.abilityC_cdImg_uiNode = self.GetBaseUIControl(self.abilityC+"/cdImg").asImage()

        self.attack_uiNode = self.GetBaseUIControl(self.attack).asButton()
        self.attack_uiNode.AddTouchEventParams({"isSwallow": True})
        self.attack_uiNode.SetButtonTouchDownCallback(self.attack)
        self.attack_cdImg_uiNode = self.GetBaseUIControl(self.attack+"/cdImg").asImage()

        self.lie_uiNode = self.GetBaseUIControl(self.lie).asButton()
        self.lie_uiNode.AddTouchEventParams({"isSwallow": True})
        self.lie_uiNode.SetButtonTouchDownCallback(self.action)

        self.sneak_uiNode = self.GetBaseUIControl(self.sneak).asButton()
        self.sneak_uiNode.AddTouchEventParams({"isSwallow": True})
        self.sneak_uiNode.SetButtonTouchDownCallback(self.action)

        self.jump_uiNode = self.GetBaseUIControl(self.jump).asButton()
        self.jump_uiNode.AddTouchEventParams({"isSwallow": True})
        self.jump_uiNode.SetButtonTouchDownCallback(self.action)

        self.directionLabel_uiNode = self.GetBaseUIControl(self.directionLabel).asLabel()
        self.progress_bar_uiNode = self.GetBaseUIControl(self.progress_bar).asProgressBar()
        self.timeLabel_uiNode = self.GetBaseUIControl(self.timeLabel).asLabel()
        self.zombieNum_uiNode = self.GetBaseUIControl(self.zombieNum).asLabel()
        self.surviveNum_uiNode = self.GetBaseUIControl(self.surviveNum).asLabel()
        self.setting_uiNode = self.GetBaseUIControl(self.setting).asButton()
        self.setting_uiNode.AddTouchEventParams({"isSwallow": True})

        # init health bar
        self.health_bar_uiNode.SetValue(1.0)
        self.health_bar_text_uiNode.SetText("1000/1000")
        # init energy bar
        self.energy_bar_uiNode.SetValue(1.0)
        self.energy_bar_text_uiNode.SetText("1000/1000")
        # init ability 
        self.abilityA_cdImg_uiNode.SetSpriteClipRatio(1.0)
        self.abilityB_cdImg_uiNode.SetSpriteClipRatio(1.0)
        self.abilityC_cdImg_uiNode.SetSpriteClipRatio(1.0)
        self.attack_cdImg_uiNode.SetSpriteClipRatio(1.0)
        # init top panel
        self.progress_bar_uiNode.SetValue(0.0)
        self.zombieNum_uiNode.SetText("0")
        self.surviveNum_uiNode.SetText("0")
        self.timeLabel_uiNode.SetText("<Competition is not started>")
        self.directionLabel_uiNode.SetText("<Direction Panel Is Not Working>")

        # invisible game ui
        clientApi.HideAirSupplyGUI(True)
        clientApi.HideArmorGui(True)
        clientApi.HideEmoteGUI(True)
        clientApi.HideExpGui(True)
        clientApi.HideFoldGUI(True)
        clientApi.HideHealthGui(True)
        clientApi.HideHungerGui(True)
        clientApi.HideInteractGui(True)
        clientApi.HideJumpGui(True)
        clientApi.HideVoiceGUI(True)
        clientApi.HideSwimGui(True)
        clientApi.HideSneakGui(True)
        clientApi.HideSlotBarGui(True)
        clientApi.HideReportGUI(True)
    
    def ability(self, args):
        """ability A B C execute button"""
        pass

    def attack(self, args):
        """player attack button"""
        pass

    def action(self, args):
        """lie jump and sneak"""
        pass

    def AutoTimer(self, args):
        self.gameTime[-1] += 1
        if self.gameTime[-1] == 10:
            self.gameTime[-2] += 1
            self.gameTime[-1] = 0
            if self.gameTime[-2] == 60:
                self.gameTime[-3] += 1
                self.gameTime[-2] = 0
                if self.gameTime[-3] == 60:
                    self.gameTime[-4] += 1
                    self.gameTime[-3] = 0
        timeLabelText = "{}:{}:{}".format(self.gameTime[0], self.gameTime[1], self.gameTime[2])
        self.timeLabel_uiNode.SetText(timeLabelText)

        for element in self.cdTime:
            if element >= 0.1:
                element -= 0.1
        self.abilityA_cdImg_uiNode.SetSpriteClipRatio()

    def Update(self):
        pass

    def Destroy(self):
        pass