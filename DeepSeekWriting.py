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

mbar_y_1 = window1.height - 275
mbar_y_2 = mbar_y_1 - 200
mbar_y_3 = mbar_y_2 - 200
mbar_y_4 = mbar_y_3 - 200

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
total_label = pyglet.text.Label('Total Life Status',
                                font_name='Arial',
                                font_size=24,
                                x=window1.width // 2,
                                y=bar_y + bar_height + 10,
                                anchor_x='center',
                                anchor_y='bottom',
                                batch=batch)
m1_label = pyglet.text.Label('O2 Level',
                             font_name='Arial',
                             font_size=24,
                             x=mbar_x + window1.width // 5,
                             y=mbar_y_1 + mbar_height + 10,
                             anchor_x='center',
                             anchor_y='bottom',
                             batch=batch)
m2_label = pyglet.text.Label('CO2 Level',
                             font_name='Arial',
                             font_size=24,
                             x=mbar_x + window1.width // 5,
                             y=mbar_y_2 + mbar_height + 10,
                             anchor_x='center',
                             anchor_y='bottom',
                             batch=batch)
m3_label = pyglet.text.Label('Brody-ness Level',
                             font_name='Arial',
                             font_size=24,
                             x=mbar_x + window1.width // 5,
                             y=mbar_y_3 + mbar_height + 10,
                             anchor_x='center',
                             anchor_y='bottom',
                             batch=batch)
m4_label = pyglet.text.Label('Document Management Percentage',
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
    print(foreground.color)
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

window2 = pyglet.window.Window(height=640, width=768)
window2.set_location(0, 700)
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

window3 = pyglet.window.Window(height=640, width=768)
window3.set_location(770, 0)
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

#################
# WINDOW FOUR!! #
#################

window4 = pyglet.window.Window(height=640, width=768)
window4.set_location(770, 700)
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