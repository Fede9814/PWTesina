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

    def next_step(self):
        for j in points:
            if(j[0] == self.pos_x and j[1] == self.pos_y):
                self.name = j[2]
                self.pos = j[3]
                self.cors = j[4]
                self.sens = j[5]
                if(j[2] == "semaforo" and j[4] == "Null"):
                    self.light = True
                elif(j[2] == "semaforo" and j[4] != "Null"):
                    self.light = False
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
                if(j[2] == "semaforo"):
                    self.stop_ord = j[6]
                    break
    
    def change_status(self, current_status):
        token = current_status
        if(current_status == self.stop_ord):
            self.stop_status = True
        else:
            self.stop_status = False



