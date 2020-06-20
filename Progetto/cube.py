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
        self.stop_status = False

    def recognition(self, pos_x, pos_y):
        cube = None
        if(self.val == 0):
            cube = arcade.load_texture("../Concept Art/Blocks/bound.png")
            cube.draw_scaled(self.center_x, self.center_y)
        elif(self.val == 1):
            cube = arcade.load_texture("../Concept Art/Blocks/start.png")
            cube.draw_scaled(self.center_x, self.center_y)
        elif(self.val == 2):
            cube = arcade.load_texture("../Concept Art/Blocks/end.png")
            cube.draw_scaled(self.center_x, self.center_y)
        elif(self.val == 3):
            #NORD#
            if(self.pos == "nord"):
                if(self.sens == "in"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road1_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road2_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
                if(self.sens == "out"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road3_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road4_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
            #SUD#
            if(self.pos == "sud"):
                if(self.sens == "in"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road3_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road4_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
                if(self.sens == "out"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road1_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road2_new.png")
                        cube.draw_scaled(self.center_x, self.center_y, angle=90)
            #OVEST#
            if(self.pos == "ovest"):
                if(self.sens == "in"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road2_new.png", mirrored=True)
                        cube.draw_scaled(self.center_x, self.center_y)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road1_new.png", mirrored=True)
                        cube.draw_scaled(self.center_x, self.center_y)
                if(self.sens == "out"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road4_new.png", mirrored=True)
                        cube.draw_scaled(self.center_x, self.center_y)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road3_new.png", mirrored=True)
                        cube.draw_scaled(self.center_x, self.center_y)
            #EST#
            if(self.pos == "est"):
                if(self.sens == "in"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road1_new.png")
                        cube.draw_scaled(self.center_x, self.center_y)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road2_new.png")
                        cube.draw_scaled(self.center_x, self.center_y)
                if(self.sens == "out"):
                    if(self.cors == "left"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road3_new.png")
                        cube.draw_scaled(self.center_x, self.center_y)
                    if(self.cors == "right"):
                        cube = arcade.load_texture("../Concept Art/Blocks/road4_new.png")
                        cube.draw_scaled(self.center_x, self.center_y)

        elif(self.val == 4):
            cube = arcade.load_texture("../Concept Art/Blocks/stop.png")
            cube.draw_scaled(self.center_x, self.center_y)
        elif(self.val == 5):
            cube = arcade.load_texture("../Concept Art/Blocks/road_new.png")
            cube.draw_scaled(self.center_x, self.center_y)
        self.cube = cube
    
    def next_step(self):
        for j in points:
            if(j[0] == self.pos_x and j[1] == self.pos_y):
                self.name = j[2]
                self.pos = j[3]
                self.cors = j[4]
                self.sens = j[5]
                if(j[2] == "strada" or j[2] == "start"):
                    if(self.pos == "nord"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y - 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y - 60
                        elif(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y + 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y + 60
                    elif(self.pos == "sud"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y + 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y + 60
                        elif(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y - 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x
                                self.next_right_y = self.pos_y - 60
                    elif(self.pos == "est"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y + 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y
                        elif(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y - 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y
                    elif(self.pos == "ovest"):
                        if(self.sens == "in"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y - 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x + 60
                                self.next_left_y = self.pos_y + 60
                                self.next_right_x = self.pos_x + 60
                                self.next_right_y = self.pos_y
                        elif(self.sens == "out"):
                            if(self.cors == "left"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y 
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y + 60
                            elif(self.cors == "right"):
                                self.next_left_x = self.pos_x - 60
                                self.next_left_y = self.pos_y - 60
                                self.next_right_x = self.pos_x - 60
                                self.next_right_y = self.pos_y
                    break
                if(j[2] == "semaforo"):
                    self.stop_ord = j[6]
                    break
    
    def change_status(self, current_status):
        token = current_status
        if(current_status == self.stop_ord):
            self.stop_status = True
        else:
            self.stop_status = False


            
