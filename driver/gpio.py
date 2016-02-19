# load wiringpi
import wiringpi2 as w
from time import sleep

pins_pwm=[4,17,21,22]
pins_pol=[18,23,24,25]

def all_off():
    for pin in pins_pol:
        w.digitalWrite(pin, 0)

    for pin in pins_pwm:
        w.softPwmWrite(pin,0)

# print raspberry pi board revision
# print(w.piBoardRev())

def main():
    setup()
    
    

    # finally:
         # turn all pins off
        # all_off()

def setup():
    # use Gpio pin numbering
    w.wiringPiSetupGpio()

    # polarity pins are outputs:
    for pin in pins_pol:
        w.pinMode(pin, 1)           # defined as output 
        w.digitalWrite(pin,0)       # all output off

    # PWM pins:
    for pin in pins_pwm:
        w.softPwmCreate(pin,0,100)  #define pin as pwm output      

    # all magnets turned off
    magnet(0,0,0)
    magnet(1,0,0)
    magnet(2,0,0)
    magnet(3,0,0)


def magnet(nummer, staerke, polaritaet):
    if not ((0 <= nummer <=3) and (0<= staerke <= 100) and (0<= polaritaet <=1)):
        #fehler        
        print("magnet: falscher Parameter. Magnet=" + str(nummer) + ", Staerke=" + str(staerke) + ", Polaritaet=" + str(polaritaet))
        return -1
    w.softPwmWrite(pins_pwm[nummer],staerke)
    w.digitalWrite(pins_pol[nummer],polaritaet)
    return 0
    
def mag_st(nummer, staerke):
    if not ((0 <= nummer <=3) and (0<= staerke <= 100)):
        #fehler        
        print("mag_st: falscher Parameter. Magnet=" + str(nummer) + ", Staerke=" + str(staerke))
        return -1
    w.softPwmWrite(pins_pwm[nummer],staerke)
    return 0

def pol(nummer,polaritaet):
    if not ((0 <= nummer <=3) and  (0<= polaritaet <=1)):
        print("magnet: falscher Parameter. Magnet=" + str(nummer) + ", Polaritaet=" + str(polaritaet))   
        return -1
    w.digitalWrite(pins_pol[nummer],polaritaet)
    return 0

if __name__ == "__main__":
    main()
    




