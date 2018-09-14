from Tkinter import Tk, Label, Button
import time
import blinkt

blinkt.set_brightness(0.1)

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text='this is out first GUI')
        self.label.pack()

        self.greet_button = Button(master,text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text = "Close", command = master.quit)
        self.close_button.pack()

    def greet(self):
      hi = 10
      ho = 80
      while hi >= 0:
        for var in range(0,8):
          blinkt.clear()
          blinkt.set_pixel(var, 0, 80, ho)
          blinkt.show()
          time.sleep(0.1)
          ho = ho - 2
        hi = hi - 1
      

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
