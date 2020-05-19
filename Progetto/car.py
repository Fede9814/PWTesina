import arcade
import math
import os
import numpy

class car(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.frame_count = 0

        
    def setup(self, cube_list):
        self.cube_list = cube_list
        
        self.center_x = 840
        self.center_y = 1020
        self.angle = 0 
    
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
                temp_x = cube.next_right_x
                temp_y = cube.next_right_y
                break

        for cube in self.cube_list:
            if(cube.pos_x == temp_x and cube.pos_y == temp_y):
                dest_x = cube.center_x
                dest_y = cube.center_y
                break
        
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        if self.frame_count % 1 == 0:

            self.center_x = start_x
            self.center_y = start_y
            
            self.angle = math.degrees(angle)

            self.change_x = math.cos(angle) * self.initial_speed 
            self.change_y = math.sin(angle) * self.initial_speed

            self.center_x = self.center_x + self.change_x
            self.center_y = self.center_y + self.change_y
    


