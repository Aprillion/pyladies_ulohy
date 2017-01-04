import pyglet

WIDTH = 800
HEIGHT = 600

spaceship_img = pyglet.image.load('playerShip1_blue.png')
spaceship_img.anchor_x = spaceship_img.width // 2
spaceship_img.anchor_y = spaceship_img.height // 2

pressed_keys = set()
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
        self.x = window.width // 2
        self.y = window.height // 2
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.window = window
        self.sprite = pyglet.sprite.Sprite(spaceship_img, batch=batch)
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - self.rotation

    def tick(self, dt):
        # TODO: podivej se do pressed_keys
        pass


def tick_all(dt):
    for obj in objects:
        obj.tick(dt)

pyglet.clock.schedule(tick_all)


objects.append(Spaceship(window))

pyglet.app.run()
