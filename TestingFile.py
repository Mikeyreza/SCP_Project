import pyglet
from pyglet import shapes
import random

# Create a window2
window3 = pyglet.window.Window(800, 600, "Algebraic Equation Solver")
batch3 = pyglet.graphics.Batch()


# Game state
class GameState:
    def __init__(self):
        self.reset_problem()
        self.selected_num1 = None
        self.selected_num2 = None
        self.message = "Select two numbers to solve the equation!"
        self.message_color = (255, 255, 255, 255)

    def reset_problem(self):
        # Generate random equation parameters
        self.operation = random.choice(['+', '-', '*', '/'])
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        # Calculate target based on operation
        if self.operation == '+':
            self.target = self.num1 + self.num2
        elif self.operation == '-':
            self.target = self.num1 - self.num2
        elif self.operation == '*':
            self.target = self.num1 * self.num2
        elif self.operation == '/':
            # Ensure division results in integer
            self.target = self.num1
            self.num1 = self.num1 * self.num2

        # Create options (include correct numbers and some random ones)
        self.options = list({self.num1, self.num2,
                             random.randint(1, 15),
                             random.randint(1, 15),
                             random.randint(1, 15)})
        random.shuffle(self.options)

    def check_solution(self, a, b):
        # Check if the selected numbers solve the equation
        try:
            if self.operation == '+':
                return a + b == self.target
            elif self.operation == '-':
                return a - b == self.target
            elif self.operation == '*':
                return a * b == self.target
            elif self.operation == '/':
                return a / b == self.target
        except ZeroDivisionError:
            return False


game_state = GameState()

# UI Elements
equation_label = pyglet.text.Label(
    "", font_size=24, x=window3.width // 2, y=500,
    anchor_x='center', anchor_y='center', batch=batch3
)

target_label = pyglet.text.Label(
    "", font_size=24, x=window3.width // 2, y=450,
    anchor_x='center', anchor_y='center', batch=batch3
)

message_label = pyglet.text.Label(
    "", font_size=20, x=window3.width // 2, y=100,
    anchor_x='center', anchor_y='center', batch=batch3
)

# Create number option buttons
option_buttons = []
for i in range(5):
    button = shapes.Rectangle(
        x=150 + i * 120, y=300, width=100, height=80,
        color=(50, 50, 200), batch=batch3
    )
    button_label = pyglet.text.Label(
        "", font_size=24, x=150 + i * 120 + 50, y=340,
        anchor_x='center', anchor_y='center', batch=batch3
    )
    option_buttons.append((button, button_label))

# Create submit button
submit_button = shapes.Rectangle(
    x=window3.width // 2 - 50, y=200, width=100, height=50,
    color=(0, 200, 0), batch=batch3
)
submit_label = pyglet.text.Label(
    "Submit", font_size=20, x=window3.width // 2, y=225,
    anchor_x='center', anchor_y='center', batch=batch3
)


def update_display():
    # Update equation display
    equation_label.text = f"Find numbers where: a {game_state.operation} b = ?"
    target_label.text = f"Target: {game_state.target}"
    message_label.text = game_state.message
    message_label.color = game_state.message_color

    # Update option buttons
    for i, (button, label) in enumerate(option_buttons):
        if i < len(game_state.options):
            label.text = str(game_state.options[i])
            # Highlight selected numbers
            if game_state.options[i] == game_state.selected_num1 or game_state.options[i] == game_state.selected_num2:
                button.color = (200, 50, 50)  # Red for selected
            else:
                button.color = (50, 50, 200)  # Blue for unselected
        else:
            label.text = ""


@window3.event
def on_draw():
    window3.clear()
    batch3.draw()


@window3.event
def on_mouse_press(x, y, button, modifiers):
    # Check option buttons
    for i, (rect, _) in enumerate(option_buttons):
        if (i < len(game_state.options) and
                x >= rect.x and x <= rect.x + rect.width and
                y >= rect.y and y <= rect.y + rect.height):
            num = game_state.options[i]
            if game_state.selected_num1 is None:
                game_state.selected_num1 = num
                game_state.message = f"First number: {num}. Select second number."
                game_state.message_color = (255, 255, 255, 255)
            elif game_state.selected_num2 is None and num != game_state.selected_num1:
                game_state.selected_num2 = num
                game_state.message = f"Selected numbers: {game_state.selected_num1} and {num}"
                game_state.message_color = (255, 255, 255, 255)
            break

    # Check submit button
    if (game_state.selected_num1 is not None and game_state.selected_num2 is not None and
            x >= submit_button.x and x <= submit_button.x + submit_button.width and
            y >= submit_button.y and y <= submit_button.y + submit_button.height):

        if game_state.check_solution(game_state.selected_num1, game_state.selected_num2):
            game_state.message = "Correct! Well done!"
            game_state.message_color = (0, 255, 0, 255)
            pyglet.clock.schedule_once(reset_after_delay, 2.0)
        else:
            game_state.message = "Incorrect. Try again!"
            game_state.message_color = (255, 0, 0, 255)
            game_state.selected_num1 = None
            game_state.selected_num2 = None


def reset_after_delay(dt):
    game_state.reset_problem()
    game_state.selected_num1 = None
    game_state.selected_num2 = None
    game_state.message = "Select two numbers to solve the equation!"
    game_state.message_color = (255, 255, 255, 255)


# Initial display update
update_display()


# Schedule regular updates
def update(dt):
    update_display()


pyglet.clock.schedule_interval(update, 0.1)

pyglet.app.run()