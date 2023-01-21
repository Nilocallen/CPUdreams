import pyglet.shapes
#from modules.gui import rectangle_button


class CircuitStore:
    def __init__(self, x_draw_offset, y_draw_offset, screen_width, batch):
        self.circuits = list()  # A list of lists.  Can store many pages of circuits. circuits[page][idx]
        self.current_page = 0

        self.shape = pyglet.shapes.Rectangle(x_draw_offset, y_draw_offset, screen_width - 2 * x_draw_offset,
                                             50, color=(46, 45, 47, 255), batch=batch)

    #def update(self):
        #for circuit in self.circuits[self.current_page]:
            #circuit_button = rectangle_button.RectangleButton()
