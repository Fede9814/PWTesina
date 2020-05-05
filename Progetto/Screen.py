import arcade
import keyboard
import os

class Screen_Class(arcade.Window):

    @staticmethod
    def createWindow():

        SET_SCREEN_WIDTH = 1500
        SET_SCREEN_HEIGHT = 1200
        SET_SCREEN_TITLE = "Traffic Simulator"
        SET_resizable = True
        SET_antialiasing = True #Give me some RAM will ya?
 
        arcade.open_window(     SET_SCREEN_WIDTH, 
                                SET_SCREEN_HEIGHT, 
                                SET_SCREEN_TITLE,  
                                SET_resizable,
                                SET_antialiasing,)

        arcade.start_render()