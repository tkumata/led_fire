#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
import time
import random
import grovepi
import signal
import sys

pin7 = 7
numleds = 1
grovepi.pinMode(pin7, "OUTPUT")
grovepi.chainableRgbLed_init(pin7, numleds)

int = 0
r = 235
g = 35
b = 0

fire_pattern_1 = [
    (161,0,0),
    (234,35,0),
    (255,129,0),
    (242,85,0),
    (216,0,0)
    ]
fire_pattern_2 = [
    (225,122,87),
    (199,75,75),
    (161,59,59),
    (133,43,43),
    (107,8,8)
    ]
fire_pattern_3 = [
    (236,83,0),
    (249,125,22),
    (255,151,80),
    (255,182,5),
    (189,67,67)
    ]


def signal_term_handler(signal, frame):
    print 'got SIGTERM'
    grovepi.chainableRgbLed_test(pin7, numleds, 0)
    sys.exit(0)


def generate_rgb_color(i):
    global r, g, b
    #i = random.randint(0, 4)
    #(r, g, b) = fire_pattern_1[i]
    k = random.randint(0, 1)

    if k == 0:
        r = r + i
        if r > 245:
            r = 245
        g = g + i
        if g > 55:
            g = 55
    else: 
        r = r - i
        if r < 215:
            r = 215
        g = g - i
        if g < 15:
            g = 15

    b = 0
    t = 0.05

    return (r, g, b, t)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_term_handler)

    while True:
        try:
            if int > 20:
                int = 1
            (r, g, b, t) = generate_rgb_color(int)
            grovepi.storeColor(r, g, b)
            grovepi.chainableRgbLed_pattern(pin7, 0, 0)
            int = int + 1
            #print("%d, %d, %d") % (r, g, b)
            time.sleep(t)
        except KeyboardInterrupt:
            grovepi.chainableRgbLed_test(pin7, numleds, 0)
            quit()
        except IOError:
            print ("Error")
