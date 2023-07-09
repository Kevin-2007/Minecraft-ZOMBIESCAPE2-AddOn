# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod


@Mod.Binding(name="ZombiescapeScript", version="0.0.1")
class ZombiescapeScript(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def ZombiescapeScriptServerInit(self):
        serverApi.RegisterSystem("ZombiescapeScript", "ZombiescapeServerSystem", "ZombiescapeScript.serverSystem.ZombiescapeServerSystem.ZombiescapeServerSystem")

    @Mod.DestroyServer()
    def ZombiescapeScriptServerDestroy(self):
        pass

    @Mod.InitClient()
    def ZombiescapeScriptClientInit(self):
        clientApi.RegisterSystem("ZombiescapeScript", "ZombiescapeClientSystem", "ZombiescapeScript.clientSystem.ZombiescapeClientSystem.ZombiescapeClientSystem")

    @Mod.DestroyClient()
    def ZombiescapeScriptClientDestroy(self):
        pass
