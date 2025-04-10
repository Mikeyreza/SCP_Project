import pyglet
from pyglet import shapes
import random

# Set up the window1
window2 = pyglet.window.Window(800, 600, "Math Quiz Game")
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
            color=GRAY, batch=batch2
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
pyglet.app.run()