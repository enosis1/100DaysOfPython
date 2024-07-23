import random
import turtle as t

import colorgram


def get_colors(colors):
    """Converts the colors from colorgram into a list of tuples of rgb."""
    list_in_colors = []
    for color in colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        if b < 200:
            list_in_colors.append((r, g, b))
    return list_in_colors


def get_random_color(colors):
    return random.choice(colors)


# generated_colors = colorgram.extract("spot_painting.webp", 30)
# colors = get_colors(generated_colors)
colors = [
    (203, 172, 107),
    (153, 181, 196),
    (193, 161, 177),
    (152, 186, 174),
    (214, 204, 111),
    (208, 179, 196),
    (160, 214, 187),
    (114, 123, 186),
    (178, 161, 71),
    (213, 182, 180),
    (98, 98, 97),
    (41, 41, 41),
    (94, 92, 93),
    (201, 207, 43),
    (53, 51, 52),
    (130, 127, 128),
    (105, 105, 107),
    (66, 63, 64),
]


timmy = t.Turtle()
screen = t.Screen()

# SCREEN
screen.colormode(255)
screen.title("Test Title")
screen_size = screen.screensize()
x = 0
y = 0
for cord in screen_size:
    if cord == screen_size[0]:
        x = cord
        continue
    y = cord

print(x, y)


# TURTLE
timmy.speed(0)
timmy.width(10)  # Sets the width of the drawings, even if it's the pen or the dot
timmy.hideturtle()
timmy.penup()  # Does not allow the pen to be down
def timmy_teleport():
    timmy.teleport(-x * 0.55, -y + 100 )
timmy_teleport()
for _ in range(1, 101):
    random_color = random.choice(colors)
    timmy.pencolor(random_color)
    timmy.dot()
    timmy.forward(50)
    print(timmy.pos())
    if _ % 10 == 0:
        y -= 50
        timmy_teleport()


screen.exitonclick()
# Dots should be 20 in size and pace 50 spaces apart.
