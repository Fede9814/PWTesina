import random
import string
import names
import numpy
import json


def JSON_information():

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
        pilot_surname = names.get_last_name(gender='female')
    elif gender_picker == 1:
        pilot_sex = "M"
        pilot_name =  names.get_full_name(gender='male')
        pilot_surname = names.get_last_name(gender='female')

    Json =  {
            "Gender": pilot_sex,
            "Age": age,
            "Name": pilot_name,
            "Surname": pilot_surname,
            "Plate": plate,
            "Region": region
            }    