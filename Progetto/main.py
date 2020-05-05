import arcade
from map import *
from Screen import *

Screen_Class.createWindow()


"""
# Linea verticale ogni 75px
for x in range(0, 1501, 75):
    arcade.draw_line(0, x, 1500, x, arcade.color.BLACK, 1)

# Linea orizzontale ogni 75px
for y in range(0, 1201, 75):
    arcade.draw_line(0, y, 1200, y, arcade.color.BLACK, 1)

"""

for j in points:
    for i in j:
        if j[2] == "exit":
            arcade.draw_rectangle_filled(j[0], j[1], 75, 75, arcade.color.ORANGE)
        if j[2] == "start":
            arcade.draw_rectangle_filled(j[0], j[1], 75, 75, arcade.color.CYAN)
        if j[2] == "semaforo":
            arcade.draw_rectangle_filled(j[0], j[1], 75, 75, arcade.color.RED)
arcade.finish_render()

arcade.run()