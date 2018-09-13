from blinkt import set_pixel, set_brightness, show, clear, time

set_brightness(0.1)

while True:
  for var in range(0,8):
    clear()
    set_pixel(0, 0 , 0, 0)
    show()
    time.sleep(0.002)
