import numpy
import math

for i in range (10000):
    age_range = [20, 40, 60, 80]
    Speed_range = [1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
    reaction_time_range = [1.5, 3.0, 4.5]
    fixed_value = 250
    age_range = age_range
    Speed_range = Speed_range 
    fixed_value = fixed_value
    reaction_time_range = reaction_time_range

    age = numpy.random.choice(age_range, p=[0.22, 0.54, 0.10, 0.14])

    Speed = numpy.random.choice(Speed_range, p=[0.05, 0.10, 0.35, 0.35, 0.10, 0.05])

    reaction_time = numpy.random.choice(reaction_time_range, p=[0.8, 0.18, 0.02])

    skill_factor = 0

    if age == 20 or age == 80:
        skill_factor = 0.3
    elif age == 40:
        skill_factor = 0.0
    elif age == 60:
        skill_factor = 0.1

    if skill_factor == 0.6:
        R_dist = ((math.pow(Speed, 2.0) * reaction_time)/(3.2 - skill_factor))


    elif skill_factor == 0.0:
        R_dist = ((math.pow(Speed, 2.0) * reaction_time)/(3.2 + skill_factor))


    elif skill_factor == 0.2:
        R_dist = ((math.pow(Speed, 2.0) * reaction_time)/(3.2 - skill_factor))


    B_dist = ((math.pow(Speed, 2.0) / (fixed_value * 0.8)))


"""
    if B_dist <= 0.01125:
        print ("1.DrySlow", B_dist)
    elif B_dist > 0.01126 and B_dist <= 0.045:
        print ("2.DryFast", B_dist)"""

"""    if R_dist <= 3.45:
        print ("1", R_dist)
    elif R_dist > 3.45 and R_dist <= 5.9625:
        print ("2", R_dist)
    elif R_dist >  5.9625 and R_dist <= 8.475:
        print ("3", R_dist)
    elif R_dist > 8.475 and R_dist <= 10.9875:
        print ("4", R_dist)
    elif R_dist > 10.9875:
        print ("5", R_dist)"""
