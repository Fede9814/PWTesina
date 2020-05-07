import arcade
import path
import os
import pymunk
import shape
import timeit
import numpy
import math
 
"""
ordine:

le variabili per:
Dove spawna e la probabilità
Direzione da prendere e probabilità
in Setup gli sprite e """

#variabili direzione
nord = 1
sud = 2
est = 3
ovest = 4
cardinali = [nord, sud, est, ovest]
car_list = None

class Car(pygame.sprite.Sprite):
    
#Inizializzazione del mezzo
    def __init__(self):
        self.entra = numpy.random.choice("""qua ci và la lista giusta dei cardinali nuova""", p=[0.25, 0.25, 0.25, 0.25])
        self.direzione = numpy.random.choice(["SX", "DX"], p = [0.50, 0.50])
        self.colore = numpy.random.choice([1, 2, 3, 4, 5], p=[0.20, 0.20, 0.20, 0.20, 0.20 ])


    def setup(self):

        #generate list of sprites
        self.car_list = arcade.SpriteList()

        #color picker ok
        if(self.colore == 1):
            self.car = arcade.Sprite("path_to_the_car_png", 0.5)
            self.car_list.append(self.car)
        elif(self.colore == 2):
            self.car = arcade.Sprite("path_to_the_car_png", 0.5)
            self.car_list.append(self.car)
        elif(self.colore == 3):
            self.car = arcade.Sprite("path_to_the_car_png", 0.5)
            self.car_list.append(self.car)
        elif(self.colore == 4):
            self.car = arcade.Sprite("path_to_the_car_png", 0.5)
            self.car_list.append(self.car)
        elif(self.colore == 5):
            self.car = arcade.Sprite("path_to_the_car_png", 0.5)
            self.car_list.append(self.car)
