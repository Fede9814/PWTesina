import arcade
import os
import pyglet
from car import *

from map import *
from cube import *
from car import *

class window(arcade.Window):

    def __init__(self):
        super().__init__(width=1920, height=1080, title="Traffic Simulator", fullscreen=False)
        self.cube_list = []
        self.car_list = None
        self.change = 1
        self.current_status = 1
        self.frame_count = 0

    def setup(self):
        y = 1050
        for j in map:
            x = 30
            for i in j:
                self.cube_list.append(cube(x-30, y-30, x, y, i))
                x = x + 60
            y = y - 60  
      

        self.car_list = arcade.SpriteList()

        auto1 = car("../car_1.png", 1)
        auto2 = car("../car_2.png", 1)
        auto3 = car("../car_3.png", 1)
        auto4 = car("../car_4.png", 1)
        auto5 = car("../car_5.png", 1)
        auto6 = car("../car_6.png", 1)

        auto1.setup(self.cube_list, self.car_list)
        auto2.setup(self.cube_list, self.car_list)
        auto3.setup(self.cube_list, self.car_list)
        auto4.setup(self.cube_list, self.car_list)
        auto5.setup(self.cube_list, self.car_list)
        auto6.setup(self.cube_list, self.car_list)

        self.car_list.append(auto1)
        self.car_list.append(auto2)
        self.car_list.append(auto3)
        self.car_list.append(auto4)
        self.car_list.append(auto5)
        self.car_list.append(auto6)

        auto = numpy.random.choice(self.car_list, p=[0.165, 0.165, 0.165, 0.165, 0.165, 0.175])

    def on_draw(self):       
        arcade.start_render()
        for cube in self.cube_list:
            cube.recognition(cube.pos_x, cube.pos_y)
        for car in self.car_list:
            car.fov.sprite.draw()
        self.car_list.draw()

    def on_update(self, delta_time=0.50):
        self.frame_count += 1
        if(self.frame_count % 60 == 0):
            for cube in self.cube_list:
                if(cube.val == 4):
                    cube.change_status(self.current_status)
            if(self.current_status < 4):
                self.current_status += 1
            else:
                self.current_status = 1

        for car in self.car_list:
            car.set_car_list(self.car_list)
        
        self.car_list.update()
        for car in self.car_list:
            car.fov.sprite.update()
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if key == arcade.key.S:
            if(self.change == 1):
                for auto in self.car_list:
                    auto.frame_up = False
                self.change = 0  
            else:
                for auto in self.car_list:
                    auto.frame_up = True 
                self.change = 1   
        
        if key == arcade.key.C:
            if(self.change == 1):
                for auto in self.car_list:
                    if(auto.fov.sprite.alpha != 0):
                        auto.fov.sprite.alpha = 0
                self.change = 0  
            else:
                for auto in self.car_list:
                    if(auto.fov.sprite.alpha == 0):
                        auto.fov.sprite.alpha = 255 
                self.change = 1   

        if key == arcade.key.K:
    
            auto = car("../Concept Art/Blocks/car.png", 1)
            auto.setup(self.cube_list, self.car_list)
            self.car_list.append(auto)

    def set_update_rate(self, rate: float):

        pyglet.clock.unschedule(self.update)
        pyglet.clock.schedule_interval(self.update, rate)
        pyglet.clock.unschedule(self.on_update)
        pyglet.clock.schedule_interval(self.on_update, rate)
