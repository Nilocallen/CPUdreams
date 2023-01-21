import pyglet.shapes
import pyglet.text


class RectangleButton:
    def __init__(self, x, y, batch, label_text):
        self.label = None

        width = 80
        height = 40
        if label_text:
            width = 14.5 * len(label_text) + 20
            self.label = pyglet.text.Label(text=label_text, x=x+10, y=y + height * .5, batch=batch,
                                           font_name='Lucida Console', font_size=18)

        self.shape = pyglet.shapes.Rectangle(x, y, width, height, batch=batch, color=(53, 52, 54, 255))


