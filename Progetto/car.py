import arcade
import math
import os
import numpy
import random
from fov import *

class car(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.frame_count = 0

        
    def setup(self, cube_list):
        self.cube_list = cube_list

        self.center_x, self.center_y = self.spawn()
        self.angle = 0 
        self.fov = fov(self.center_x, self.center_y, self.angle)
        self.fov.setup()
        
        
    
    def update(self, delta_time=0.50):
        self.frame_count += 1
        self.initial_speed = 5

        start_x = self.center_x
        start_y = self.center_y

        dest_x = None
        dest_y = None
        temp_x = None
        temp_y = None

        for cube in self.cube_list:
            if(cube.pos_x <= self.center_x and cube.pos_x + 60 > self.center_x and cube.pos_y <= self.center_y and cube.pos_y + 60 > self.center_y):
                if(cube.name == "strada" or cube.name == "start"):
                    temp_x = cube.next_right_x
                    temp_y = cube.next_right_y
                else:
                    temp_x = self.tempdestx
                    temp_y = self.tempdesty
                break

        for cube in self.cube_list:
            if(cube.pos_x == temp_x and cube.pos_y == temp_y):
                dest_x = cube.center_x
                dest_y = cube.center_y
                self.tempdestx = temp_x
                self.tempdesty = temp_y
                break
        
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        if self.frame_count % 1 == 0:
            
            self.angle = math.degrees(angle)
            self.fov.set_angle(self.angle)

            self.change_x = math.cos(angle) * self.initial_speed 
            self.change_y = math.sin(angle) * self.initial_speed

            self.center_x = self.center_x + self.change_x
            self.center_y = self.center_y + self.change_y

            self.fov.move(self.change_x, self.change_y)
            

    def spawn(self):
        spawn = random.randint(1, 8)

        if(spawn == 1):
            start_spn_x = random.randint(850, 890)
            start_spn_y = 1079
        if(spawn == 2):
            start_spn_x = random.randint(910, 950)
            start_spn_y = 1079
        if(spawn == 3):
            start_spn_x = 1919
            start_spn_y = random.randint(550, 590)
        if(spawn == 4):
            start_spn_x = 1919
            start_spn_y = random.randint(610, 650)
        if(spawn == 5):
            start_spn_x = random.randint(970, 1010)
            start_spn_y = 1
        if(spawn == 6):
            start_spn_x = random.randint(1030, 1070)
            start_spn_y = 1
        if(spawn == 7):
            start_spn_x = 1
            start_spn_y = random.randint(430, 470)
        if(spawn == 8):
            start_spn_x = 1
            start_spn_y = random.randint(490, 530)
        return start_spn_x, start_spn_y
        
    


