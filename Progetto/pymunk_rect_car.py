import arcade
import pymunk
import timeit
import math
import os
from test2 import *

class CarPhysicsSprite(arcade.Sprite):
    def __init__(self, pymunk_shape, filename):
        super().__init__(filename, center_x=MyGame.car.center_x, center_y=MyGame.car.center_y)
        positive_y_is_up = True
        self.body = pymunk.Body(mass=0, moment=0)
        self.body.width = (MyGame.car.Sprite + 50)
        self.height = (MyGame.car.Sprite + 50)