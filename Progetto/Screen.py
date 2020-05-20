import arcade
import os

from map import *
from cube import *
from car import *

class window(arcade.Window):

    def __init__(self):
        super().__init__(width=1920, height=1080, title="Traffic Simulator", fullscreen=False)
        self.cube_list = []
        self.car_list = None

    def setup(self):
        y = 1050;
        for j in map:
            x = 30;
            for i in j:
                self.cube_list.append(cube(x-30, y-30, x, y, i))
                x = x + 60
            y = y - 60  

        self.car_list = arcade.SpriteList()

        auto = car("../Concept Art/Blocks/car.png", 1)
        auto.setup(self.cube_list)
        self.car_list.append(auto)

        auto = car("../Concept Art/Blocks/car.png", 1)
        auto.setup(self.cube_list)
        self.car_list.append(auto)

        auto = car("../Concept Art/Blocks/car.png", 1)
        auto.setup(self.cube_list)
        self.car_list.append(auto)
    
    def on_draw(self):       
        arcade.start_render()
        for cube in self.cube_list:
            cube.recognition(cube.pos_x, cube.pos_y)
        self.car_list.draw()

    def on_update(self, delta_time=0.50):
        self.car_list.update()
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)
    
