#!/usr/bin/env python


import re
import threading
import time
import lib8relind 


class SitchTrackService(object):

    def __init__(self):        
        # self._relay1 = False
        # self.relay2 = False
        # self._relay3 = False
        # self._relay4 = False
        # self._relay5 = False
        # self._relay6 = False
        # self._relay7 = False
        # self._relay8 = False

        self._trackSwitchThrough1=True
        self._trackSwitchThrough2=True
        self._trackSwitchThrough3=True
        self._trackSwitchThrough4=True

        self.setInitialSwitchState()

        #initit needs to call me
    def setInitialSwitchState(self):
        self.switchTrack(1)
        time.sleep(1)
        self.switchTrack(2)
        time.sleep(1)
        self.switchTrack(3)
        time.sleep(1)
        self.switchTrack(4)
        time.sleep(3)
        self.switchTrack(1,False)
        return


    def switchInnerLoupeToOuterLoop(self):
        
        return

    #
    def switchTrack(self,switchNumber,through=True):
        #if through (true) then switch number minus 1 = the refering 0 based relay number
        relayToSwitch = (switchNumber*2) - 1 if through else (switchNumber*2) -  0
        self.switchRelay(relayToSwitch)
        return


        # 1 1-2
        # 2 3-4
        # 3 5-6
        # 4 7-8


    def switchRelay_thread(self,relayNumber):
        lib8relind.set(0,relayNumber,1)
        time.sleep(.5)
        lib8relind.set(0,relayNumber,0)
        return
    
    def switchRelay(self,relayNumber):
        x=threading.Thread(target=self.switchRelay_thread,args=(relayNumber,))
        x.start()



bob = SitchTrackService()