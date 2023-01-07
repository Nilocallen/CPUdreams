# File:     cpudreams.py
# Author:   Colin Allen (https://github.com/Nilocallen)
# This program is a simple logic gate simulator that supports creating and
# saving circuits that can be used in further circuits.  My goal with the software
# is to work up to the circuitry needed for a basic CPU.
#
# This project was inspired by a YouTube series by Sebastian Lague listed here.
# https://www.youtube.com/watch?v=QZwneRb-zqA&list=PLFt_AvWsXl0dPhqVsKt1Ni_46ARyiCGSq&index=3&t=2s&ab_channel=SebastianLague
#

import pyglet as pyg
from modules import and_circuit, not_circuit


app_window = pyg.window.Window()
app_window.maximize()

main_batch = pyg.graphics.Batch()


a = and_circuit.AndCircuit('A1')
a.C.monitor = 1
a.A.set(1)
a.B.set(1)


def update(dt):
    """
    This is the main app loop, where objects will be checked and updated.
    :param dt: delta t, passed by pyg.clock.schedule_interval
    """
    pass


@app_window.event
def on_draw():
    app_window.clear()
    main_batch.draw()


if __name__ == '__main__':
    pyg.clock.schedule_interval(update, 1/120.0)
    pyg.app.run()
