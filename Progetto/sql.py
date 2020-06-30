import pyodbc
from fov import *

    def connectionString(self):
        
    def queryThis(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO Car_Information (CarBirthTime, CarDeathTime, CarLifeSpan, IDVehicle, Gender, Age,  Name, Surname, Plate, Region, Model, Displacement, CarTax, Insurance) VALUES (fov.self.Birth, fov.self.Death, fov.self.Life , fov.self.VehicleID, fov.self.pilot_sex, fov.self.true_age, fov.self.pilot_name, fov.self.pilot_surname, fov.self.plate, fov.self.region, fov.self.car_model, fov.self.Displacement, fov.self.Tax_status, fov.self.Insurance_status)")

        self.cursor.commit()

