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

display = pyg.canvas.Display()
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height

app_window = pyg.window.Window(resizable=True)
app_window.maximize()

background = pyg.image.SolidColorImagePattern((169, 169, 169, 255)).create_image(screen_width, screen_height)

main_batch = pyg.graphics.Batch()

circuit_store = pyg.shapes.Rectangle(10, 10, screen_width - 20, 80, color=(54, 69, 79, 255),
                                     batch=main_batch)
circuit_name = pyg.gui.TextEntry("Name", 10, screen_height - 90, screen_width - 20, color=(54, 69, 79, 255),
                                 batch=main_batch, text_color=(169, 169, 169, 255))
circuit_name.on_text("aa")


a = and_circuit.AndCircuit('A1')
a.outputs[0].monitor = 1
a.inputs[0].set(1)
a.inputs[1].set(1)

n = not_circuit.NotCircuit('N1')
a.outputs[0].connect(n.inputs[0])
n.outputs[0].monitor = 1
a.inputs[0].set(0)
print("done")


def update(dt):
    """
    This is the main app loop, where objects will be checked and updated.
    :param dt: delta t, passed by pyg.clock.schedule_interval
    """
    pass


@app_window.event
def on_draw():
    app_window.clear()
    background.blit(0, 0)
    main_batch.draw()


if __name__ == '__main__':
    pyg.clock.schedule_interval(update, 1 / 120.0)
    pyg.app.run()
