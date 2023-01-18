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

background = pyg.image.SolidColorImagePattern((70, 68, 72, 255)).create_image(screen_width, screen_height)

main_batch = pyg.graphics.Batch()


x_draw_offset = 30
y_draw_offset = 20
circuit_store = pyg.shapes.Rectangle(x_draw_offset, y_draw_offset, screen_width - 2 * x_draw_offset,
                                     80, color=(46, 45, 47, 255), batch=main_batch)

circuit_name = pyg.gui.TextEntry("Name", x_draw_offset, screen_height - 100, screen_width - 2 * x_draw_offset,
                                 color=(80, 78, 83, 255), batch=main_batch, text_color=(253, 255, 247, 255))

draw_area = pyg.shapes.BorderedRectangle(x_draw_offset, y_draw_offset + 80 + 20, screen_width - 2 * x_draw_offset,
                                         screen_height - 250, border=10, border_color=(111, 108, 113, 255),
                                         color=(53, 52, 54, 255), batch=main_batch)


key_handler = pyg.window.key.KeyStateHandler()
mouse_handler = pyg.window.mouse.MouseStateHandler()
"""
mouse_handler notes:
If a button is pressed then this handler holds a True value for it. If the window loses focus,
all buttons will be reset to False in order to avoid a “sticky” button state.
If holding down lmb:
>>> mouse_handler[pyg.window.mouse.LEFT] == true
>>> mouse_handler[pyg.window.mouse.RIGHT] == false
"""

app_window.push_handlers(key_handler)
app_window.push_handlers(mouse_handler)


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
    # if mouse_handler[pyg.window.mouse.LEFT]:
    #     print("LMB")
    # if mouse_handler[pyg.window.mouse.RIGHT]:
    #     print("RMB")
    if circuit_name.on_mouse_press()
    pass


@app_window.event
def on_draw():
    app_window.clear()
    background.blit(0, 0)
    main_batch.draw()


if __name__ == '__main__':
    pyg.clock.schedule_interval(update, 1 / 120.0)
    pyg.app.run()
