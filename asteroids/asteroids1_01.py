import pyglet
import math

WIDTH = 800
HEIGHT = 600
ACCELERATION = 300
ROTATION_SPEED = 200

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


def key_press(key, modificator):
    pressed_keys.add(key)


def key_release(key, modificator):
    pressed_keys.discard(key)


window.push_handlers(
    on_draw=draw,
    on_key_press=key_press,
    on_key_release=key_release
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

    def tick(self, dt):
        if pyglet.window.key.UP in pressed_keys:
            rotation_radians = math.radians(self.rotation)
            self.x_speed += dt * ACCELERATION * math.cos(rotation_radians)
            self.y_speed += dt * ACCELERATION * math.sin(rotation_radians)
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation += dt * ROTATION_SPEED
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation -= dt * ROTATION_SPEED

        self.x += self.x_speed * dt
        self.y += self.y_speed * dt

        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - self.rotation
        pass


def tick_all(dt):
    for obj in objects:
        obj.tick(dt)

pyglet.clock.schedule(tick_all)


objects.append(Spaceship(window))

pyglet.app.run()
