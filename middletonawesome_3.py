import pyglet
import random
from pyglet import shapes

# Window
window1 = pyglet.window.Window(height=640, width=768)
window1.set_location(0, 0)
batch = pyglet.graphics.Batch()

'''
# Images
character = pyglet.resource.image("guy.png")
character.width = 600
character.height = 600
'''

# Total Status Bar Variables
bar_width = window1.width * 0.8  # 80% of window1 width
bar_height = 30
bar_x = (window1.width - bar_width) / 2
bar_y = window1.height - 100  # 50 pixels from top

# Module Bar Variables
mbar_width = window1.width * 0.4
mbar_height = 30
mbar_x = bar_x * 5

mbar_y_1 = window1.height - 250
mbar_y_2 = mbar_y_1 - 100
mbar_y_3 = mbar_y_2 - 100
mbar_y_4 = mbar_y_3 - 100

# Total Status Bar Components
background = shapes.Rectangle(bar_x, bar_y, bar_width, bar_height,
                             color=(50, 50, 50), batch=batch)
foreground = shapes.Rectangle(bar_x, bar_y, 0, bar_height,
                             color=(0, 200, 0), batch=batch)
border = shapes.Rectangle(bar_x, bar_y, bar_width, bar_height,
                         color=(255, 255, 255), batch=batch)
border.opacity = 128  # Semi-transparent

# Module Bar 1
background_1 = shapes.Rectangle(mbar_x, mbar_y_1, mbar_width, mbar_height,
                                color=(50, 50, 50), batch=batch)
foreground_1 = shapes.Rectangle(mbar_x, mbar_y_1, 0, mbar_height,
                                color=(0, 200, 0), batch=batch)
border_1 = shapes.Rectangle(mbar_x, mbar_y_1, mbar_width, mbar_height,
                            color=(255, 255, 255), batch=batch)
border_1.opacity = 128

# Module Bar 2
background_2 = shapes.Rectangle(mbar_x, mbar_y_2, mbar_width, mbar_height,
                                color=(50, 50, 50), batch=batch)
foreground_2 = shapes.Rectangle(mbar_x, mbar_y_2, 0, mbar_height,
                                color=(0, 200, 0), batch=batch)
border_2 = shapes.Rectangle(mbar_x, mbar_y_2, mbar_width, mbar_height,
                            color=(255, 255, 255), batch=batch)
border_2.opacity = 128

# Module Bar 3
background_3 = shapes.Rectangle(mbar_x, mbar_y_3, mbar_width, mbar_height,
                                color=(50, 50, 50), batch=batch)
foreground_3 = shapes.Rectangle(mbar_x, mbar_y_3, 0, mbar_height,
                                color=(0, 200, 0), batch=batch)
border_3 = shapes.Rectangle(mbar_x, mbar_y_3, mbar_width, mbar_height,
                            color=(255, 255, 255), batch=batch)
border_3.opacity = 128

# Module Bar 4
background_4 = shapes.Rectangle(mbar_x, mbar_y_4, mbar_width, mbar_height,
                                color=(50, 50, 50), batch=batch)
foreground_4 = shapes.Rectangle(mbar_x, mbar_y_4, 0, mbar_height,
                                color=(0, 200, 0), batch=batch)
border_4 = shapes.Rectangle(mbar_x, mbar_y_4, mbar_width, mbar_height,
                            color=(255, 255, 255), batch=batch)
border_4.opacity = 128

# Labels
total_label = pyglet.text.Label('Life Support Status',
                                font_name='Arial',
                                font_size=24,
                                x=window1.width // 2,
                                y=bar_y + bar_height + 10,
                                anchor_x='center',
                                anchor_y='bottom',
                                batch=batch)
m1_label = pyglet.text.Label('O2 / CO2 Balance',
                             font_name='Arial',
                             font_size=24,
                             x=mbar_x + window1.width // 5,
                             y=mbar_y_1 + mbar_height + 10,
                             anchor_x='center',
                             anchor_y='bottom',
                             batch=batch)
m2_label = pyglet.text.Label('Temperature',
                             font_name='Arial',
                             font_size=24,
                             x=mbar_x + window1.width // 5,
                             y=mbar_y_2 + mbar_height + 10,
                             anchor_x='center',
                             anchor_y='bottom',
                             batch=batch)
m3_label = pyglet.text.Label('Radiation',
                             font_name='Arial',
                             font_size=24,
                             x=mbar_x + window1.width // 5,
                             y=mbar_y_3 + mbar_height + 10,
                             anchor_x='center',
                             anchor_y='bottom',
                             batch=batch)
m4_label = pyglet.text.Label('Electricity',
                             font_name='Arial',
                             font_size=24,
                             x=mbar_x + window1.width // 5,
                             y=mbar_y_4 + mbar_height + 10,
                             anchor_x='center',
                             anchor_y='bottom',
                             batch=batch)

# Progress variables
progress = 0
progress_small = 0
progress_max = 100
progress_max_small = 20

def update(dt):
    update_bars()

