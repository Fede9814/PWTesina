import arcade
import math
import os
import numpy
import random
from fov import *


imagelist = [
    "../Sprites/Car/car_1.png",
    "../Sprites/Car/car_2.png",
    "../Sprites/Car/car_3.png",
    "../Sprites/Car/car_4.png",
    "../Sprites/Car/car_5.png",
    "../Sprites/Car/TIR_1.png",
    "../Sprites/Car/TIR_2.png",
    "../Sprites/Car/TIR_3.png",
    "../Sprites/Car/bike_1.png",
    "../Sprites/Car/bike_2.png",
    "../Sprites/Car/bike_3.png"
    ]


class car(arcade.Sprite):
    def __init__(self, scale):
        super().__init__(scale)
        filename = numpy.random.choice(imagelist, p = [0.1, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09])
        self.texture = arcade.load_texture(filename)
        self.telaio = numpy.random.randint(0, 1000000, 1)
        self.frame_up = True
        self.probability_change = 1
        self.my_cube = None
        self.in_transit = False
        self.stop_cube = None
        #max speed = 330, after that it explodes.
        #reasonable range: 150 < v < 300
        self.initial_speed_range = [180, 210, 240, 270, 300, 330]
        self.initial_speed = numpy.random.choice(self.initial_speed_range, p = [0.16, 0.16, 0.17, 0.17, 0.17, 0.17])
        self.speed = self.initial_speed
        self.base_value_x = 0
        self.base_value_y = 0
        self.collision = False
        self.skip_collision = False
        self.ignore = False
        self.frame_count = 0
        self.despawn_count = 100
        
        
        
    def setup(self, cube_list, car_list):
        self.cube_list = cube_list
        self.car_list = car_list
        self.center_x, self.center_y = self.spawn()
        self.angle = 0 
        self.fov = fov(self.center_x, self.center_y, self.angle, self)
        self.fov.setup()

    def set_car_list (self, car_list):
        self.car_list = car_list

    def reduce_speed (self):
        if( self.speed >= 15 and self.ignore == False):
            self.speed += -15

        if( self.speed > 210):
            self.probability_change += 2
    
    def increase_speed (self):
        if( self.speed < self.initial_speed or (self.stop_cube != None and self.in_transit == False) and self.speed < 400):
            self.speed += 15

    def brack_in_time (self, car):
        if(car.speed < self.speed):
            self.speed = self.speed/2
            self.reduce_speed()
        else:
            self.reduce_speed()

    def check_collision(self, car_list):
            in_range = None
            for car in car_list:
                if(car.telaio != self.telaio):
                    if arcade.check_for_collision(self, car):
                        in_range = True
                        if(self.frame_count > self.despawn_count):
                            self.kill()
                            car.kill()
                        break
                    else:
                        in_range = False
            if(in_range == None):
                in_range = False
            return in_range
    
    def update(self, delta_time=0.50): 
        
        start_x = self.center_x
        start_y = self.center_y

        dest_x, dest_y = self.next_move()

        x_diff = (dest_x + self.base_value_x) - start_x
        y_diff = (dest_y + self.base_value_y) - start_y
        angle = math.atan2(y_diff, x_diff)

        self.check_speed = self.fov.check_distance(self.car_list)
        if(self.check_speed != True):
            self.reduce_speed()
        else:
            self.increase_speed()

        self.check_brack, front_car = self.fov.check_bracking(self.car_list)
        if(self.check_brack == True and self.ignore == False):
            self.brack_in_time(front_car)

        #self.check_speed = True

        self.skip_collision = self.fov.check_car_collision(self.car_list)
        if(self.skip_collision == True):
            self.probability_change = 0
            self.temp_destx = self.last_change_x
            self.temp_desty = self.last_change_y

        self.collision = self.check_collision(self.car_list)


            
        if self.collision == False:
            if self.frame_up == True:
                self.angle = math.degrees(angle)
                self.fov.set_angle(self.angle)

                self.change_x = math.cos(angle)* 0.01 * self.speed
                self.change_y = math.sin(angle)* 0.01 * self.speed

                self.center_x = self.center_x + self.change_x
                self.center_y = self.center_y + self.change_y

                self.fov.move()
        else:
            self.frame_count += 1
            

    def spawn(self):
        spawn = random.randint(1,8)

        if(spawn == 1):
            start_spn_x = random.randint(850, 890)
            start_spn_y = 1079
        if(spawn == 2):
            start_spn_x = random.randint(910, 950)
            start_spn_y = 1079
        if(spawn == 3):
            start_spn_x = 1919
            start_spn_y = random.randint(550, 590)
        if(spawn == 4):
            start_spn_x = 1919
            start_spn_y = random.randint(610, 650)
        if(spawn == 5):
            start_spn_x = random.randint(970, 1010)
            start_spn_y = 1
        if(spawn == 6):
            start_spn_x = random.randint(1030, 1070)
            start_spn_y = 1
        if(spawn == 7):
            start_spn_x = 1
            start_spn_y = random.randint(430, 470)
        if(spawn == 8):
            start_spn_x = 1
            start_spn_y = random.randint(490, 530)
        return start_spn_x, start_spn_y

    def next_move(self):

        dest_x = None
        dest_y = None
        temp_x = None
        temp_y = None

        probability_perc = random.randint(1, 100)

        for cube in self.cube_list:
            self.fov.search_my_cube(cube)
            if(cube.pos_x <= self.center_x and cube.pos_x + 60 > self.center_x and cube.pos_y <= self.center_y and cube.pos_y + 60 > self.center_y):
                if(cube != self.my_cube):
                    self.my_cube = cube
                    if(self.in_transit == False):
                        if(cube.name == "exit"):
                            self.kill()
                        if(cube.name == "strada" or cube.name == "start"):
                            if(self.probability_change > probability_perc):
                                if(cube.cors == "left"):
                                    temp_x = cube.next_right_x
                                    temp_y = cube.next_right_y
                                    #self.probability_change += 1
                                else:
                                    temp_x = cube.next_left_x
                                    temp_y = cube.next_left_y
                                    self.probability_change = 0
                            else:
                                if(cube.cors == "right"):
                                    temp_x = cube.next_right_x
                                    temp_y = cube.next_right_y

                                    self.last_change_x = cube.next_left_x
                                    self.last_change_y = cube.next_left_y
                                else:
                                    temp_x = cube.next_left_x
                                    temp_y = cube.next_left_y

                                    self.last_change_x = cube.next_right_x
                                    self.last_change_y = cube.next_right_y
                        elif(cube.name == "semaforo"):
                            temp_x, temp_y = self.rotation(cube)
                            self.stop_cube = cube
                            if(self.stop_cube.cors == "right"):
                                if(self.direction_perc != 1):
                                    if(self.stop_cube.pos == "nord"):
                                        self.base_value_x = 60
                                        self.base_value_y = 0
                                    elif(self.stop_cube.pos == "sud"):
                                        self.base_value_x = -60
                                        self.base_value_y = 0
                                    elif(self.stop_cube.pos == "est"):
                                        self.base_value_x = 0
                                        self.base_value_y = -60
                                    elif(self.stop_cube.pos == "ovest"):
                                        self.base_value_x = 0
                                        self.base_value_y = 60
                            else:
                                if(self.stop_cube.pos == "nord"):
                                    self.base_value_x = -180
                                    self.base_value_y = 0
                                elif(self.stop_cube.pos == "sud"):
                                    self.base_value_x = 180
                                    self.base_value_y = 0
                                elif(self.stop_cube.pos == "est"):
                                    self.base_value_x = 0
                                    self.base_value_y = 180
                                elif(self.stop_cube.pos == "ovest"):
                                    self.base_value_x = 0
                                    self.base_value_y = -180
                            self.in_transit = True
                            
                            if(cube.stop_status == True):
                                self.frame_up = True
                            else:
                                self.frame_up = False
                                if(self.fov.my_cube != "semaforo"):
                                   self.frame_up = True 
                                else:
                                    self.frame_up = False
                        else:
                            temp_x = self.temp_destx
                            temp_y = self.temp_desty
                        break
                    else:
                        if(cube.pos_x != self.temp_destx or cube.pos_y != self.temp_desty):
                            if(self.stop_cube.cors == "right"):
                                if(self.direction_perc != 1):
                                    if(self.stop_cube.pos == "nord"):
                                        if(self.base_value_x > 0):
                                            self.base_value_x = self.base_value_x - 1
                                    elif(self.stop_cube.pos == "sud"):
                                        if(self.base_value_x < 0):
                                            self.base_value_x = self.base_value_x + 1
                                    elif(self.stop_cube.pos == "est"):
                                        if(self.base_value_y < 0):
                                            self.base_value_y = self.base_value_y + 1
                                    elif(self.stop_cube.pos == "ovest"):
                                        if(self.base_value_y > 0):
                                            self.base_value_y = self.base_value_y - 1
                            else:
                                if(self.stop_cube.pos == "nord"):
                                    if(self.speed > 270): 
                                        if(self.base_value_x < -115):
                                            self.base_value_x = self.base_value_x + 1
                                        else:
                                            self.base_value_x = 0
                                    else:
                                        if(self.base_value_x < -95):
                                            self.base_value_x = self.base_value_x + 1
                                        else:
                                            self.base_value_x = 0
                                elif(self.stop_cube.pos == "sud"):
                                    if(self.speed > 270): 
                                        if(self.base_value_x > 115):
                                            self.base_value_x = self.base_value_x - 1
                                        else:
                                            self.base_value_x = 0
                                    else:
                                        if(self.base_value_x > 95):
                                            self.base_value_x = self.base_value_x - 1
                                        else:
                                            self.base_value_x = 0
                                elif(self.stop_cube.pos == "est"):
                                    if(self.speed > 270):
                                        if(self.base_value_y > 115):
                                            self.base_value_y = self.base_value_y - 1
                                        else:
                                            self.base_value_y = 0
                                    else:
                                        if(self.base_value_y > 95):
                                            self.base_value_y = self.base_value_y - 1
                                        else:
                                            self.base_value_y = 0
                                elif(self.stop_cube.pos == "ovest"):
                                    if(self.speed > 270):
                                        if(self.base_value_y < -115):
                                            self.base_value_y = self.base_value_y + 1
                                        else:
                                            self.base_value_y = 0
                                    else:
                                        if(self.base_value_y < -95):
                                            self.base_value_y = self.base_value_y + 1
                                        else:
                                            self.base_value_y = 0
                            temp_x = self.temp_destx
                            temp_y = self.temp_desty
                        else:
                            self.in_transit = False
                            self.base_value_x = 0
                            self.base_value_y = 0
                            if(cube.cors == "left"):
                                temp_x = cube.next_left_x
                                temp_y = cube.next_left_y
                            else:
                                temp_x = cube.next_right_x
                                temp_y = cube.next_right_y

                else:
                    if(self.in_transit == False):
                        if(cube.name == "strada" or cube.name == "start"):
                            temp_x = self.temp_destx
                            temp_y = self.temp_desty
                        else:
                            temp_x = self.temp_destx
                            temp_y = self.temp_desty
                        break
                    else:
                        if(cube.val == 4):
                            if(cube.stop_status == True):
                                self.frame_up = True
                            else:
                                self.frame_up = False
                                if(self.fov.my_cube != 4):
                                       self.frame_up = True 
                                else:
                                    self.frame_up = False

                        if(self.frame_up == True and self.check_speed == True):
                            if(self.stop_cube.cors == "right"):
                                    if(self.direction_perc != 1):
                                        if(self.stop_cube.pos == "nord"):
                                            if(self.base_value_x > 0):
                                                self.base_value_x = self.base_value_x - 1
                                        elif(self.stop_cube.pos == "sud"):
                                            if(self.base_value_x < 0):
                                                self.base_value_x = self.base_value_x + 1
                                        elif(self.stop_cube.pos == "est"):
                                            if(self.base_value_y < 0):
                                                self.base_value_y = self.base_value_y + 1
                                        elif(self.stop_cube.pos == "ovest"):
                                            if(self.base_value_y > 0):
                                                self.base_value_y = self.base_value_y - 1
                            else:
                                if(self.stop_cube.pos == "nord"):
                                    if(self.speed > 270): 
                                        if(self.base_value_x < -115):
                                            self.base_value_x = self.base_value_x + 1
                                        else:
                                            self.base_value_x = 0
                                    else:
                                        if(self.base_value_x < -95):
                                            self.base_value_x = self.base_value_x + 1
                                        else:
                                            self.base_value_x = 0
                                elif(self.stop_cube.pos == "sud"):
                                    if(self.speed > 270): 
                                        if(self.base_value_x > 115):
                                            self.base_value_x = self.base_value_x - 1
                                        else:
                                            self.base_value_x = 0
                                    else:
                                        if(self.base_value_x > 95):
                                            self.base_value_x = self.base_value_x - 1
                                        else:
                                            self.base_value_x = 0
                                elif(self.stop_cube.pos == "est"):
                                    if(self.speed > 270):
                                        if(self.base_value_y > 115):
                                            self.base_value_y = self.base_value_y - 1
                                        else:
                                            self.base_value_y = 0
                                    else:
                                        if(self.base_value_y > 95):
                                            self.base_value_y = self.base_value_y - 1
                                        else:
                                            self.base_value_y = 0
                                elif(self.stop_cube.pos == "ovest"):
                                    if(self.speed > 270):
                                        if(self.base_value_y < -115):
                                            self.base_value_y = self.base_value_y + 1
                                        else:
                                            self.base_value_y = 0
                                    else:
                                        if(self.base_value_y < -95):
                                            self.base_value_y = self.base_value_y + 1
                                        else:
                                            self.base_value_y = 0
                        temp_x = self.temp_destx
                        temp_y = self.temp_desty

        for cube in self.cube_list:
            if(cube.pos_x == temp_x and cube.pos_y == temp_y):
                dest_x = cube.center_x
                dest_y = cube.center_y
                self.temp_destx = temp_x
                self.temp_desty = temp_y
                break

        return dest_x, dest_y
    
    def rotation(self, cube):
        if(cube.cors == "right"):
            self.direction_perc = random.randint(1,2)
            #Dritto
            if(self.direction_perc == 1):
                if(cube.pos == "nord"):
                    temp_x = 840
                    temp_y = 360
                elif(cube.pos == "sud"):
                    temp_x = 1020
                    temp_y = 660
                elif(cube.pos == "est"):
                    temp_x = 780
                    temp_y = 600
                elif(cube.pos == "ovest"):
                    temp_x = 1080
                    temp_y = 420
            #Destra
            else:
                if(cube.pos == "nord"):
                    temp_x = 780
                    temp_y = 600
                elif(cube.pos == "sud"):
                    temp_x = 1080
                    temp_y = 420
                elif(cube.pos == "est"):
                    temp_x = 1020
                    temp_y = 660
                elif(cube.pos == "ovest"):
                    temp_x = 840
                    temp_y = 360
        #Sinistra
        else:
            if(cube.pos == "nord"):
                temp_x = 1080
                temp_y = 480
            elif(cube.pos == "sud"):
                temp_x = 780
                temp_y = 540
            elif(cube.pos == "est"):
                temp_x = 900
                temp_y = 360
            elif(cube.pos == "ovest"):
                temp_x = 960
                temp_y = 660

        return temp_x, temp_y


