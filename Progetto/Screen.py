import arcade
import asyncio
import os
import pyglet
import time
import timeit
from car import *
from map import *
from cube import *
from FPS_Counter import *
from timeit import default_timer as timer

USE_SPATIAL_HASHING = True
if USE_SPATIAL_HASHING:
    RESULTS_FILE = "stress_test_collision_arcade_spatial.csv"
else:
    RESULTS_FILE = "stress_test_collision_arcade.csv"

class window(arcade.Window):

    def __init__(self):
        super().__init__(width=1920, height=1080, title="Traffic Simulator", fullscreen=False)
        self.cube_list = []
        self.car_list = None
        self.change = 0
        self.current_status = 1
        self.frame_count = 0
        self.yellow_start = False
        self.yellow_count = 0
        self.yellow_time = 30
        self.red_time = 200
        self.global_spawn = 0
        self.hour = 20
        self.timer_start = None
        self.timer_now = None
        self.timer_result = None
        self.timer_second = 0
        self.timer_second_sup = 0
        self.timer_minute = 0
        self.timer_string_min = "00"
        self.timer_string_sec = "00"
        self.total_car = 0
        self.total_car_min = 0
        self.spawn_rate = 0
        self.incidenti_min = 0

        self.background_music_list = []
        self.current_background_song = 0
        self.music = None
        self.BACKGROUND_MUSIC_VOLUME = 0

        self.results_file = open(RESULTS_FILE, "w")

    def play_background_song(self):
        self.background_music = arcade.Sound(self.background_music_list[self.current_background_song], streaming=True)
        self.background_music.play(self.BACKGROUND_MUSIC_VOLUME)

    def setup(self):
        self.background_music_list = ["../Sound/traffic.wav"]
        self.current_background_song = 0
        self.play_background_song()

        y = 1050
        for j in map:
            x = 30
            for i in j:
                self.cube_list.append(cube(x-30, y-30, x, y, i))
                x = x + 60
            y = y - 60  
      
        self.car_list = arcade.SpriteList()

        auto = car()
        auto.setup(self.cube_list, self.car_list)
        auto.time_service(self.hour, self.timer_minute, self.timer_second)
        self.car_list.append(auto)
        self.total_car += 1
        self.total_car_min += 1
        
        self.timer_start = datetime.datetime.now().replace(microsecond=0)

    def on_draw(self):       
        arcade.start_render()
        img_map = arcade.load_texture("../Sprites/Road_blocks/map.png")
        img_map.draw_scaled(960, 540)
        for car in self.car_list:
            car.fov.sprite.draw()
            car.fov.stop_sprite.draw()

        self.car_list.draw()
        try:
            self.incidenti = self.car_list[0].get_incidenti()
            self.incidenti_min = self.incidenti
        except:
            self.incidenti = self.incidenti
        
        height = 990
        val = 0
        for i in self.car_list:
            val = val + 1
        #    height = height - 30
        #    if(i.collision == False):
        #        output_draw_time = f"Velocita veicoli: {i.probability_change}"
        #        arcade.draw_text(output_draw_time, 300, height, arcade.color.BLACK, 25)

        output_draw_time = f"Numero Veicoli Totali: {self.total_car}"
        arcade.draw_text(output_draw_time, 300, 1020, arcade.color.BLACK, 25)

        output_draw_time = f"Numero Veicoli Nell'Incrocio: {val}"
        arcade.draw_text(output_draw_time, 300, 990, arcade.color.BLACK, 25)

        output_draw_time = f"Frame Count: {self.global_spawn}"
        arcade.draw_text(output_draw_time, 300, 960, arcade.color.BLACK, 25)

        output_draw_time = f"Incidenti: {self.incidenti}"
        arcade.draw_text(output_draw_time, 300, 930, arcade.color.BLACK, 25)

        output_draw_time = f"Cronometro: {self.hour}:{self.timer_string_min}:{self.timer_string_sec}"
        arcade.draw_text(output_draw_time, 300, 900, arcade.color.BLACK, 25)


        if(self.current_status == 1 and self.yellow_start == False):
            cube = arcade.load_texture("../Sprites/Lights/Green.png")
            cube.draw_scaled(810, 750, angle=180)
        elif(self.current_status == 1 and self.yellow_start == True):
            cube = arcade.load_texture("../Sprites/Lights/Yellow.png")
            cube.draw_scaled(810, 750, angle=180)
        else:
            cube = arcade.load_texture("../Sprites/Lights/Red.png")
            cube.draw_scaled(810, 750, angle=180)

        if(self.current_status == 2 and self.yellow_start == False):
            cube = arcade.load_texture("../Sprites/Lights/Green.png")
            cube.draw_scaled(1170, 690, angle=90)
        elif(self.current_status == 2 and self.yellow_start == True):
            cube = arcade.load_texture("../Sprites/Lights/Yellow.png")
            cube.draw_scaled(1170, 690, angle=90)
        else:
            cube = arcade.load_texture("../Sprites/Lights/Red.png")
            cube.draw_scaled(1170, 690, angle=90)

        if(self.current_status == 3 and self.yellow_start == False):
            cube = arcade.load_texture("../Sprites/Lights/Green.png")
            cube.draw_scaled(1110, 330)
        elif(self.current_status == 3 and self.yellow_start == True):
            cube = arcade.load_texture("../Sprites/Lights/Yellow.png")
            cube.draw_scaled(1110, 330)
        else:
            cube = arcade.load_texture("../Sprites/Lights/Red.png")
            cube.draw_scaled(1110, 330)

        if(self.current_status == 4 and self.yellow_start == False):
            cube = arcade.load_texture("../Sprites/Lights/Green.png")
            cube.draw_scaled(750, 390, angle=270)
        elif(self.current_status == 4 and self.yellow_start == True):
            cube = arcade.load_texture("../Sprites/Lights/Yellow.png")
            cube.draw_scaled(750, 390, angle=270)
        else:
            cube = arcade.load_texture("../Sprites/Lights/Red.png")
            cube.draw_scaled(750, 390, angle=270)

    def advance_song(self):
        self.current_background_song += 1
        if self.current_background_song >= len(self.background_music_list):
            self.current_background_song = 0

    def query_5_min(self):
        self.cursor = cursor
        self.cursor.execute("INSERT INTO dbo.ClockTable (NVehicle, Hours, Collision) VALUES (?, ?, ?)", (self.total_car_min, self.hour, self.incidenti_min))
        cursor.commit()
        cursor.cancel()
        self.incidenti_min = 0
        self.total_car_min = 0

    def on_update(self, delta_time=0.50):


        self.timer_now = datetime.datetime.now().replace(microsecond=0)
        self.timer_result =  self.timer_now - self.timer_start

        if(self.timer_result.seconds != self.timer_second_sup):
            self.timer_second_sup = self.timer_result.seconds
            self.timer_second = self.timer_second + 1
            if(self.timer_second <= 9):
                self.timer_string_sec = "0" + str(self.timer_second)
            else:
                self.timer_string_sec = str(self.timer_second)
        if(self.timer_second == 59):
            self.timer_second = 0
            self.timer_minute = self.timer_minute + 1
            if(self.timer_minute % 5 == 0):
                self.query_5_min()
                if(self.hour <= 23):
                    self.hour += 1
            if(self.timer_minute <= 9):
                self.timer_string_min = "0" + str(self.timer_minute)
            else:
                self.timer_string_min = str(self.timer_minute)

        self.global_spawn += 1
        background_music_looper = self.background_music.get_stream_position()
        if background_music_looper == 0.0:
            self.advance_song()
            self.play_background_song()

        if(self.frame_count % self.red_time == 0 and self.frame_count != 0):
            self.yellow_start = True
            if(self.yellow_count == 0):
                for cube in self.cube_list:
                    if(cube.val == 4):
                        if(cube.stop_status == True):
                            cube.stop_status = False
            if(self.yellow_count % self.yellow_time == 0 and self.yellow_count != 0):
                self.yellow_start = False
                self.yellow_count = 0
                if(self.current_status < 4):
                    self.current_status += 1
                else:
                    self.current_status = 1
                for cube in self.cube_list:
                    if(cube.val == 4 or cube.val == 6):
                        cube.change_status(self.current_status)
            else:
                self.yellow_count += 1
        if(self.yellow_start != True):
            self.frame_count += 1

        for car in self.car_list:
            car.set_car_list(self.car_list)
        
        self.car_list.update()
        for car in self.car_list:
            car.fov.sprite.update()
            car.fov.stop_sprite.update()

        if(self.hour == 1 or self.hour == 2 or self.hour == 3 or self.hour == 4):
            self.spawn_rate = 1500
        elif(self.hour == 5 or self.hour == 0):
            self.spawn_rate = 750
        elif(self.hour == 6 or self.hour == 23):
            self.spawn_rate = 500
        elif(self.hour == 7 or self.hour == 11 or self.hour == 22):
            self.spawn_rate = 300
        elif(self.hour == 8 or self.hour == 10 or self.hour == 16 or self.hour == 21):
            self.spawn_rate = 200
        elif(self.hour == 9 or self.hour == 20):
            self.spawn_rate = 150
        elif(self.hour == 15 or self.hour == 17 or self.hour == 19):
            self.spawn_rate = 125
        elif(self.hour == 12 or self.hour == 14 or self.hour == 18):
            self.spawn_rate = 100
        elif(self.hour == 13):
            self.spawn_rate = 75

        if(self.global_spawn % self.spawn_rate == 0):
            self.spawn_car()
            
    def spawn_car(self):
        auto = car()
        auto.setup(self.cube_list, self.car_list)
        auto.time_service(self.hour, self.timer_minute, self.timer_second)
        self.car_list.append(auto)
        self.total_car += 1
        self.total_car_min += 1


        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height) 
        
        if key == arcade.key.C:
            if(self.change == 1):
                for auto in self.car_list:
                    if(auto.fov.sprite.alpha != 0):
                        auto.fov.sprite.alpha = 0
                        auto.fov.stop_sprite.alpha = 0
                self.change = 0  
            else:
                for auto in self.car_list:
                    if(auto.fov.sprite.alpha == 0):
                        auto.fov.sprite.alpha = 255 
                        auto.fov.stop_sprite.alpha = 255
                self.change = 1   

        if key == arcade.key.KEY_1:
            auto = car()
            auto.setup(self.cube_list, self.car_list)
            auto.time_service(self.hour, self.timer_minute, self.timer_second)
            self.car_list.append(auto)
            self.total_car += 1
            self.total_car_min += 1

        if key == arcade.key.P:
            auto = car()
            auto.ignore = True
            auto.speed = 500
            auto.setup(self.cube_list, self.car_list)
            auto.time_service(self.hour, self.timer_minute, self.timer_second)
            self.car_list.append(auto)
            self.total_car += 1
            self.total_car_min += 1

        if key == arcade.key.UP:
            if(self.hour < 23):
                self.hour = self.hour + 1
                self.timer_start = datetime.datetime.now().replace(microsecond=0)
                self.timer_second = 0
                self.timer_minute = 0
                self.timer_string_min = "00"
                self.timer_string_sec = "00"
                self.incidenti_min = 0
                self.total_car_min = 0

        if key == arcade.key.DOWN:
            if(self.hour > 0):
                self.hour = self.hour - 1
                self.timer_start = datetime.datetime.now().replace(microsecond=0)
                self.timer_second = 0
                self.timer_minute = 0
                self.timer_string_min = "00"
                self.timer_string_sec = "00"
                self.incidenti_min = 0
                self.total_car_min = 0
            

    def set_update_rate(self, rate: float):

        pyglet.clock.unschedule(self.update)
        pyglet.clock.schedule_interval(self.update, rate)
        pyglet.clock.unschedule(self.on_update)
        pyglet.clock.schedule_interval(self.on_update, rate)