def update_bars():
    global progress
    global progress_small
    speed = calculate_speed()
    progress = (progress + speed) % progress_max
    progress_small = (progress_small + speed) % progress_max_small
    foreground.width = (progress / progress_max) * bar_width
    foreground.color = (int(252 - (progress / progress_max) * 252), int((progress / progress_max) * 252), 0)
    foreground_1.width = (progress_small / progress_max_small) * mbar_width
    foreground_2.width = (progress_small / progress_max_small) * mbar_width
    foreground_3.width = (progress_small / progress_max_small) * mbar_width
    foreground_4.width = (progress_small / progress_max_small) * mbar_width

@window1.event
def on_draw():
    window1.clear()
    batch.draw()
    #character.blit(x=150, y=175)

###############
#SECOND WINDOW#
###############

window2 = pyglet.window.Window(height=650, width=768)
window2.set_location(0, 710)
batch2 = pyglet.graphics.Batch()

# Game state
score = 0
current_question = None
answer_buttons = []
correct_answer = None

# Colors
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
GREEN = (0, 255, 0, 255)
RED = (255, 0, 0, 255)
BLUE = (0, 0, 255, 255)
GRAY = (200, 200, 200, 255)

# UI Elements
question_label = pyglet.text.Label(
    "", font_size=24, x=window2.width // 2, y=window2.height - 100,
    anchor_x='center', anchor_y='center', batch=batch2, color=BLACK
)

score_label = pyglet.text.Label(
    f"Score: {score}", font_size=20, x=20, y=window2.height - 30,
    batch=batch2, color=BLACK
)


def generate_question():
    """Generate a random math question and return the correct answer."""
    global current_question, correct_answer

    # Randomly choose an operation
    operations = ['+', '-', '*', '/']
    op = random.choice(operations)

    # Generate numbers based on the operation to avoid division by zero or negative results
    if op == '+':
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        correct = a + b
    elif op == '-':
        a = random.randint(1, 50)
        b = random.randint(1, a)  # Ensure non-negative result
        correct = a - b
    elif op == '*':
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        correct = a * b
    elif op == '/':
        b = random.randint(1, 10)
        correct = random.randint(1, 10)
        a = correct * b  # Ensure exact division

    current_question = f"{a} {op} {b} = ?"
    correct_answer = correct

    # Generate two incorrect answers
    wrong1 = correct + random.randint(1, 10)
    wrong2 = correct - random.randint(1, 10)
    if wrong2 == correct:
        wrong2 -= 5  # Ensure wrong answers are distinct

    # Shuffle the answer choices
    answers = [correct, wrong1, wrong2]
    random.shuffle(answers)

    return answers


def setup_question():
    """Set up the question and answer buttons."""
    global answer_buttons

    # Clear previous buttons
    answer_buttons = []

    # Generate new question and answers
    answers = generate_question()
    question_label.text = current_question
    question_label.color =  WHITE

    # Create answer buttons
    button_width = 200
    button_height = 60
    spacing = 20
    start_y = window2.height // 2

    for i, answer in enumerate(answers):
        button_x = window2.width // 2 - button_width // 2
        button_y = start_y - i * (button_height + spacing)

        # Create a background rectangle for the button
        rect = shapes.Rectangle(
            button_x, button_y, button_width, button_height,
            batch=batch2
        )

        # Create the answer label
        answer_text = pyglet.text.Label(
            str(answer), font_size=20,
            x=button_x + button_width // 2, y=button_y + button_height // 2,
            anchor_x='center', anchor_y='center', batch=batch2, color=BLACK
        )

        # Store button info (rectangle, label, and answer value)
        answer_buttons.append((rect, answer_text, answer))


def check_answer(answer):
    """Check if the selected answer is correct."""
    global score

    if answer == correct_answer:
        score += 1
        score_label.text = f"Score: {score}"
        score_label.color = WHITE
        setup_question()  # Move to the next question
    else:
        # Flash red to indicate wrong answer (optional)
        pass

def calculate_speed():
    return score/5

@window2.event
def on_draw():
    window2.clear()
    batch2.draw()


@window2.event
def on_mouse_press(x, y, button, modifiers):
    for rect, _, answer in answer_buttons:
        if (rect.x <= x <= rect.x + rect.width and
                rect.y <= y <= rect.y + rect.height):
            check_answer(answer)


# Start the game
setup_question()

################
# WINDOW THREE #
################

# Configuration
# Configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
IMAGE_DISPLAY_TIME = 2.0  # seconds per image


class ImageSlideshow:
    def __init__(self):
        self.window = pyglet.window.Window(
            height=640, width=768
        )

        self.window.set_location(768, 0)

        # Load your images (replace with your own image paths)
        self.images = [
            pyglet.resource.image("flower3.png"),  # Replace with actual paths
            pyglet.resource.image("flower2.png"),
            pyglet.resource.image("flower1.png")
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
        pyglet.clock.schedule_interval(self.next_image, IMAGE_DISPLAY_TIME)

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

game2 = ImageSlideshow()

#################
# WINDOW FOUR!! #
#################

window4 = pyglet.window.Window(height=650, width=768)
window4.set_location(768, 710)
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

# Schedule the update function
pyglet.clock.schedule_interval(update, 1/60.0)

# Run the application
pyglet.app.run()