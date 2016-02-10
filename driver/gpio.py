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
    try:
        sleep(5)

        # test der relais:
        #magnet(0,0,1)
        #sleep(1)
        #magnet(1,0,1)
        #sleep(1)
        #magnet(2,0,1)
        #sleep(1)
        #magnet(3,0,1)
        #sleep(10)
	
        # test der magneten und polaritaet:
        #magnet(0,40,1)
        #sleep(9)
        #magnet(0,00,0)
        #magnet(1,40,0)
        #sleep(9)
        #magnet(1,00,0)
        #magnet(2,40,1)
        #sleep(9)
        #magnet(2,00,0)
        #magnet(3,40,0)

        # kreisbewegung:
        magnet(0,50,0)
        magnet(1,50,1)
        magnet(2,50,0)
        magnet(3,50,1)

        for rot in range(1,4):
          for mag in range(0,3):
            mag_st(mag,100)
            mag_st(mag-1,50)
            sleep(1)

        sleep(9)
	
        # helligkeit = 10
        # while True:
            # magnet (2,helligkeit,0) 
            # sleep(0.01)
            # helligkeit += 1
            # if helligkeit > 100:
                # helligkeit = 0
             

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

if __name__ == "__main__":
    main()
    




