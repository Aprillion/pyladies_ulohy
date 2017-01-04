import pyglet

WIDTH = 800
HEIGHT = 600

objects = []
batch = pyglet.graphics.Batch()

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


def draw():
    window.clear()
    batch.draw()

window.push_handlers(
    on_draw=draw
)

pyglet.app.run()
