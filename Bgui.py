import turtle
import time
import blinkt


window = turtle.Screen()
blinkt.set_brightness(0.1)

red = 200
green = 200
blue = 200
hi = 3

def one():
    global hi
    print("keypress detected")
#    blinkt.clear()
#    blinkt.set_pixel(1,red, green, blue)
#    blinkt.show()
    hi = False
    
#difficulty = window.numinput("Difficulty", "Enter a level from 1 to 5: ", minval=1, maxval=5)

print("Print function prints to terminal.")
while hi >0:
  for var in range(0,8):
    blinkt.clear()
    blinkt.set_pixel(var, 0 , 50, 0)
    blinkt.show()
    time.sleep(0.2)
  hi -= hi

window.listen()
window.mainloop()
window.textinput("GAME OVER", "Well done. You scored:")
time.sleep(0.2)

