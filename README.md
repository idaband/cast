# Pi Computer Aided Switch Track Pi-CAST

Control Lionel Switch Track from a raspbery pi.
Used for switching relays on a https://sequentmicrosystems.com/products/raspberry-pi-relays-stackable-card board attached to a raspbery pi.

## goals
Lionel switch remote switch track uses a momentary switches.  One activates switch track to through.  The other activates to bypass.
We will use a set of relays.  We will turn on / off a relay to act like a momentary switch.

The application will facitage as a service for both command line and eventually support webapi.  
It will hold the current last know computer controlled state.  

## pre-reqs
raspberry pi
relay board from sequent microsystems


## intial startup
Default mapping used for the project.

|SWITCH | RELAY NUMBER | ACTION|
|---|---|---|
|Switch 1 | relay 0 | through|
|Switch 1 | relay 1 | bypass|
| | | |
|Switch 2 | relay 2 | through|
|Switch 2 | relay 3 | bypass|
| | | |
|Switch 3 | relay 4 | through|
|Switch 3 | relay 5 | bypass|
| | | |
|Switch 4 | relay 6 | through|
|Switch 4 | relay 7 | bypass|

```switchTrack(SwitchNumber,Through)```
```switchTrack(SwitchNumber,bypass)```

```switchTrack(1)```Through
```switchTrack(1,False)``` bypasses

(See attached images for wiring up)  
(see diagram for wiring up)
