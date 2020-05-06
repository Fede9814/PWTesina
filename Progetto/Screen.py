import arcade
import os

from map import *

class Screen_Class(arcade.Window):

    def __init__(self):

        super().__init__(width=1920, height=1080, title="Traffic Simulator", fullscreen=False)

    def on_draw(self):
        arcade.start_render()
        y = 1050;
        for j in map:
            x = 30;
            for i in j:
                if(i == 0):
                    arcade.draw_rectangle_filled(x, y, 60, 60, arcade.color.GREEN)
                if(i == 1):
                    arcade.draw_rectangle_filled(x, y, 60, 60, arcade.color.CYAN)
                if(i == 2):
                    arcade.draw_rectangle_filled(x, y, 60, 60, arcade.color.ORANGE)
                if(i == 3):
                    arcade.draw_rectangle_filled(x, y, 60, 60, arcade.color.GRAY)
                if(i == 4):
                    arcade.draw_rectangle_filled(x, y, 60, 60, arcade.color.RED)
                x = x + 60
            y = y - 60

    def on_key_press(self, key, modifiers):
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)