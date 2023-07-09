# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()

class ZombiescapeClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        print("===ZombiescapeClientSystemListen")
        self.ListenEvent()

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUIInit)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnScriptTickClient", self, self.OnTick)

    def OnUIInit(self,args):
        print("initUI")
        clientApi.RegisterUI("ZombiescapeScript", "playingGUIScreen", "ZombiescapeScript.clientSystem.playingGUIScreen.playingGUIScreen", "playingGUIScreen.main")
        clientApi.CreateUI("ZombiescapeScript", "playingGUIScreen", {"isHud": 1})

    def OnTick(self):
        pass