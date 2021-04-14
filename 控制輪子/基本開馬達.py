import RPi.GPIO as GPIO
import curses
import time
from curses import wrapper

GPIO.setmode(GPIO.BCM)

RIN1 = 7
RIN2 = 11
RIN3 = 25
RIN4 = 10
LIN1 = 17
LIN2 = 18
LIN3 = 22
LIN4 = 23



GPIO.setup(RIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIN4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN4, GPIO.OUT, initial=GPIO.LOW)

stdscr = curses.initscr()
stdscr.clear()

while True:
    ch = stdscr.getkey()
# Quit
    if ch == 'q':
       curses.endwin()
       GPIO.output(LIN1, False)     #GPIO17
       GPIO.output(LIN2, False)     #GPIO18
       GPIO.output(LIN3, False)     #GPIO22
       GPIO.output(LIN4, False)     #GPIO23
       GPIO.output(RIN1, False)     #GPIO7
       GPIO.output(RIN2, False)     #GPIO11
       GPIO.output(RIN3, False)     #GPIO25
       GPIO.output(RIN4, False)     #GPIO10
       break

# Forward
    if ch == 'w':
       GPIO.output(LIN1, True)
       GPIO.output(LIN2, False)
       GPIO.output(LIN3, False)
       GPIO.output(LIN4, True)
       GPIO.output(RIN1, True)
       GPIO.output(RIN2, False)
       GPIO.output(RIN3, False)
       GPIO.output(RIN4, True)

# Backward
    if ch == 'x':
       GPIO.output(LIN1, False)
       GPIO.output(LIN2, True)
       GPIO.output(LIN3, True)
       GPIO.output(LIN4, False)
       GPIO.output(RIN1, False)
       GPIO.output(RIN2, True)
       GPIO.output(RIN3, True)
       GPIO.output(RIN4, False)

# Turn Right
    if ch == 'd':
       GPIO.output(LIN1, True)
       GPIO.output(LIN2, False)
       GPIO.output(LIN3, False)
       GPIO.output(LIN4, True)
       GPIO.output(RIN1, True)
       GPIO.output(RIN2, False)
       GPIO.output(RIN3, False)
       GPIO.output(RIN4, False)

# Turn Left
    if ch == 'a':
       GPIO.output(LIN1, False)
       GPIO.output(LIN2, False)
       GPIO.output(LIN3, False)
       GPIO.output(LIN4, True)
       GPIO.output(RIN1, True)
       GPIO.output(RIN2, False)
       GPIO.output(RIN3, False)
       GPIO.output(RIN4, True)
