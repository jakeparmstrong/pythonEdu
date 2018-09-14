#Blinkt switcher - September 14
#Uses readchar library to take input from keypad
#to turn LEDs in Blinkt on and off.

import blinkt
import random
import readchar

#Sets LED colour to something random.
def colourset():
    global red
    global green
    global blue
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

status = [False] * 8

#Setup for first run. User prompted to enter seed
sihd = input("Enter any number (random number seed): ")
random.seed(sihd)
colourset()
blinkt.set_brightness(0.5)
lNum = 1

print("To switch on an LED, press the corresponding number (1-8) on the "
      +"keyboard. \n (9 to reset, 0 to quit)")

while lNum != 0:
    lNum = int(readchar.readchar())
    if lNum == 9:
        print("Clearing LEDs and changing LED colour.\n")
        colourset()
        blinkt.clear()
        blinkt.show()
        status = [False] * 8     
    else:
        lNum = int(lNum)
#        colourset()         #uncomment for more colours  
        if status[lNum-1] is False:
            print ("Turning on LED # "+str(lNum)+".\n")
            blinkt.set_pixel(lNum - 1, red, green, blue)
            blinkt.show()
            status[lNum-1] = True
        else:
            print ("Turning off LED # "+str(lNum)+".\n")
            blinkt.set_pixel(lNum - 1, 0,0,0)
            blinkt.show()
            status[lNum-1] = False
            
print("Exiting program.")
blinkt.set_brightness(0)
blinkt.show()
