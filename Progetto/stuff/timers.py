
import arcade
import random
import os
import timeit
import time
import collections
import pyglet

STOP_COUNT = 12000
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000




class MyGame(arcade.Window):

        self.processing_time = 0
        self.draw_time = 0
        self.program_start_time = timeit.default_timer()
        self.fps_list = []
        self.processing_time_list = []
        self.drawing_time_list = []
        self.last_fps_reading = 0
        self.fps = FPSCounter()

        # Open file to save timings
        self.results_file = open(RESULTS_FILE, "w")

    def on_draw(self):
        """ Draw everything """

        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 40, arcade.color.BLACK, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 60, arcade.color.BLACK, 16)

        fps = self.fps.get_fps()
        output = f"FPS: {fps:3.0f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 80, arcade.color.BLACK, 16)

        self.draw_time = timeit.default_timer() - draw_start_time
        self.fps.tick()

    def update(self, delta_time):
        # Start update timer

        start_time = timeit.default_timer()
        self.processing_time = timeit.default_timer() - start_time
        total_program_time = int(timeit.default_timer() - self.program_start_time)
        if total_program_time > self.last_fps_reading:
            self.last_fps_reading = total_program_time
            if total_program_time > 5:
                if total_program_time % 2 == 1:
                    output = f"{total_program_time}, {len(self.coin_list)}, {self.fps.get_fps():.1f}, " \
                            f"{self.processing_time:.4f}, {self.draw_time:.4f}\n"

                    print(output, end="")
                    self.results_file.write(output)

                    if len(self.coin_list) >= STOP_COUNT:
                        self.results_file.close()
                        pyglet.app.exit()
                        return

                    # Take timings
                    print(f"{total_program_time}, {len(self.coin_list)}, {self.fps.get_fps():.1f}, "
                          f"{self.processing_time:.4f}, {self.draw_time:.4f}")
                    self.sprite_count_list.append(len(self.coin_list))
                    self.fps_list.append(round(self.fps.get_fps(), 1))
                    self.processing_time_list.append(self.processing_time)
                    self.drawing_time_list.append(self.draw_time)