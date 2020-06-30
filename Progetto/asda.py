import random
import string
import names
import numpy
import json
import math

"""""""""plate_chars = []

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

plate = ''.join(plate_chars)""""""


age_range = [20, 40, 60, 80]
Speed_range = [1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
μ_global_range = [0.1, 0.8]
reaction_time_range = [1.5, 3.0, 4.5]
fixed_value = 250
age_range = age_range
Speed_range = Speed_range 
fixed_value = fixed_value
μ_global_range = μ_global_range 
reaction_time_range = reaction_time_range
#fov parameters pickers
age = numpy.random.choice(
    #questo è ok
    age_range, p=[0.22, 0.54, 0.10, 0.14])
    #questo è ok
Speed = numpy.random.choice(
    Speed_range, p=[0.05, 0.10, 0.35, 0.35, 0.10, 0.05])
    #questo è ok
reaction_time = numpy.random.choice(
    reaction_time_range, p=[0.8, 0.18, 0.02])
    #questo è ok
μ_value = numpy.random.choice(
    μ_global_range, p=[0.01, 0.99])
    #questo è ok
skill_factor = 0
#fov calculations
if age == 20 or age == 80:
    skill_factor = 0.6
elif age == 40:
    skill_factor = 0.0
elif age == 60:
    skill_factor = 0.2
#print("Skill", skill_factor)
if skill_factor == 0.6:
    R_dist = ((math.pow(Speed, 2.0) *
                    reaction_time)/(3.6 - skill_factor))
#print("R_dist", R_dist)
elif skill_factor == 0.0:
    R_dist = ((math.pow(Speed, 2.0) *
                    reaction_time)/(3.6 + skill_factor))
#print("R_dist", R_dist)
elif skill_factor == 0.2:
    R_dist = ((math.pow(Speed, 2.0) *
                    reaction_time)/(3.6 - skill_factor))
#print("R_dist", R_dist)
B_dist = ((math.pow(Speed, 2.0) /
                (fixed_value * μ_value)))
# print("B_dist",B_dist)
#Plate info
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
region = random.choice(region_list)
#Pilot full name generator
gender = [0, 1]
gender_picker = numpy.random.choice(gender, p = [0.54, 0.46])
if gender_picker == 0:
    pilot_sex = "F"
    pilot_name = names.get_first_name(gender='female')
    pilot_surname = names.get_last_name()
elif gender_picker == 1:
    pilot_sex = "M"
    pilot_name =  names.get_full_name(gender='male')
    pilot_surname = names.get_last_name()

Json =  {
        "Gender": pilot_sex,
        "Age": age + random.randint(0, 9),
        "Name": pilot_name,
        "Surname": pilot_surname,
        "Plate": plate,
        "Region": region
        }  

print(Json)"""


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
car_model = numpy.random.choice(car_model_list, p = 
    [0.03, 0.03, 0.05, 0.06, 0.08, 0.12, 0.12, 0.15, 0.15, 0.21])
print(car_model)

displacement_list = ["1200", "1300", "1400", "1600", "2000"]
displacement = random.choice(displacement_list)
print(displacement)
Tax_status_list = ["Paid", "Unpaid"]
Tax_status = numpy.random.choice(Tax_status_list, p = [0.95, 0.05])
print(Tax_status)
Insurance_status_list = ["Paid", "Unpaid"]
Insurance_status = numpy.random.choice(Insurance_status_list, p = [0.95, 0.05])
print(Insurance_status)