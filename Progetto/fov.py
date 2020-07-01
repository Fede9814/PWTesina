import pyodbc
import arcade
import math
import os
import numpy
import random
import string
import names
import numpy
import json
import datetime
from car import *

class fov(arcade.PhysicsEngineSimple):
    def __init__(self, center_x, center_y, angle, car):

        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.car = car

        self.age_range = [20, 40, 60, 80]
        self.Speed_range = [1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
        self.μ_global_range = [0.1, 0.8]
        self.reaction_time_range = [1.5, 3.0, 4.5]

        fixed_value = 250

        self.age = numpy.random.choice(self.age_range, p=[0.22, 0.54, 0.10, 0.14])
        self.Speed = numpy.random.choice(self.Speed_range, p=[0.05, 0.10, 0.35, 0.35, 0.10, 0.05])
        self.reaction_time = numpy.random.choice(self.reaction_time_range, p=[0.8, 0.18, 0.02])
        self.μ_value = numpy.random.choice(self.μ_global_range, p=[0.01, 0.99])
        self.skill_factor = 0

        if self.age == 20 or self.age == 80:
            self.skill_factor = 0.6
        elif self.age == 40:
            self.skill_factor = 0.0
        elif self.age == 60:
            self.skill_factor = 0.2

        if self.skill_factor == 0.6:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 - self.skill_factor))
        elif self.skill_factor == 0.0:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 + self.skill_factor))
        elif self.skill_factor == 0.2:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 - self.skill_factor))
        
    def setup(self):

        if self.R_dist < 3.10:
            hitbox_fov = "../Sprites/Hitbox/Hitbox_L70_W30.png"

        elif self.R_dist > 3.11 and self.R_dist < 5.6:
            hitbox_fov = "../Sprites/Hitbox/Hitbox_L80_W30.png"

        elif self.R_dist > 5.7 and self.R_dist < 8.7:
            hitbox_fov = "../Sprites/Hitbox/Hitbox_L120_W30.png"
        
        elif self.R_dist > 8.8 and self.R_dist < 9.8:
            hitbox_fov = "../Sprites/Hitbox/Hitbox_L140_W30.png"
        
        elif self.R_dist > 9.9:
            hitbox_fov = "../Sprites/Hitbox/Hitbox_L100_W30.png"

        self.sprite = arcade.Sprite(hitbox_fov, 1)
        self.sprite.alpha = 0
        pcx, pcy = self.center_calc(self.car)
        self.sprite.center_x = pcx
        self.sprite.center_y = pcy

        self.stop_sprite = arcade.Sprite("../Sprites/Hitbox/Fixed_Hitbox_L20_W30.png", 1)
        self.stop_sprite.alpha = 0
        pcx, pcy = self.center_calc(self.car)
        self.stop_sprite.center_x = pcx
        self.stop_sprite.center_y = pcy

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

        self.stop_sprite.center_x = pcx
        self.stop_sprite.center_y = pcy

    def search_my_cube(self, cube):
        if(cube.pos_x <= self.sprite.center_x and cube.pos_x + 60 > self.sprite.center_x and cube.pos_y <= self.sprite.center_y and cube.pos_y + 60 > self.sprite.center_y):
            self.my_cube = cube.val

    def set_angle(self, value):
        self.sprite.angle = value
        self.stop_sprite.angle = value

    def check_distance(self, car_list):
        in_range = None
        for car in car_list:
            if(car.telaio != self.car.telaio):
                if arcade.check_for_collision(self.sprite, car):
                    in_range = False
                    break
                else:
                    in_range = True
        if(in_range == None):
            in_range = True
        return in_range

    def check_braking(self, car_list):
            braking = None
            collided_car = None
            collision_car = arcade.check_for_collision_with_list(self.stop_sprite, car_list)

            for car in collision_car:
                if(car.telaio != self.car.telaio):
                    collided_car = car
                    braking = True
                    break
                else:
                    braking = False
                    collided_car = self
            return braking, collided_car 

    def check_car_collision (self, car_list):
        skip_collision = None
        for car in car_list:
            if(car.telaio != self.car.telaio):
                if arcade.check_for_collision(self.sprite, car):
                    if(car.collision == True):
                        skip_collision = True
                        break
                    else:
                        skip_collision = False
            
        if (skip_collision == None):
            skip_collision = False

        return skip_collision
    
"""        self.Json_car =  {
                "CarBirthTime":     self.Birth,
                "IDVehicle" :       self.VehicleID,
                "Gender":           self.pilot_sex,
                "Age":              self.true_age,
                "Name":             self.pilot_name,
                "Surname":          self.pilot_surname,
                "Plate":            self.plate,
                "Region":           self.region,
                "Model" :           self.car_model,
                "Displacement" :    self.Displacement,
                "CarTax" :          self.Tax_status,
                "Insurance" :       self.Insurance_status,
                }
"""