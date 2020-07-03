import arcade
import math
import os
import numpy
import random
import Screen
from fov import *
import datetime
pyodbc.pooling = False

incidenti = 0

server = 'databasetesina.c8xvln9jnfss.eu-west-1.rds.amazonaws.com' 
database = 'db_tesina' 
username = 'admin' 
password = 'password' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

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
    ]

class car(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.filename = numpy.random.choice(imagelist, p = [0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10])
        self.texture = arcade.load_texture(self.filename)
        self.telaio = numpy.random.randint(0, 1000000, 1)
        self.frame_up = True
        self.probability_change = 1
        self.my_cube = None
        self.in_transit = False
        self.stop_cube = None
        self.initial_speed_range = [180, 210, 240, 270, 300]
        self.initial_speed = numpy.random.choice(self.initial_speed_range, p = [0.2, 0.2, 0.2, 0.2, 0.2])
        self.speed = self.initial_speed
        self.base_value_x = 0
        self.base_value_y = 0
        self.collision = False
        self.skip_collision = False
        self.ignore = False
        self.frame_count = 0
        self.despawn_count = 100
        self.car_music_list = []
        self.tir_music_list = []
        self.bike_music_list = []
        self.current_car_song = 0
        self.current_tir_song = 0
        self.current_bike_song = 0
        self.CAR_MUSIC_VOLUME = 0.1
        self.TIR_MUSIC_VOLUME = 0.1
        self.BIKE_MUSIC_VOLUME = 0.1

    def get_incidenti(self):
        return incidenti
        
        
    def setup(self, cube_list, car_list):
        self.cube_list = cube_list
        self.car_list = car_list
        self.center_x, self.center_y = self.spawn()
        self.angle = 0 
        self.fov = fov(self.center_x, self.center_y, self.angle, self)
        self.fov.setup()
        self.car_music_list = ["../Sound/1_crash.wav"]
        self.tir_music_list = ["../Sound/1_crash.wav"]
        self.bike_music_list = ["../Sound/1_crash.wav"]
        self.db_info()
        self.queryThis()
          
        
        self.timer_start = datetime.datetime.now().replace(microsecond=0)

    def time_service (self, hour, minute, second):
        self.start_time = str(hour) + ":" + str(minute) + ":" + str(second)
        self.hour = hour
        self.end_time = None
        self.timer_second = 0
        self.timer_second_sup = 0
        self.timer_minute = 0
        self.timer_string_min = "00"
        self.timer_string_sec = "00"

    def db_info(self):
        self.car_information = []

        #VehicleID
        ID_Chars = []
        IDChars = string.ascii_uppercase
        IDChars2 = string.ascii_uppercase
        IDChars3 = string.ascii_uppercase
        
        ID_Numbers = str(random.randint(1, 99999))
        ID_Numbers2 = str(random.randint(1, 99999))

        IDChar = random.choice(IDChars)
        IDChar2 = random.choice(IDChars2)
        IDChar3 = random.choice(IDChars3)
        
        ID_Chars.append(IDChar)
        ID_Chars.append(ID_Numbers)
        ID_Chars.append(IDChar2)
        ID_Chars.append(ID_Numbers2)
        ID_Chars.append(IDChar3)
        IDVehicle = str(''.join(ID_Chars))
        self.car_information.append(IDVehicle)

        #PLATE
        plate_chars = []
        Chars = string.ascii_uppercase
        middle_numbers = str(random.randint(100, 999))
        CharI = random.choice(Chars)
        plate_chars.append(CharI)
        CharII = random.choice(Chars)
        plate_chars.append(CharII)
        plate_chars.append(middle_numbers)
        CharIII = random.choice(Chars)
        plate_chars.append(CharIII)
        CharIV = random.choice(Chars)
        plate_chars.append(CharIV)

        plate = ''.join(plate_chars)
        self.car_information.append(plate)

        #AGE
        true_age = int(self.fov.age + random.randint(0, 9))

        #GENDER - NAME - SURNAME
        gender = [0, 1]
        gender_picker = numpy.random.choice(gender, p = [0.54, 0.46])
        if gender_picker == 0:
            pilot_sex = "F"
            pilot_name = names.get_first_name(gender='female')
            pilot_surname = names.get_last_name()
        else:
            pilot_sex = "M"
            pilot_name =  names.get_full_name(gender='male')
            pilot_surname = names.get_last_name()

        self.car_information.append(pilot_sex)
        self.car_information.append(true_age)
        self.car_information.append(pilot_name)
        self.car_information.append(pilot_surname)

        #REGION
        region_list = [
            "AL","AN","AO","AQ","AR","AP",
            "AT","AV","BA","BT","BL","BN",
            "BG","BI","BO","BZ","BS","BR",
            "CA","CL","CB","CI","CE","CT",
            "CZ","CH","CO","CS","CR","KR",
            "CN","EN","FM","FE","FI","FG",
            "FC","FR","GE","GO","GR","IM",
            "IS","SP","LT","LE","LC","LI",
            "LO","LU","MC","MN","MS","MT",
            "VS","ME","MI","MO","MB","NA",
            "NO","NU","OG","OT","OR","PD",
            "PA","PR","PV","PG","PU","PE",
            "PC","PI","PT","PN","PZ","PO",
            "RG","RA","RC","RE","RI","RN",
            "RO","SA","SS","SV","SI","SR",
            "SO","TA","TE","TR","TO","TP",
            "TN","TV","TS","UD","VA","VE",
            "VB","VC","VR","VV","VI","VT"
            ]

        region = random.choice(region_list)
        self.car_information.append(region)

        #CAR MODEL
        car_model_list = ["Peugeot-Citroen",
            "Suzuki",
            "FCA",
            "Honda",
            "Ford",
            "Hyundai-Kia",
            "General Motors",
            "Renault-Nissan",
            "Toyota",
            "VW Group"]
        car_model = numpy.random.choice(car_model_list, p = 
            [0.03, 0.03, 0.05, 0.06, 0.08, 0.12, 0.12, 0.15, 0.15, 0.21])
        self.car_information.append(car_model)

        #DISPLACEMENT
        displacement_list = ["1200", "1300", "1400", "1600", "2000"]
        displacement = random.choice(displacement_list)
        self.car_information.append(displacement)

        #TAX
        tax_status_list = ["Paid", "Unpaid"]
        tax_status = numpy.random.choice(tax_status_list, p = [0.95, 0.05])
        self.car_information.append(tax_status)

        #INSURANCE
        insurance_status_list = ["Paid", "Unpaid"]
        insurance_status = numpy.random.choice(insurance_status_list, p = [0.95, 0.05])
        self.car_information.append(insurance_status)


    def queryThis(self):
        self.cursor = cursor
        self.cursor.execute("INSERT INTO dbo.Car_Information (IDVehicle, Plate, Gender, Age, Name, Surname, Region, Model, Displacement, CarTax, Insurance) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.car_information[0], self.car_information[1], self.car_information[2], self.car_information[3], self.car_information[4], self.car_information[5], self.car_information[6], self.car_information[7], self.car_information[8], self.car_information[9], self.car_information[10]))
        cursor.commit()
        cursor.cancel()
        
    def queryEnd(self, pos, cors):
        self.cursor = cursor
        self.cursor.execute("INSERT INTO dbo.Car_Result (Vehicle, StartTime, EndTime, Collision, StartDirection, EndDirection, StartLane, EndLane) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (self.car_information[0], self.start_time, self.end_time, str(self.collision), self.cube_start_pos, pos, self.cube_start_cors, cors))
        cursor.commit()
        cursor.cancel()
    

    def play_car_song(self):
        self.car_music = arcade.Sound(self.car_music_list[self.current_car_song], streaming=True)
        self.car_music.play(self.CAR_MUSIC_VOLUME)
    
    def play_tir_song(self):
        self.tir_music = arcade.Sound(self.tir_music_list[self.current_tir_song], streaming=True)
        self.tir_music.play(self.TIR_MUSIC_VOLUME)
     
    def play_bike_song(self):
        self.bike_music = arcade.Sound(self.bike_music_list[self.current_bike_song], streaming=True)
        self.bike_music.play(self.BIKE_MUSIC_VOLUME)

    def set_car_list (self, car_list):
        self.car_list = car_list

    def reduce_speed (self, reduce):
        if(self.speed >= reduce and self.ignore == False):
            self.speed -= reduce

        if(self.speed > 210):
            self.probability_change += 2
    
    def increase_speed (self):
        if(self.speed < self.initial_speed or (self.stop_cube != None and self.in_transit == False) and self.speed < 400):
            self.speed += 15

    def brake_in_time (self, car):
        if(car.speed < self.speed):
            self.reduce_speed(30)
        else:
            self.reduce_speed(15)

    def check_collision(self, car_list):
            in_range = None
            for car in car_list:
                if(car.telaio != self.telaio):
                    if arcade.check_for_collision(self, car):
                        in_range = True
                        self.end_time = "00" + ":" + str(self.timer_minute) + ":" + str(self.timer_second)
                        if(self.frame_count > self.despawn_count):
                            if self.filename == "../Sprites/Car/car_1.png" or self.filename == "../Sprites/Car/car_2.png" or self.filename == "../Sprites/Car/car_3.png" or self.filename == "../Sprites/Car/car_4.png" or self.filename == "../Sprites/Car/car_5.png":
                                car.play_car_song()
                            elif self.filename == "../Sprites/Car/TIR_1.png" or self.filename == "../Sprites/Car/TIR_2.png" or self.filename == "../Sprites/Car/TIR_3.png":
                                car.play_tir_song()
                            elif self.filename == "../Sprites/Car/bike_1.png" or self.filename == "../Sprites/Car/bike_2.png" or self.filename == "../Sprites/Car/bike_3.png":
                                car.play_bike_song()
                            self.queryEnd("", "")
                            car.queryEnd("", "")                          
                            
                            self.kill()
                            car.kill()

                            global incidenti 
                            incidenti += 1
                        break
                    else:
                        in_range = False
            if(in_range == None):
                in_range = False
            return in_range
    
    def update(self, delta_time=0.50):

        self.timer_now = datetime.datetime.now().replace(microsecond=0)
        self.timer_result =  self.timer_now - self.timer_start

        if(self.timer_result.seconds != self.timer_second_sup):
            self.timer_second_sup = self.timer_second_sup + 1
            self.timer_second = self.timer_second + 1
            if(self.timer_second <= 9):
                self.timer_string_sec = "0" + str(self.timer_second)
            else:
                self.timer_string_sec = str(self.timer_second)
        if(self.timer_second == 59):
            self.timer_second = 0
            self.timer_minute = self.timer_minute + 1
            if(self.timer_minute <= 9):
                self.timer_string_min = "0" + str(self.timer_minute)
            else:
                self.timer_string_min = str(self.timer_minute)
        
        start_x = self.center_x
        start_y = self.center_y

        dest_x, dest_y = self.next_move()

        x_diff = (dest_x + self.base_value_x) - start_x
        y_diff = (dest_y + self.base_value_y) - start_y
        angle = math.atan2(y_diff, x_diff)

        self.check_speed = self.fov.check_distance(self.car_list)
        if(self.check_speed != True):
            self.reduce_speed(15)
        else:
            self.increase_speed()

        self.check_brake, front_car = self.fov.check_braking(self.car_list)
        if(self.check_brake == True and self.ignore == False):
            self.brake_in_time(front_car)

        #self.check_speed = True

        self.skip_collision = self.fov.check_car_collision(self.car_list)
        if(self.skip_collision == True and self.stop_cube == None):
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
                        if(cube.name == "start"):
                            self.cube_start_pos = cube.pos
                            self.cube_start_cors = cube.cors
                        if(cube.name == "exit"):
                            self.end_time = "00" + ":" + str(self.timer_minute) + ":" + str(self.timer_second)
                            self.queryEnd(cube.pos, cube.cors)
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
