import arcade
import os
import pyglet
import time
import timeit
from car import *
from map import *
from cube import *
from FPS_Counter import *

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

        self.background_music_list = []
        self.current_background_song = 0
        self.music = None
        self.BACKGROUND_MUSIC_VOLUME = 0.1

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

        auto1 = car()
        auto1.setup(self.cube_list, self.car_list)
        self.car_list.append(auto1)

    def on_draw(self):       
        arcade.start_render()
        img_map = arcade.load_texture("../Sprites/Road_blocks/map.png")
        img_map.draw_scaled(960, 540)
        for car in self.car_list:
            car.fov.sprite.draw()
            car.fov.stop_sprite.draw()
        self.car_list.draw()

        self.car_list[0].draw()
        
        height = 990
        val = 0
        for i in self.car_list:
            val = val + 1
        #    height = height - 30
        #    if(i.collision == False):
        #        output_draw_time = f"Velocita veicoli: {i.probability_change}"
        #        arcade.draw_text(output_draw_time, 300, height, arcade.color.BLACK, 25)

        output_draw_time = f"Numero Veicoli: {val}"
        arcade.draw_text(output_draw_time, 300, 990, arcade.color.BLACK, 25)

        output_draw_time = f"Frame Count: {self.global_spawn}"
        arcade.draw_text(output_draw_time, 300, 960, arcade.color.BLACK, 25)

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

    def on_update(self, delta_time=0.50):
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

        if(self.global_spawn % 50 == 0):
            self.spawn_car()
            
    def spawn_car(self):
        auto1 = car()
        auto1.setup(self.cube_list, self.car_list)
        self.car_list.append(auto1)
        
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
            auto1 = car()
            auto1.setup(self.cube_list, self.car_list)
            self.car_list.append(auto1)

        if key == arcade.key.P:
            auto = car()
            auto.ignore = True
            auto.speed = 500
            auto.setup(self.cube_list, self.car_list)
            self.car_list.append(auto)

    def set_update_rate(self, rate: float):

        pyglet.clock.unschedule(self.update)
        pyglet.clock.schedule_interval(self.update, rate)
        pyglet.clock.unschedule(self.on_update)
        pyglet.clock.schedule_interval(self.on_update, rate)
