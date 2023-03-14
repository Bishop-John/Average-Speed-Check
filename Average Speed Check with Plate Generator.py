import random as r
import time
import datetime

date = (time.strftime("%d/%m/%Y"))
SpeedingCarCount = 0

#this bit of code below is used when generating unique numberplates
Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

Year = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"]

##################################################################################
print ("The speed limit must be set between 20 and 100 MPH.")
while True:
    try:
        SpeedLimit = int(input("What is the Speed Limit for this road?"))
        while SpeedLimit < 20 or SpeedLimit > 100:
            SpeedLimit = int(input("That is not valid, please try again>: "))
    except ValueError:
        print ("That is not valid, please try again> ")
    else:
        break
###################################################################################

PassingCars = int(input("How many cars are about to pass through? "))
while type(PassingCars) != int or PassingCars <0:
    print ("That was not a valid number, please try again.")
    PassingCars = int(input("How many cars are about to pass through? "))

for i in range(PassingCars):

    DriverReg = []
    DriverReg.extend(r.choice(Letters) for i in range(2))
    DriverReg.extend(r.choice(Year) for i in range(1))
    DriverReg.extend(" ")
    DriverReg.extend(r.choice(Letters) for i in range(3))
    
    DriverReg = "".join(DriverReg)

    Speed1 = r.randint(1, 70)
    Speed2 = r.randint(1, 70)
    AverageSpeed = ((Speed1 + Speed2)/2)

    print ("Car registration number", DriverReg, "drove through checkpoint 1 at: ", Speed1, "MPH")
    print ("Car registration number", DriverReg, "drove through checkpoint 2 at: ", Speed2, "MPH")
    print ("Car registration number", DriverReg, "therefore had an average speed of", AverageSpeed, "MPH")

    if AverageSpeed > SpeedLimit:
        print ("Car registration number", DriverReg, "was caught speeding.")
        print ("SPEEDING FINE to be issued.\n")
        SpeedingCarCount = SpeedingCarCount + 1
        #time.sleep(1)
        with open('Task 1 Output File.txt', 'a') as open_file:
            open_file.write ("On the {}, {} was caught driving at {} MPH. FINE issued. \n".format(date, DriverReg, AverageSpeed))
        open_file.close()
    else:
        print ("Car registration number", DriverReg, "was not speeding.\n")
        
print ("Out of ", PassingCars, "cars that passed through,", SpeedingCarCount, "of them were speeding.")
SpeedingRate = (SpeedingCarCount/PassingCars)*100
print ("This works out at ", SpeedingRate, "%.")
