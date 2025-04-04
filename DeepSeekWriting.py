import pyglet
from pyglet import shapes

# Window
window = pyglet.window.Window(height=1080, width=1920)
batch = pyglet.graphics.Batch()

# Images
character = pyglet.resource.image("guy.png")
character.width = 600
character.height = 600

# Total Status Bar Variables
bar_width = window.width * 0.8  # 80% of window width
bar_height = 30
bar_x = (window.width - bar_width) / 2
bar_y = window.height - 100  # 50 pixels from top

# Module Bar Variables
mbar_width = window.width * 0.4
mbar_height = 30
mbar_x = bar_x * 5

mbar_y_1 = window.height - 275
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
                         x=window.width // 2,
                         y=bar_y + bar_height + 10,
                         anchor_x='center',
                         anchor_y='bottom',
                         batch=batch)
m1_label = pyglet.text.Label('O2 Level',
                         font_name='Arial',
                         font_size=24,
                         x=mbar_x+window.width // 5,
                         y=mbar_y_1 + mbar_height + 10,
                         anchor_x='center',
                         anchor_y='bottom',
                         batch=batch)
m2_label = pyglet.text.Label('CO2 Level',
                         font_name='Arial',
                         font_size=24,
                         x=mbar_x+window.width // 5,
                         y=mbar_y_2 + mbar_height + 10,
                         anchor_x='center',
                         anchor_y='bottom',
                         batch=batch)
m3_label = pyglet.text.Label('Brody-ness Level',
                         font_name='Arial',
                         font_size=24,
                         x=mbar_x+window.width // 5,
                         y=mbar_y_3 + mbar_height + 10,
                         anchor_x='center',
                         anchor_y='bottom',
                         batch=batch)
m4_label = pyglet.text.Label('Document Management Percentage',
                         font_name='Arial',
                         font_size=24,
                         x=mbar_x+window.width // 5,
                         y=mbar_y_4 + mbar_height + 10,
                         anchor_x='center',
                         anchor_y='bottom',
                         batch=batch)

# Progress variables
progress = 0
progress_small = 0
progress_max = 100
progress_max_small = 20
speed = 0.5

def update(dt):
    global progress
    global progress_small
    progress = (progress + speed) % progress_max
    progress_small = (progress_small + speed) % progress_max_small
    foreground.width = (progress / progress_max) * bar_width
    foreground.color = (int(252-(progress / progress_max)*252), int((progress / progress_max)*252), 0)
    print(foreground.color)
    foreground_1.width = (progress_small / progress_max_small) * mbar_width
    foreground_2.width = (progress_small / progress_max_small) * mbar_width
    foreground_3.width = (progress_small / progress_max_small) * mbar_width
    foreground_4.width = (progress_small / progress_max_small) * mbar_width

@window.event
def on_draw():
    window.clear()
    batch.draw()
    character.blit(x=150, y=175)

# Schedule the update function
pyglet.clock.schedule_interval(update, 1/60.0)

# Run the application
pyglet.app.run()