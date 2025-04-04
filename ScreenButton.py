import pyglet

pressedImage = pyglet.resource.image("pressed.jpg")
unpressedImage = pyglet.resource.image("unpressed.jpg")

class ScreenButton(pyglet.gui.PushButton):
    def __init__(self, x: int, y: int, pressed: pyglet.resource.image, unpressed: pyglet.resource.image):
        super().__init__(x, y, pressed, unpressed)
