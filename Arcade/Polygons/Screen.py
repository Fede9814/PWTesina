import arcade

def Arcade_Window():
    #Generic screen settings
    SCREEN_WIDTH = 2000
    SCREEN_HEIGHT = 2000
    SCREEN_TITLE = "Traffic Simulator"
    Fullscreen = False
    resizable = True
    update_rate = 1/60 #1sec/60FPS (console casul)
    antialiasing = True #Give me some RAM will ya?

    #Screen generator
    arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, Fullscreen, resizable, update_rate, antialiasing)

    #Clear screen - render
    arcade.start_render()

    #Run until closed
    arcade.run()

#For the sake of trying this
"""Arcade_Window()"""