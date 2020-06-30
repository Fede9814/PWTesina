import arcade
import math
import os
import numpy
import random
import string
import names
import numpy
import json

#LARGHEZZA < 55
#LUNGHEZZA < L CAR

class fov(arcade.PhysicsEngineSimple):
    def __init__(self, center_x, center_y, angle, car):

        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
        self.car = car

        age_range = [20, 40, 60, 80]
        Speed_range = [1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
        μ_global_range = [0.1, 0.8]
        reaction_time_range = [1.5, 3.0, 4.5]

        fixed_value = 250

        self.age_range = age_range
        self.Speed_range = Speed_range 
        self.fixed_value = fixed_value
        self.μ_global_range = μ_global_range 
        self.reaction_time_range = reaction_time_range

        #fov parameters pickers
        self.age = numpy.random.choice(
            #questo è ok
            self.age_range, p=[0.22, 0.54, 0.10, 0.14])
            #questo è ok
        self.Speed = numpy.random.choice(
            self.Speed_range, p=[0.05, 0.10, 0.35, 0.35, 0.10, 0.05])
            #questo è ok
        self.reaction_time = numpy.random.choice(
            self.reaction_time_range, p=[0.8, 0.18, 0.02])
            #questo è ok
        self.μ_value = numpy.random.choice(
            self.μ_global_range, p=[0.01, 0.99])
            #questo è ok
        self.skill_factor = 0

        #fov calculations
        if self.age == 20 or self.age == 80:
            self.skill_factor = 0.6
        elif self.age == 40:
            self.skill_factor = 0.0
        elif self.age == 60:
            self.skill_factor = 0.2
        #print("Skill", self.skill_factor)

        if self.skill_factor == 0.6:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 - self.skill_factor))
        #print("R_dist", self.R_dist)
        elif self.skill_factor == 0.0:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 + self.skill_factor))
        #print("R_dist", self.R_dist)
        elif self.skill_factor == 0.2:
            self.R_dist = ((math.pow(self.Speed, 2.0) *
                            self.reaction_time)/(3.6 - self.skill_factor))
        #print("R_dist", self.R_dist)

        self.B_dist = ((math.pow(self.Speed, 2.0) /
                        (self.fixed_value * self.μ_value)))
        # print("B_dist",self.B_dist)

        #Age correction
        self.true_age = self.age + random.randint(0, 9)

        #VehicleID
        self.VehicleID = random.randint(100000, 999999)

        #Car model, displacement, tax and insurance status
        car_model_list = ["Peugeot-Citroen",
                          "Suzuki",
                          "FCA",
                          "Honda" ,
                          "Ford",
                          "Hyundai-Kia",
                          "General Motors",
                          "Renault-Nissan",
                          "Toyota",
                          "VW Group"]
        self.car_model = numpy.random.choice(car_model_list, p = 
            [0.03, 0.03, 0.05, 0.06, 0.08, 0.12, 0.12, 0.15, 0.15, 0.21])
        
        Displacement_list = ["1200", "1300", "1400", "1600", "2000"]
        self.Displacement = random.choice(Displacement_list)

        Tax_status_list = ["Paid", "Unpaid"]
        self.Tax_status = numpy.random.choice(Tax_status_list, p = [0.95, 0.05])

        Insurance_status_list = ["Paid", "Unpaid"]
        self.Insurance_status = numpy.random.choice(Insurance_status_list, p = [0.95, 0.05])


        #Plate info
        self.plate_chars = []
        self.Chars = string.ascii_uppercase
        self.middle_numbers = str(random.randint(100, 999))
        self.CharI = random.choice(self.Chars)
        self.plate_chars.append(self.CharI)
        self.CharII = random.choice(self.Chars)
        self.plate_chars.append(self.CharII)
        self.plate_chars.append(self.middle_numbers)
        self.CharIII = random.choice(self.Chars)
        self.plate_chars.append(self.CharIII)
        self.CharIV = random.choice(self.Chars)
        self.plate_chars.append(self.CharIV)

        self.plate = ''.join(self.plate_chars)

        #Region initials
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

        self.region = random.choice(region_list)

        #Pilot full name generator
        gender = [0, 1]
        self.gender_picker = numpy.random.choice(gender, p = [0.54, 0.46])
        if self.gender_picker == 0:
            self.pilot_sex = "F"
            self.pilot_name = names.get_first_name(gender='female')
            self.pilot_surname = names.get_last_name()
        elif self.gender_picker == 1:
            self.pilot_sex = "M"
            self.pilot_name =  names.get_full_name(gender='male')
            self.pilot_surname = names.get_last_name()

        self.Json =  {
                "IDVehicle" : self.VehicleID,
                "Gender": self.pilot_sex,
                "Age": self.true_age,
                "Name": self.pilot_name,
                "Surname": self.pilot_surname,
                "Plate": self.plate,
                "Region": self.region,
                "Model" : self.car_model,
                "Displacement" : self.Displacement,
                "CarTax" : self.Tax_status,
                "Insurance" : self.Insurance_status,
                }

    def setup(self):

        fov_list = []

        hitbox1 = "../Sprites/Hitbox/Hitbox_L70_W30.png"
        hitbox2 = "../Sprites/Hitbox/Hitbox_L80_W30.png"
        hitbox3 = "../Sprites/Hitbox/Hitbox_L100_W30.png"
        hitbox4 = "../Sprites/Hitbox/Hitbox_L120_W30.png"
        hitbox5 = "../Sprites/Hitbox/Hitbox_L140_W30.png"

        fov_list.append(hitbox1)
        fov_list.append(hitbox2)
        fov_list.append(hitbox3)
        fov_list.append(hitbox4)
        fov_list.append(hitbox5)

        hitbox_fov = numpy.random.choice(fov_list, p = [0.7795, 0.1679, 0.0479, 0.0032, 0.0015])

        #setta alpha a 0 per nascondere i fov delle macchine
        #self.hitbox.alpha = 255
        self.sprite = arcade.Sprite(hitbox_fov, 1)
        #setta alpha a 0 per nascondere i fov delle macchine
        self.sprite.alpha = 0
        pcx, pcy = self.center_calc(self.car)
        self.sprite.center_x = pcx
        self.sprite.center_y = pcy

        self.stop_sprite = arcade.Sprite("../Sprites/Hitbox/Fixed_Hitbox_L20_W30.png", 1)
        self.stop_sprite.alpha = 0
        pcx, pcy = self.center_calc(self.car)
        self.stop_sprite.center_x = pcx
        self.stop_sprite.center_y = pcy

    def center_calc(self, car):
        punto_a = car.points[1]
        punto_b = car.points[3]

        punto_a_x = punto_a[0]
        punto_a_y = punto_a[1]
        punto_b_x = punto_b[0]
        punto_b_y = punto_b[1]

        punto_c_x = (punto_a_x + punto_b_x)/2
        punto_c_y = (punto_a_y + punto_b_y)/2

        return punto_c_x, punto_c_y


    def move(self):
        pcx, pcy = self.center_calc(self.car)
        self.sprite.center_x = pcx
        self.sprite.center_y = pcy

        self.stop_sprite.center_x = pcx
        self.stop_sprite.center_y = pcy

    def search_my_cube(self, cube):
        if(cube.pos_x <= self.sprite.center_x and cube.pos_x + 60 > self.sprite.center_x and cube.pos_y <= self.sprite.center_y and cube.pos_y + 60 > self.sprite.center_y):
            self.my_cube = cube.val

    def set_angle(self, value):
        self.sprite.angle = value
        self.stop_sprite.angle = value

    def check_distance(self, car_list):
        in_range = None
        for car in car_list:
            if(car.telaio != self.car.telaio):
                if arcade.check_for_collision(self.sprite, car):
                    in_range = False
                    break
                else:
                    in_range = True
        if(in_range == None):
            in_range = True
        return in_range

    def check_braking(self, car_list):
            braking = None
            collided_car = None
            collision_car = arcade.check_for_collision_with_list(self.stop_sprite, car_list)

            for car in collision_car:
                if(car.telaio != self.car.telaio):
                    collided_car = car
                    braking = True
                    break
                else:
                    braking = False
                    collided_car = self
            return braking, collided_car 

    def check_car_collision (self, car_list):
        skip_collision = None
        for car in car_list:
            if(car.telaio != self.car.telaio):
                if arcade.check_for_collision(self.sprite, car):
                    if(car.collision == True):
                        skip_collision = True
                        break
                    else:
                        skip_collision = False
            
        if (skip_collision == None):
            skip_collision = False

        return skip_collision
    
        