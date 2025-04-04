import os

import pyglet
import ScreenButton
from gpiozero import Button

#button = Button(21)

window = pyglet.window.Window()
window.width = 1920
window.height = 1080

pressed = pyglet.image.load("pressed.jpg")

unpressed = pyglet.image.load("unpressed.jpg")

batch = pyglet.graphics.Batch()

newButton = pyglet.gui.PushButton(100, 100, pressed, unpressed, batch=batch)

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

label_new = pyglet.text.Label('Its gooning time',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//3, y=window.height//2,
                          anchor_x='center', anchor_y='center')

window.push_handlers(newButton)

@window.event()
def on_draw():
    window.clear()
    label.draw()
    batch.draw()

def brody_draw():
    label_new.draw()

pyglet.app.run()