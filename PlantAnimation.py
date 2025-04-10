import pyglet
from pyglet import clock

# Configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
IMAGE_DISPLAY_TIME = 2.0  # seconds per image


class ImageSlideshow:
    def __init__(self):
        self.window = pyglet.window.Window(
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            caption="Image Slideshow"
        )

        self.window.set_location(768, 0)

        # Load your images (replace with your own image paths)
        self.images = [
            pyglet.resource.image("flower1.png"),  # Replace with actual paths
            pyglet.resource.image("flower2.png"),
            pyglet.resource.image("flower3.png")
        ]

        self.instruction_label = pyglet.text.Label(
            "Water your plants to keep O2 and CO2 stable",
            font_name='Arial',
            font_size=24,
            x=WINDOW_WIDTH // 2,
            y=WINDOW_HEIGHT - 50,
            anchor_x='center',
            anchor_y='center',
            color=(255, 255, 255, 255)  # White text
        )

        self.button = pyglet.shapes.Circle(
            x=180,
            y=300,
            radius=100,
            color=(30,144,255, 255)
        )

        self.arrow = pyglet.resource.image("waterarrow.png")

        self.button_label = pyglet.text.Label(
            "Water Plant",
            font_name='Arial',
            font_size=20,
            x=self.button.x,
            y=self.button.y,
            anchor_x='center',
            anchor_y='center',
            color=(0,0,205, 255)
        )

        # Scale images to fit window while maintaining aspect ratio
        for i, img in enumerate(self.images):
            self.images[i] = self._scale_image(img)

        self.current_image_index = 0
        self.sprite = pyglet.sprite.Sprite(self.images[0])
        self._center_sprite()

        # Schedule image updates
        clock.schedule_interval(self.next_image, IMAGE_DISPLAY_TIME)

        @self.window.event
        def on_draw():
            self.window.clear()
            self.sprite.draw()
            self.instruction_label.draw()
            self.button.draw()
            self.button_label.draw()
            self.arrow.blit(x=310, y=225, width=200, height=150)

    def _scale_image(self, image):
        """Scale image to fit window while maintaining aspect ratio"""
        scale = min(
            WINDOW_WIDTH / image.width,
            WINDOW_HEIGHT / image.height
        )
        image.width = int(200)
        image.height = int(200)
        return image

    def _center_sprite(self):
        """Center the sprite in the window"""
        self.sprite.x = 500
        self.sprite.y = 200

    def next_image(self, dt):
        """Switch to the next image in the sequence"""
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.sprite.image = self.images[self.current_image_index]
        self._center_sprite()

if __name__ == "__main__":
    slideshow = ImageSlideshow()
    pyglet.app.run()