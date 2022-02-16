import RPi.GPIO as GPIO
import time
import math as bob
from SwitchTrackService import SwitchTrackService


# service = SwitchTrackService()
class BeamBreakerService(object):

    def __init__(self):
        self._holding_time = 10.0
        self._inHold = False
        self._startHold = time.time()
        self._BEAM_PIN = 17
        self._lastBreakTime = time.time()
        self._broke = False
        self._stopped = False
        self._currentHolder = -1
        self._switchNumbers=[27,222,17,18]
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self._BEAM_PIN, GPIO.BOTH, callback=self.__break_beam_callback)
        
    def __del__(self):
        GPIO.cleanup()



    def __break_beam_callback(self,channel):
        # global lastBreakTime
        # global inHold
        # global startHold
        # global broke
        # global stopped
    
    
    # if(time.time()-lastBreakTime <=.05):#trying to get rid of gitter without using log
    #    # broke= True
    #     return
    # else:
    #     lastBreakTime = time.time()
    # print (f'The one we care about is {switchNumbers[currentHolder-1]}')
        
        print (f"The channel number was {channel}")
    # print (f'The switch number we care about is {switchNumbers.index(channel)+1}')
        
        
        self._currentTime = time.time()
        if GPIO.input(self._BEAM_PIN):
        
            print("beam unbroken")
            self._broke = False
            self.__holdingLogic(self._currentTime)
        
        else:
            self._broke= True
            print("beam broken")
            self.__holdingLogic(self._currentTime)
       
    def __holdingLogic(self, passedInTime):
        # global inHold
        # global stopped
        # global broke
        # global holding_time
    
        if(self._inHold == False ):
            return
    
        #if bean has been open for more than 5 seconds release if in hold mode.    
        if(((passedInTime - self._startHold) > self._holding_time) & self._inHold):
            self._inHold = False            #not sure i want to auto release the inHold
            self._stopped = False
            return
        
        
        print( bob.ceil(passedInTime-self._startHold))
        
        
        
        if(bob.ceil(passedInTime - self._startHold) >= self._holding_time ):
            print("train is stopped and waiting")
            self._inHold = True
            self._broke = False
            self._stopped=True
            # service.openSwitchInnerLoupeToOuterLoop()
        else:
            print("START the timer over bouncing")


    def holdTrain(self):
        # global inHold
        # global startHold
        # global currentHolder 
        self._currentHolder= 3
        # print ("hold value = %s" %inHold);
        print (f"hold value = {self._inHold}")
        if(self._inHold==True):
            return
    
        self._inHold=True
        self._startHold = time.time()
    

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)
bbs = BeamBreakerService()

while(True):
    message = input("Press q to quit\n\n")
    if(message=='q'):
        break
    if(message=='h'):
        bbs.holdTrain()
    
# GPIO.cleanup()