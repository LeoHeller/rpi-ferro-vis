# load wiringpi
import wiringpi2 as w
from time import sleep

pins_pwm=[4,17,21,22]
pins_pol=[18,23,24,25]

def all_off():
    for pin in range(1, 26):
        w.digitalWrite(pin, 0)

# print raspberry pi board revision
print(w.piBoardRev())

def main():
    setup()
    try:
        helligkeit = 10
        while True:
            magnet (2,helligkeit,0) 
            sleep(0.01)
            helligkeit += 1
            if helligkeit > 100:
                helligkeit = 0
             

    finally:
         # turn all pins off
        all_off()

def setup():
    # use Gpio pin numbering
    w.wiringPiSetupGpio()

    # polarity pins are outputs:
    for pin in pins_pol:
        w.pinMode(pin, 1)
        w.digitalWrite(pin,0)

    # PWM pins:
    for pin in pins_pwm:
        w.softPwmCreate(pin,0,100)

def magnet(nummer, staerke, polaritaet):
    if not ((0 <= nummer <=3) and (0<= staerke <= 100) and (0<= polaritaet <=1)):
        #fehler        
        return -1
    w.softPwmWrite(pins_pwm[nummer],staerke)
    w.digitalWrite(pins_pol[nummer],polaritaet)
    return 0

if __name__ == "__main__":
    main()
    




