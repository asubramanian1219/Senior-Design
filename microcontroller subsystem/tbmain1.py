import time
#import GPIO
import helpersV2 as helpers
#import following
#import sensorsdata
import math
#import alarm


def rovergo(sensorrightdata, sensorleftdata, followingdistance,updateright, updateleft):
    # defining
    power = True
    distanceRight = sensorrightdata  # number is in inches
    distanceLeft = sensorleftdata  # number is in inches
    followrange = followingdistance  # number in inches

    while(power==True):
        if(followrange<=7):
            while(distanceRight>= 36 and distanceLeft >= 36): #3 feet
                #follow() #this is where the follow command will be put in
                helpers.motorsforward()
                time.sleep(2)
                break

            if(distanceRight<=36 and distanceLeft <=36):
                time.sleep(1)
                helpers.motorsbackward()
                time.sleep(.05)
                helpers.motorsturnright()
                time.sleep(.05)
                #break
                if(updateright>36):
                    helpers.motorsforward()
                    time.sleep(.05)
                    helpers.motorsturnleft()
                    time.sleep(.05)
                    helpers.motorsforward()
                    time.sleep(.05)
                    break
                elif(updateright<36):
                    helpers.motorsturnbackleft()
                    time.sleep(.05)
                    helpers.motorsturnleft()
                    time.sleep(.05)
                    if(updateleft>36):
                        helpers.motorsforward()
                        time.sleep(.05)
                        helpers.motorsturnright()
                        time.sleep(.05)
                        helpers.motorsforward()
                        time.sleep(.05)
                        break
                    elif(updateleft<36):
                        helpers.motorsturnbackright()
                        time.sleep(.05)
                        helpers.motorsbackward()
                        time.sleep(.05)
                        break
                    else:
                        break
                    break
                else:
                    break
            elif(distanceRight<36 and distanceLeft>36):
                helpers.motorsturnleft()
                time.sleep(.05)
                helpers.motorsforward()
                time.sleep(.05)
                helpers.motorsturnright()
                time.sleep(.05)
                helpers.motorsforward()
                time.sleep(.05)
                break
            elif(distanceLeft<36 and distanceRight>36):
                helpers.motorsturnright()
                time.sleep(.05)
                helpers.motorsforward()
                time.sleep(.05)
                helpers.motorsturnleft()
                time.sleep(.05)
                helpers.motorsforward()
                time.sleep(.05)
                break
            else:
                break
        elif(followrange > 7):
            helpers.stop()
            print('alarm')#alarm
            break
        power=False