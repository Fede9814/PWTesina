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
                self.cors = j[4]
                self.sens = j[5]
                break;
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
            if(self.sens == "in"):
                if(self.cors == "left"):
                    cube = arcade.load_texture("../Concept Art/Blocks/road1.png")
                    cube.draw_scaled(self.center_x, self.center_y)
                if(self.cors == "right"):
                    cube = arcade.load_texture("../Concept Art/Blocks/road2.png")
                    cube.draw_scaled(self.center_x, self.center_y)
            if(self.sens == "out"):
                if(self.cors == "left"):
                    cube = arcade.load_texture("../Concept Art/Blocks/road3.png")
                    cube.draw_scaled(self.center_x, self.center_y)
                if(self.cors == "right"):
                    cube = arcade.load_texture("../Concept Art/Blocks/road4.png")
                    cube.draw_scaled(self.center_x, self.center_y)
            
        if(self.val == 4):
            cube = arcade.load_texture("../Concept Art/Blocks/stop.png")
            cube.draw_scaled(self.center_x, self.center_y)
        if(self.val == 5):
            cube = arcade.load_texture("../Concept Art/Blocks/road.png")
            cube.draw_scaled(self.center_x, self.center_y)
        self.cube = cube
    
#    def next_step(self):
#        for j in points:
#            if(j[0] == self.pos_x and j[1] == self.pos_y):
#                if(self.pos == "nord"):
#                    if(self.sens == "in"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):
#                    if(self.sens == "out"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):
#                if(self.pos == "sud"):
#                    if(self.sens == "in"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):
#                    if(self.sens == "out"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):
#                if(self.pos == "est"):
#                    if(self.sens == "in"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):
#                    if(self.sens == "out"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):
#                if(self.pos == "ovest"):
#                    if(self.sens == "in"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):
#                    if(self.sens == "out"):
#                        if(self.cors == "left"):
#                        if(self.cors == "right"):

