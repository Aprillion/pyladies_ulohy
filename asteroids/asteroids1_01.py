import pyglet

WIDTH = 800
HEIGHT = 600

spaceship_img = pyglet.image.load('playerShip1_blue.png')

objects = []
batch = pyglet.graphics.Batch()

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


def draw():
    window.clear()
    batch.draw()

window.push_handlers(
    on_draw=draw
)


class Spaceship:
    def __init__(self, window):
        self.window = window
        self.sprite = pyglet.sprite.Sprite(spaceship_img, batch=batch)

objects.append(Spaceship(window))

pyglet.app.run()
