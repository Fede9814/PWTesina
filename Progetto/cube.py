import arcade
from map import *

class cube():
    def __init__(self, pos_x, pos_y, center_x, center_y, val):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.center_x = center_x
        self.center_y = center_y
        self.val = val
        self.recognition(self.pos_x, self.pos_y)

    def recognition(self, pos_x, pos_y):
        for j in points:
            if(j[0] == pos_x and j[1] == pos_y):
                self.name = j[2] 
                self.pos = j[3]
        cube = None
        if(self.val == 0):
            cube = arcade.load_texture("../Concept Art/Blocks/bound.png")
            cube.draw_scaled(self.center_x, self.center_y)
        if(self.val == 1):
            cube = arcade.load_texture("../Concept Art/Blocks/start.png")
            cube.draw_scaled(self.center_x, self.center_y)
        if(self.val == 2):
            cube = arcade.load_texture("../Concept Art/Blocks/end.png")
            cube.draw_scaled(self.center_x, self.center_y)
        if(self.val == 3):
            cube = arcade.load_texture("../Concept Art/Blocks/road.png")
            cube.draw_scaled(self.center_x, self.center_y)
        if(self.val == 4):
            cube = arcade.load_texture("../Concept Art/Blocks/stop.png")
            cube.draw_scaled(self.center_x, self.center_y)
        self.cube = cube


    
    

        