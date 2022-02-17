#!/usr/bin/env python

import time
import operator
from SequentMicroSystemsRelay8 import SequentMicroSystemsRelay8 as relay8
from Event import Event
from BeamService import BeamBreakerService


class SwitchTrackService(object):

    def __init__(self):        
        # self._trackSwitchThrough1=True
        # self._trackSwitchThrough2=True
        # self._trackSwitchThrough3=True
        # self._trackSwitchThrough4=True
        # self._switchStatusArray = [self._trackSwitchThrough1,self._trackSwitchThrough2,self._trackSwitchThrough3,self._trackSwitchThrough4]
        self._switchStatusArray = [True,True,True,True]

        self._relay = relay8()

      #todo put in for production  self.__setInitialSwitchState()

        #initit needs to call me
    def __setInitialSwitchState(self):
        self.__switchTrack(1)
        time.sleep(1)
        self.__switchTrack(2)
        time.sleep(1)
        self.__switchTrack(3)
        time.sleep(1)
        self.__switchTrack(4)
        self._switchStatusArray = [True,True,True,True]
        return


    def openSwitchInnerLoupeToOuterLoop(self):
        self.__switchTrack(3,False)
        time.sleep(1)
        self.__switchTrack(4,False)
        # self._switchStatusArray[2] = False
        # time.sleep(1)
        # self._switchStatusArray[3] = False
        return

    def closeSwitchInnerLoupeToOuterLoop(self):
        self.__switchTrack(3)
        time.sleep(1)
        self.__switchTrack(4)
        return

    def openSwitchOuterLoupetoInsideLoupe(self):
        """switches the outside loupe to move to the inside"""
        self.__switchTrack(1,False)
        time.sleep(1)
        self.__switchTrack(2,False)
        return


    def switchTrack(self,switchNumber,Through=True,Flip = False):
        """Switches the track so whatever the Through value is.  If True make it Through, if False make it switch.  
        IF FLIP is set to true, just switch the the current status of the track.

        Args:
            switchNumber (int): The switch number on your track
            Through (bool, optional): stays straight. Defaults to True.
            Flip (bool, optional): change the current state of the switch number.  
                                    IF SET TO TRUE OVERRIDES THE THROUGH VALUE. Defaults to False.
        """
        
        if(Flip):
            self.__switchTrack(switchNumber,through=operator.not_(self._switchStatusArray[switchNumber-1]))
        else:
            self.__switchTrack(switchNumber,Through)


    def reset(self):
        
        self.__setInitialSwitchState()
        return

    def closeSwitchOuterLoupetoInsideLoupe(self):
        self.__switchTrack(3)
        time.sleep(1)
        self.__switchTrack(4)
        return

    

    def __switchTrack(self,switchNumber,through=True):
        """[summary]

        Args:
            switchNumber (int): switch track to change
            through (bool, optional): True for Through, False for Switch. Defaults to True.
        """
        #if through (true) then switch number minus 1 = the refering 0 based relay number

        relayToSwitch = (switchNumber*2) - 1 if through else (switchNumber*2) -  0
        self._relay.switchRelay(relayToSwitch)
        self._switchStatusArray[switchNumber-1] = through
        
        return


    def __getStatusFormated(self,switchNumber):
        return "through" if self._switchStatusArray[switchNumber-1] else "switched"


#TODO make this dynamic for the amount of switches configured
    def switchStatusAll(self):
        """Returns the formated status for all configured switches"""
        
        output = """
        Current Known Status of Switches
        ================================
        %s
        %s
        %s
        %s
        """%(self.switchStatus(1),self.switchStatus(2),self.switchStatus(3),self.switchStatus(4))

        return output

    def switchStatus(self, switchNumber):
        """Returns the status of the input switchNumber for the switch track.
        Through or switched.

        Args:
            switchNumber (int): switch track to change

        Returns:
            int: formated description of the input switch number status
        """
        try:
            output = "Switch %s = %s"%(switchNumber,self.__getStatusFormated(switchNumber))
            return output
        except IndexError as e:
            return "Switch Number ==> %s <== not configured"%switchNumber
