#!/usr/bin/env python

from SwitchTrackService import SwitchTrackService

service = SwitchTrackService()



def __art():
    art="""


X     X          ,_____  ____    O                 X     X
 X   X           | PMD \_|[]|_'__Y                  X   X
  X X            |_______|__|_|__|}                  X X
   X=============oo--oo==oo--OOO\\====================X
  X X                                                X X
 X   X       Computer Aided Switch Track            X   X
X     X                                            X     X


"""
    return art;


def __help():
    """HELP MENU
    """
    return """
Enter your Command 
q(quit)
oio(Open Inside to outside loop)
cio(close Inside to outside loop)

ooi(Open outside to inside loop)
coi(Close outside to inside loop)"""

print (__art());

print(__help())

while(True):
    command = input(": ")

    if(command.lower() =='q'):
        break

    elif(command.lower() =='oio'):
        service.openSwitchInnerLoupeToOuterLoop()

    elif(command.lower() =='cio'):
        service.closeSwitchInnerLoupeToOuterLoop()
    
    elif(command.lower()=='ooi'):
        service.openSwitchOuterLoupetoInsideLoupe()
    
    elif(command.lower()=='coi'):
        service.closeSwitchOuterLoupetoInsideLoupe()

    elif(command.lower() == 'sa'):
       print(service.switchStatusAll())
    
    elif(command.lower()=='h'):
        print(__help())
    
    elif(command.lower()=="s"):
        whichSwitch = int(input("Enter Switch Number for Status: "))
        print(service.switchStatus(whichSwitch))

    elif(command.lower()=="st"):
        whichSwitch = int(input("Enter Switch Number to Switch to FLIP: "))
        service.switchTrack(whichSwitch,Flip=True)
    elif(command.lower()=="stt"):
        whichSwitch = int(input("Enter Switch Number to Switch Through: "))
        service.switchTrack(whichSwitch)
    elif(command.lower()=="stc"):
        whichSwitch = int(input("Enter Switch Number to Switch Cross: "))
        service.switchTrack(whichSwitch,Through=False)
    
    elif(command.lower()=="r"):
        service.reset()

    else:
        print("""
Invalid command
===============""")
        print(__help())
    
