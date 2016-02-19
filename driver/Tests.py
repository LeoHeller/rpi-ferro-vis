    

def main()

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

main()
