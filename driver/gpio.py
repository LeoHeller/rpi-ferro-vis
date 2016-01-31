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

w.pinMode(19, 1)
w.digitalWrite(19,1)

w.softPwmCreate(13,0,100)
w.softPwmCreate(19,0,100)

try:
    helligkeit = 0
    while True:
        w.softPwmWrite(19,100-helligkeit) 
        w.softPwmWrite(13,helligkeit)
        sleep(0.01)
        helligkeit += 1
        if helligkeit > 100:
            helligkeit = 0
         

finally:
    # turn all pins off
    all_off()
