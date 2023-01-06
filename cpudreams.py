# file:     cpudreams.py
# author:   Colin Allen (https://github.com/Nilocallen)
# This program is a simple logic gate simulator that supports creating and
# saving circuits that can be used in further circuits.  My goal with the software
# is to work up to the circuitry needed for a basic CPU.
#
# This project was inspired by a YouTube series by Sebastian Lague listed here.
# https://www.youtube.com/watch?v=QZwneRb-zqA&list=PLFt_AvWsXl0dPhqVsKt1Ni_46ARyiCGSq&index=3&t=2s&ab_channel=SebastianLague
#

import pyglet


def init():
    pass


def update():
    pass


if __name__ == '__main':
    init()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
