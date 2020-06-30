import pyodbc
from fov import *


class writeOnDB():
    def connectionString(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=DESKTOP-7PATCN6\SQL;'
                            'Database=test;'
                            'Trusted_Connection=yes;')
    def queryThis(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO Car_Information (CarBirthTime, CarDeathTime, CarLifeSpan,  IDVehicle,   Gender, Age,  Name, Surname, Plate, Region, Model, Displacement, CarTax, Insurance) VALUES ())
        self.cursor.commit()

