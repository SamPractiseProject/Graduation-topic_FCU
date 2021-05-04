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
       GPIO.output(LIN1, GPIO.LOW)     #GPIO17
       GPIO.output(LIN2, GPIO.LOW)     #GPIO18
       GPIO.output(LIN3, GPIO.LOW)     #GPIO22
       GPIO.output(LIN4, GPIO.LOW)     #GPIO23
       GPIO.output(RIN1, GPIO.LOW)     #GPIO7
       GPIO.output(RIN2, GPIO.LOW)     #GPIO11
       GPIO.output(RIN3, GPIO.LOW)     #GPIO25
       GPIO.output(RIN4, GPIO.LOW)     #GPIO10

       GPIO.cleanup()       #清除GPIO資料

       break

# Forward
    if ch == 'w':
       GPIO.output(LIN1, GPIO.LOW)
       GPIO.output(LIN2, GPIO.HIGH)
       GPIO.output(LIN3, GPIO.LOW)
       GPIO.output(LIN4, GPIO.HIGH)
       GPIO.output(RIN1, GPIO.HIGH)
       GPIO.output(RIN2, GPIO.LOW)
       GPIO.output(RIN3, GPIO.LOW)
       GPIO.output(RIN4, GPIO.HIGH)

# Backward
    if ch == 'x':
       GPIO.output(LIN1, GPIO.HIGH)
       GPIO.output(LIN2, GPIO.LOW)
       GPIO.output(LIN3, GPIO.HIGH)
       GPIO.output(LIN4, GPIO.LOW)
       GPIO.output(RIN1, GPIO.LOW)
       GPIO.output(RIN2, GPIO.HIGH)
       GPIO.output(RIN3, GPIO.HIGH)
       GPIO.output(RIN4, GPIO.LOW)

# Turn Right
    if ch == 'd':
       GPIO.output(LIN1, GPIO.LOW)
       GPIO.output(LIN2, GPIO.LOW)
       GPIO.output(LIN3, GPIO.LOW)
       GPIO.output(LIN4, GPIO.HIGH)
       GPIO.output(RIN1, GPIO.HIGH)
       GPIO.output(RIN2, GPIO.LOW)
       GPIO.output(RIN3, GPIO.LOW)
       GPIO.output(RIN4, GPIO.HIGH)
       

# Turn Left
    if ch == 'a':
       GPIO.output(LIN1, GPIO.LOW)
       GPIO.output(LIN2, GPIO.HIGH)
       GPIO.output(LIN3, GPIO.LOW)
       GPIO.output(LIN4, GPIO.HIGH)
       GPIO.output(RIN1, GPIO.HIGH)
       GPIO.output(RIN2, GPIO.LOW)
       GPIO.output(RIN3, GPIO.LOW)
       GPIO.output(RIN4, GPIO.LOW)
