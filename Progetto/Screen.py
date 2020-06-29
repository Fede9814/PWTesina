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
        self.yellow_time = 20
        self.red_time = 120

        self.background_music_list = []
        self.car_music_list = []
        self.tir_music_list = []
        self.bike_music_list = []

        self.current_background_song = 0
        self.current_car_song = 0
        self.current_tir_song = 0
        self.current_bike_song = 0

        self.music = None
        self.BACKGROUND_MUSIC_VOLUME = 0
        self.CAR_MUSIC_VOLUME = 0.1
        self.TIR_MUSIC_VOLUME = 0.1
        self.BIKE_MUSIC_VOLUME = 0.1

        self.processing_time = 0
        self.draw_time = 0
        self.program_start_time = timeit.default_timer()
        self.fps_list = []
        self.processing_time_list = []
        self.drawing_time_list = []
        self.last_fps_reading = 0
        self.fps = FPSCounter()

        self.results_file = open(RESULTS_FILE, "w")

    def play_background_song(self):
        self.background_music = arcade.Sound(self.background_music_list[self.current_background_song], streaming=True)
        self.background_music.play(self.BACKGROUND_MUSIC_VOLUME)

    def play_car_song(self):
        self.car_music = arcade.Sound(self.car_music_list[self.current_car_song], streaming=True)
        self.car_music.play(self.CAR_MUSIC_VOLUME)

    def play_tir_song(self):
        self.tir_music = arcade.Sound(self.tir_music_list[self.current_tir_song], streaming=True)
        self.tir_music.play(self.TIR_MUSIC_VOLUME)

    def play_bike_song(self):
        self.bike_music = arcade.Sound(self.bike_music_list[self.current_bike_song], streaming=True)
        self.bike_music.play(self.BIKE_MUSIC_VOLUME)
    

    def setup(self):
        self.background_music_list = ["../Sound/traffic.wav"]
        self.car_music_list = ["../Sound/1_crash.wav"]
        self.tir_music_list = ["../Sound/2_splat.wav"]
        self.bike_music_list = ["../Sound/3_burn.wav"]
        self.current_background_song = 0
        self.play_background_song()
        self.total_execution_time = 0.0
        self.processing_time = 0
        self.processing_time_list = []
        self.program_start_time = timeit.default_timer()

        y = 1050
        for j in map:
            x = 30
            for i in j:
                self.cube_list.append(cube(x-30, y-30, x, y, i))
                x = x + 60
            y = y - 60  
      

        self.car_list = arcade.SpriteList()

        auto1 = car("../Sprites/Car/car_1.png", 1)
        auto1.setup(self.cube_list, self.car_list)
        self.car_list.append(auto1)


    def on_draw(self):       
        arcade.start_render()
        for cube in self.cube_list:
            cube.recognition(cube.pos_x, cube.pos_y)
        for car in self.car_list:
            car.fov.sprite.draw()
            car.fov.stop_sprite.draw()
        self.car_list.draw()
        
        

        height = 990
        val = 0
        for i in self.car_list:
            val = val + 1
            height = height - 30
            if(i.collision == False):
                output_draw_time = f"Velocita veicoli: {i.probability_change}"
                arcade.draw_text(output_draw_time, 300, height, arcade.color.BLACK, 25)

        output_draw_time = f"Numero Veicoli: {val}"
        arcade.draw_text(output_draw_time, 300, 990, arcade.color.BLACK, 25)


        #hours = int(self.total_execution_time) // 3600
        #minutes = int(self.total_execution_time) // 60
        #seconds = int(self.total_execution_time) % 60
 
        #elapsed_time_output = f"Elapsed Time: {hours:02d}:{minutes:02d}:{seconds:02d}"
        #arcade.draw_text(elapsed_time_output, 300, 960, arcade.color.BLACK, 25)
 
        #draw_start_time = timeit.default_timer()
 
        #output_processing_time = f"Processing time: {self.processing_time:.3f}"
        #arcade.draw_text(output_processing_time, 300, 930, arcade.color.BLACK, 25)
 
        #output_draw_time = f"Drawing time: {self.draw_time:.3f}"
        #arcade.draw_text(output_draw_time, 300, 900, arcade.color.BLACK, 25)
 
        #fps = self.fps.get_fps()
        #output_draw_text = f"FPS: {fps:3.0f}"
        #arcade.draw_text(output_draw_text, 300, 870, arcade.color.BLACK, 25)
 
        #self.draw_time = timeit.default_timer() - draw_start_time
        #self.fps.tick()

    def advance_song(self):
        self.current_background_song += 1
        if self.current_background_song >= len(self.background_music_list):
            self.current_background_song = 0

    def on_update(self, delta_time=0.50):

        background_music_looper = self.background_music.get_stream_position()
        if background_music_looper == 0.0:
            self.advance_song()
            self.play_background_song()

        self.total_execution_time += delta_time


        start_time = timeit.default_timer()
        self.processing_time = timeit.default_timer() - start_time
        total_program_time = int(timeit.default_timer() - self.program_start_time)
        if total_program_time > self.last_fps_reading:
            self.last_fps_reading = total_program_time
            if total_program_time > 5:
                if total_program_time % 2 == 1:
                    output = f"{total_program_time}, {self.fps.get_fps():.1f}, " \
                            f"{self.processing_time:.4f}, {self.draw_time:.4f}\n"

                    self.results_file.write(output)

                self.fps_list.append(round(self.fps.get_fps(), 1))
                self.processing_time_list.append(self.processing_time)
                self.drawing_time_list.append(self.draw_time)

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
                    if(cube.val == 4):
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
            auto1 = car("../Sprites/Car/car_1.png", 1)
            auto1.setup(self.cube_list, self.car_list)
            self.car_list.append(auto1)

        #if key == arcade.key.KEY_2:
        #    auto2 = car("../Sprites/Car/car_2.png", 1)
        #    auto2.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto2)
 
        #if key == arcade.key.KEY_3:
        #    auto3 = car("../Sprites/Car/car_3.png", 1)
        #    auto3.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto3)
        #
        #if key == arcade.key.KEY_4:
        #    auto4 = car("../Sprites/Car/car_4.png", 1)
        #    auto4.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto4)
 
        #if key == arcade.key.KEY_5:
        #    auto5 = car("../Sprites/Car/car_5.png", 1)
        #    auto5.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto5)
        #
        #if key == arcade.key.KEY_6:
        #    auto6 = car("../Sprites/Car/TIR_1.png", 1)
        #    auto6.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto6)
 
        #if key == arcade.key.KEY_7:
        #    auto7 = car("../Sprites/Car/TIR_2.png", 1)
        #    auto7.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto7)
 
        #if key == arcade.key.KEY_8:
        #    auto8 = car("../Sprites/Car/TIR_3.png", 1)
        #    auto8.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto8)
 
 
        #if key == arcade.key.KEY_9:
        #    auto9 = car("../Sprites/Car/bike_1.png", 1)
        #    auto9.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto9)
 
 
        #if key == arcade.key.KEY_0:
        #    auto10 = car("../Sprites/Car/bike_2.png", 1)
        #    auto10.setup(self.cube_list, self.car_list)
        #    self.car_list.append(auto10)


        if key == arcade.key.P:
            auto = car("../Sprites/Car/car_3.png", 1)
            auto.ignore = True
            auto.speed = 500
            auto.setup(self.cube_list, self.car_list)
            self.car_list.append(auto)

    def set_update_rate(self, rate: float):

        pyglet.clock.unschedule(self.update)
        pyglet.clock.schedule_interval(self.update, rate)
        pyglet.clock.unschedule(self.on_update)
        pyglet.clock.schedule_interval(self.on_update, rate)
