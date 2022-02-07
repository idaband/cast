#!/usr/bin/env python

import lib8relind 
import threading
import time


class SequentMicroSystemsRelay8(object):

    def __switchRelay_thread(self,relayNumber):
        lib8relind.set(0,relayNumber,1)
        time.sleep(.5)
        lib8relind.set(0,relayNumber,0)
        return
    
    def switchRelay(self,relayNumber):
        x=threading.Thread(target=self.__switchRelay_thread,args=(relayNumber,))
        x.start()