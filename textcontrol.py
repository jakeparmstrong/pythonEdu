import blinkt
import time
import random

def colourset():
    global red
    global green
    global blue
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

blinkt.set_brightness(0.1)

sihd = input("Enter seed: ")
random.seed(sihd)
colourset()

#def cont
lNum = 1

while lNum != 0:
    lNum = int(input("Which LED to you want to switch on? "+
                 "\nEnter 1-8, or 9 to clear all ('0' to quit)"))
    lNum %=10
    if lNum == 9:
        print("Clearing LEDs and changing LED colour.\n")
        colourset()
        blinkt.clear()
        blinkt.show()
        
    else:
        lNum = int(lNum)
        print ("Turning on LED # "+str(lNum)+".\n")
#    blinkt.clear()
        blinkt.set_pixel(lNum - 1, red, green, blue)
        blinkt.show()

print("Exiting program.")
blinkt.set_brightness(0)
blinkt.show()
