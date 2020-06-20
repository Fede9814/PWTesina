import arcade
import math
import os
import numpy
import random

class fov():
    def __init__(self, center_x, center_y, angle):
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle

    def setup(self):
        self.sprite = arcade.Sprite("../Concept Art/Blocks/end.png", 1)
        self.sprite.alpha = 0
        self.sprite.center_x = self.center_x
        self.sprite.center_y = self.center_y

    def move(self, change_x: float, change_y: float):
        self.sprite.center_x += change_x
        self.sprite.center_y += change_y

    def set_angle(self, value):
        self.sprite.angle = value
     