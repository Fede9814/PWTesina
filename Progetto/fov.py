import arcade
import math
import os
import numpy
import random

class fov(arcade.PhysicsEngineSimple):
    def __init__(self, center_x, center_y, angle, car):

        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.car = car

        age_range = [20, 40, 60, 80]
        Speed_range = [1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
        μ_global_range = [0.1, 0.8]
        reaction_time_range = [1.5, 3.0, 4.5]

        fixed_value = 250

        self.age_range = age_range
        self.Speed_range = Speed_range 
        self.fixed_value = fixed_value
        self.μ_global_range = μ_global_range 
        self.reaction_time_range = reaction_time_range

        #fov parameters pickers
        self.age = numpy.random.choice(
            #questo è ok
            self.age_range, p=[0.22, 0.54, 0.10, 0.14])
            #questo è ok
        self.Speed = numpy.random.choice(
            self.Speed_range, p=[0.05, 0.10, 0.35, 0.35, 0.10, 0.05])
            #questo è ok
        self.reaction_time = numpy.random.choice(
            self.reaction_time_range, p=[0.8, 0.18, 0.02])
            #questo è ok
        self.μ_value = numpy.random.choice(
            self.μ_global_range, p=[0.01, 0.99])
            #questo è ok
        self.skill_factor = 0

        #fov calculations
        if self.age == 20 or self.age == 80:
            self.skill_factor = 0.6
        elif self.age == 40:
            self.skill_factor = 0.0
        elif self.age == 60:
            self.skill_factor = 0.2
        #print("Skill", self.skill_factor)

        if self.skill_factor == 0.6:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 - self.skill_factor))
        #print("R_dist", self.R_dist)
        elif self.skill_factor == 0.0:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 + self.skill_factor))
        #print("R_dist", self.R_dist)
        elif self.skill_factor == 0.2:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 - self.skill_factor))
        #print("R_dist", self.R_dist)

        self.B_dist = ((math.pow(self.Speed, 2.0) /
                        (self.fixed_value * self.μ_value)))
        # print("B_dist",self.B_dist)

        self.FOV_length = self.R_dist + self.B_dist

    
    def setup(self):
        self.sprite = arcade.Sprite("../Concept Art/hitbox.png", self.FOV_length)
        #setta alpha a 0 per nascondere i fov delle macchine
        self.sprite.alpha = 255
        pcx, pcy = self.center_calc(self.car)
        self.sprite.center_x = pcx
        self.sprite.center_y = pcy

    def center_calc(self, car):
        punto_a = car.points[1]
        punto_b = car.points[3]

        punto_a_x = punto_a[0]
        punto_a_y = punto_a[1]
        punto_b_x = punto_b[0]
        punto_b_y = punto_b[1]

        punto_c_x = (punto_a_x + punto_b_x)/2
        punto_c_y = (punto_a_y + punto_b_y)/2

        return punto_c_x, punto_c_y


    def move(self):
        pcx, pcy = self.center_calc(self.car)
        self.sprite.center_x = pcx
        self.sprite.center_y = pcy


    def set_angle(self, value):
        self.sprite.angle = value

    
        