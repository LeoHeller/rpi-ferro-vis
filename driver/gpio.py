# load wiringpi
import wiringpi2 as w
from time import sleep

def all_off():
    for pin in range(1, 26):
        w.digitalWrite(pin, 0)

# print raspberry pi board revision
print(w.piBoardRev())

# use physical pin numbering
w.wiringPiSetupPhys()

# set PIN13 to output
w.pinMode(13, 1)
# turn PIN13 off
w.digitalWrite(13,0)


try:
    while True:
        w.digitalWrite(13, 1)
        # delay 0.5s
        sleep(0.5)          
        w.digitalWrite(13, 0)
        sleep(0.5)   
        w.digitalWrite(19, 1)
        # delay 0.5s
        sleep(0.5)          
        w.digitalWrite(19, 0)
        sleep(0.5)     
        
        w.digitalWrite(13, 1)
        # delay 0.5s
        sleep(0.05)          
        w.digitalWrite(13, 0)
        sleep(0.05)   
        w.digitalWrite(19, 1)
        # delay 0.5s
        sleep(0.05)          
        w.digitalWrite(19, 0)
        sleep(0.05)             
        w.digitalWrite(13, 1)
 
finally:
    # turn all pins off
    all_off()
