import arcade
import math
import os
import numpy
import random

class fov():
    def __init__(self, center_x, center_y, angle):
        self.shape_list = []
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle

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


    


        