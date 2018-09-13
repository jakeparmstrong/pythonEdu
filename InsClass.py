#classes
class Instrument():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def playmus(self):
        print('Okay, '+self.name+', take it away!')
        print(self.name+': '+self.sound)

#instr = str(input("What is the instrument called?"))
timbre = input("What sound does it make? ")
              
ins = Instrument("sax", "toot toot")#instr, timbre)

ins.playmus()
