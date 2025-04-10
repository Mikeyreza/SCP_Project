import pyglet
import random
from pyglet import shapes

window4 = pyglet.window.Window(600, 400, "Number Matcher")
batch4 = pyglet.graphics.Batch()


class NumberMatcher:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.target = random.randint(1, 100)
        self.user_input = ""
        self.feedback = f"Type: {self.target}"


game = NumberMatcher()

# UI Elements
target_display = pyglet.text.Label(
    "", font_size=36,
    x=window4.width // 2, y=300, anchor_x='center', batch=batch4
)

input_display = pyglet.text.Label(
    "", font_size=32,
    x=window4.width // 2, y=200, anchor_x='center', batch=batch4
)

feedback_display = pyglet.text.Label(
    "", font_size=24,
    x=window4.width // 2, y=100, anchor_x='center', batch=batch4
)

input_box = shapes.Rectangle(
    window4.width // 2 - 100, 175, 200, 50,
    color=(50, 50, 80), batch=batch4
)


@window4.event
def on_draw():
    window4.clear()
    target_display.text = f"Target: {game.target}"
    input_display.text = game.user_input
    feedback_display.text = game.feedback
    batch4.draw()


@window4.event
def on_text(text):
    if text == '\r':  # Enter key
        if game.user_input == str(game.target):
            game.feedback = "Correct! Generating new number..."
            pyglet.clock.schedule_once(lambda dt: game.reset_game(), 0.5)
        else:
            game.feedback = "Wrong! Try again."
    elif text == '\b':  # Backspace
        game.user_input = game.user_input[:-1]
    elif text.isdigit():
        game.user_input += text


pyglet.app.run()
