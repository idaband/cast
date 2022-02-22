import RPi.GPIO as GPIO
import time
import math as bob
# import threading
#from SwitchTrackService import SwitchTrackService
from Event import Event



# service = SwitchTrackService()
class BeamBreakerService(object):

    def __init__(self):
        self._holding_time = 10.0
        self._inHold = False
        self._startHold = -1.0
        self._BEAM_PIN = 17
        self._lastBreakTime = time.time()
        self._broke = False
        self._stopped = False
        self._currentHolder = -1
        self._switchNumbers=[27,222,17,18]
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self._BEAM_PIN, GPIO.BOTH, callback=self.__break_beam_callback)
        
        self._OnTrainHeld = Event()
        self._OnTrainStop = Event()

        
    def __TrainHeld(self,number):
        self._OnTrainHeld(number)
        
    def AddSubscribersForHoldEvent(self,objMethod):
        self._OnTrainHeld += objMethod
         
    def RemoveSubscribersForHoldEvent(self,objMethod):
        self._OnTrainHeld -= objMethod


    def __TrainStop(self,number):
        self._OnTrainStop(number)
        
    def AddSubscribersForTrainStopEvent(self,objMethod):
        self._OnTrainStop += objMethod
         
    def RemoveSubscribersForTrainStopEvent(self,objMethod):
        self._OnTrainStop -= objMethod
    
         
    def __del__(self):
        GPIO.cleanup()



    def __break_beam_callback(self,channel):
        
        print (f"The channel number was {channel}")
    # print (f'The switch number we care about is {switchNumbers.index(channel)+1}')
        
        
        self._currentTime = time.time()
        if GPIO.input(self._BEAM_PIN):
        
            print("beam unbroken")
            self._broke = False            
        else:
            self._broke= True
            print("beam broken")
        
        self.__holdingLogic(self._currentTime,channel)
       
    def __holdingLogic(self, passedInTime,channel):        
    
        if(self._inHold == False ):
            return
        if(self._startHold <0 and self._broke == True):
            self._startHold = time.time()
            self.__TrainStop(self._switchNumbers.index(channel)+1)
            # x = lambda a: print("hello")
            # t = threading.Timer(20.0,x)
            # t.start()
        
    
        #if bean has been open for more than 5 seconds release if in hold mode.    
        if(((passedInTime - self._startHold) > self._holding_time) and self._inHold):
            self._inHold = False            #not sure i want to auto release the inHold
            self._stopped = False
            self._startHold = -1.0
            self._broke  = False
            return
        
        
        print( bob.ceil(passedInTime-self._startHold))
        
        
        
        if(bob.ceil(passedInTime - self._startHold) >= self._holding_time ):
            print("train is stopped and waiting")
            self._inHold = False
            self._broke = False
            self._stopped=True
            self.__TrainHeld(self._switchNumbers.index(channel)+1)
            self._startHold = -1.0
            # service.openSwitchInnerLoupeToOuterLoop()
        else:
            print("START the timer over bouncing")


    def activateHoldTrainAndSwitch(self, switchToHoldAt):
        """Tells the switch to perpare for hold and once the train is in hold and event will fire off letting consumers know the train has been stopped for pre-defined time.

        Args:
            switchToHoldAt (int): Switch Number 1-4(you can update this depending on your switch configuration above) 
        """
        self._currentHolder= switchToHoldAt
        print (f"hold value = {self._inHold}")
        if(self._inHold==True):
            return
    
        self._inHold=True
        #self._startHold = time.time()

def doIt():    

    bbs = BeamBreakerService()

    while(True):
        message = input("Press q to quit\n\n")
        if(message=='q'):
            break
        if(message=='h'):
            bbs.holdTrain()

if __name__=="__main__":
    doIt()
    
# GPIO.cleanup()