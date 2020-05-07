import arcade
import math
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "caret incoming"
speed = 3        
       

class MyGame(arcade.Window):
    """ Main application class """

    def __init__(self, width, height, title):
        super().__init__(width)

        self.frame_count = 0
        self.car = None
        self.end = None
        self.car_list = None
        self.end_list = None
        
    def setup(self):

        # Add car and endpoint to list
        self.end_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()

        car = arcade.Sprite("C:/Users/sanv3/Desktop/PWTesina/PWTesina/Concept Art/car.png", 1)
        car.center_x = 100
        car.center_y = car.height
        car.angle = 180
        self.car = car
        self.car_list.append(car)

        end = arcade.Sprite("C:/Users/sanv3/Desktop/PWTesina/PWTesina/Concept Art/end.png", 1)
        end.center_x = 200
        end.center_y = 400
        self.end = end
        self.end_list.append(end)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        self.end_list.draw()
        self.car_list.draw()
    
    def on_update(self, delta_time=0.50):
        """All the logic to move, and the game logic goes here. """
        self.frame_count += 1
        for car in self.car_list:
        
            #spawn point della macchina
            start_x = car.center_x
            start_y = car.center_y

            #destinazione della macchina
            dest_x = self.end.center_x
            dest_y = self.end.center_y
            
            #calcolo della distanza tra fine ed inizio
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            if self.frame_count % 3 == 0:
                #calcolo della velocità 
                self.car.center_x = start_x
                self.car.center_y = start_y

                self.car.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                self.car.change_x = math.cos(angle) * speed
                self.car.change_y = math.sin(angle) * speed

        self.car_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves. """
        self.end.center_x = x
        self.end.center_y = y

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()