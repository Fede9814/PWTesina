import random
import numpy
import os
import time
import math
import arcade

class Pilot():

    def __init__(   self, age_range, Speed_range, fixed_value, 
                    μ_global_range, reaction_time_range, age, 
                    Speed, reaction_time, μ_value, skill_factor):
        
        self.age_range = age_range
        self.Speed_range = Speed_range 
        self.fixed_value = fixed_value
        self.μ_global_range = μ_global_range 
        self.reaction_time_range = reaction_time_range

        age_range =             [20, 40, 60, 80]
        Speed_range =           [0.6, 1.0, 1.6, 2.2, 2.8, 3.6]
        μ_global_range =        [0.1, 0.8]
        reaction_time_range =   [1.5, 3.0, 4.5]
        fixed_value =           250


        self.age = numpy.random.choice(
            self.age_range, p=[0.22, 0.54, 0.10, 0.14])

        self.Speed = numpy.random.choice(
            self.Speed_range, p=[0.09, 0.15, 0.3, 0.3, 0.1, 0.06])

        self.reaction_time = numpy.random.choice(
            self.reaction_time_range, p=[0.8, 0.18, 0.02])

        self.μ_value = numpy.random.choice(
            self.μ_global_range, p=[0.01, 0.99])

        self.skill_factor = 0

    def FOV(self, R_dist, B_dist, FOV_length):

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

        FOV_length = self.R_dist + self.B_dist
        print(FOV_length)

"""    def Angle(self):

        dodge_turn_direction = ["L", "R", "S"]
        dodge_angle_range = [1, 10, 20]
        self.dodge_turn = numpy.random.choice(
            dodge_turn_direction, p=[0.48, 0.48, 0.04])

        if self.dodge_turn == "L":
            dodge_angle_value = numpy.random.choice(
                dodge_angle_range, p=[0.30, 0.30, 0.40])

        elif self.dodge_turn == "R":
            dodge_angle_value = (numpy.random.choice(
                dodge_angle_range, p=[0.30, 0.30, 0.40])) * -1

        elif self.dodge_turn == "S":
            dodge_angle_value = 0
        
        return dodge_angle_value
"""

"""class fov():

    def __init__(self, center_x, center_y, angle):
        self.shape_list = []
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        
        age_range = [20, 40, 60, 80]
        Speed_range = [0.6, 1.0, 1.6, 2.2, 2.8, 3.6]
        self.fixed_value = 250
        μ_global_range = [0.1, 0.8]
        reaction_time_range = [1.5, 3.0, 4.5]

        self.age = numpy.random.choice(
            age_range, p=[0.22, 0.54, 0.10, 0.14])

        self.Speed = numpy.random.choice(
            Speed_range, p=[0.09, 0.15, 0.3, 0.3, 0.1, 0.06])

        self.reaction_time = numpy.random.choice(
            reaction_time_range, p=[0.8, 0.18, 0.02])

        self.μ_value = numpy.random.choice(
            μ_global_range, p=[0.01, 0.99])

        self.skill_factor = 0

    def setup(self):
        self.shape_list = arcade.ShapeElementList()
        self.shape_list.center_x = self.center_x
        self.shape_list.center_y = self.center_y
        shape = arcade.create_rectangle_outline(0, 0, 40, 50, arcade.color.BLUE, 1, 0)
        self.shape_list.append(shape)

    def draw(self):
        self.shape_list.draw()

    def move(self, change_x: float, change_y: float):
        self.shape_list.center_x += change_x
        self.shape_list.center_y += change_y

    def set_angle(self, value):
        self.shape_list.angle = value

    def FOV(self):

        if self.age == 20 or self.age == 80:
            self.skill_factor = 0.6
        elif self.age == 40:
            self.skill_factor = 0.0
        elif self.age == 60:
            self.skill_factor = 0.2
        print("Skill", self.skill_factor)

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

        FOV_length = self.R_dist + self.B_dist

        return FOV_length

    def Angle(self):

        dodge_turn_direction = ["L", "R", "S"]
        dodge_angle_range = [1, 10, 20]
        self.dodge_turn = numpy.random.choice(
            dodge_turn_direction, p=[0.48, 0.48, 0.04])

        if self.dodge_turn == "L":
            dodge_angle_value = numpy.random.choice(
                dodge_angle_range, p=[0.30, 0.30, 0.40])

        elif self.dodge_turn == "R":
            dodge_angle_value = (numpy.random.choice(
                dodge_angle_range, p=[0.30, 0.30, 0.40])) * -1

        elif self.dodge_turn == "S":
            dodge_angle_value = 0
        
        return dodge_angle_value"""



"""        self.car_music = arcade.Sound(self.car_music_list[self.current_car_song], streaming=True)
        self.car_music.play(self.MUSIC_VOLUME)

        self.tir_music = arcade.Sound(self.tir_music_list[self.current_tir_song], streaming=True)
        self.tir_music.play(self.MUSIC_VOLUME)

        self.bike_music = arcade.Sound(self.bike_music_list[self.current_bike_song], streaming=True)
        self.bike_music.play(self.MUSIC_VOLUME)
        self.current_car_song = 0
        self.current_tir_song = 0
        self.current_bike_song = 0"""