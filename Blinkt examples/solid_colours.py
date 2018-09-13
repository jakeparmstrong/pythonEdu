#!/usr/bin/env python

import time

import blinkt

from blinkt import set_brightness, set_pixel

import random


blinkt.set_clear_on_exit()
set_brightness(0.05)
step = 0
var = 0

while True:
    if step == 0:
        w = random.randint(0,25)*10
        blinkt.set_all(w, var, w)
        print(w)

    else:
        blinkt.set_all(w, var, w)
        w +=1
        w %= 255

    step += 1
    step %= 100
    var += 1
    var %= 100
    blinkt.show()
    time.sleep(0.01)
