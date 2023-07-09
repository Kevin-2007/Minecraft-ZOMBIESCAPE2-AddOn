# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()

class ZombiescapeServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        print("===ZombiescapeServerSystemFlie===")
        self.ListenEvent()
        self.gameState = -1 
        # -1: prepare   0: prestart   1: gaming    2: aftergaming   3: finished
        self.playerNum = 0

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "OnScriptTickServer", self, self.OnTick)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnChat)

    def UnListenEvent(self):
        pass

    def OnChat(self, args):
        username = args["username"]
        playerId = args["playerId"]
        message = args["message"]
        if "ze2cmd>" in message:
            if "damage" in message:
                pass

    def OnTick(self):
        self.playerNum = len(serverApi.GetPlayerList())

    def prestart(self, args):
        """
        args: None
        todo: 
        - show the view of the map
        - show the information of the players
        - teleport players to the target position
        """

    def Destory(self):
        print("===ZomebiescapeServerSystemDestroy===")
        self.UnListenEvent()