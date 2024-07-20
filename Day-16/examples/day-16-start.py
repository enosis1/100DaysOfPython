# from turtle import Screen, Turtle
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("purple")
# timmy.forward(100)
# timmy.left(120)
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.align = "r"
table.set_style(prettytable.MSWORD_FRIENDLY)
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
print(table)
