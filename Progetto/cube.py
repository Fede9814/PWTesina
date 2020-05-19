import arcade
from map import *

class cube():
    def __init__(self, pos_x, pos_y, center_x, center_y, val):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.center_x = center_x
        self.center_y = center_y
        self.val = val
        self.next_step()

    def recognition(self, pos_x, pos_y):
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
    
    def next_step(self):
        for j in points:
            self.name = j[2]
            self.pos = j[3]
            self.cors = j[4]
            self.sens = j[5]
            if(j[0] == self.pos_x and j[1] == self.pos_y):
                if(j[2] == "strada" or j[2] == "start"):
                    if(self.pos == "nord"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y - 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y - 60
                        if(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y + 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y + 60
                    if(self.pos == "sud"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y + 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y + 60
                        if(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y - 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y - 60
                    if(self.pos == "est"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y + 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y
                        if(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y - 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y
                    if(self.pos == "ovest"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y - 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y
                        if(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y + 60
                            if(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y
                    break

