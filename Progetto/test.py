import arcade
import math
import os
import numpy

# la direzione NORD equivale all'angolo 0
# la direzione OVEST equivale all'angolo 90
# la direzione SUD equivale all'angolo 180
# la direzione EST equivale all'angolo 270

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "caret incoming"      

class MyGame(arcade.Window):
    """ Main application class """

    def __init__(self, width, height, title):
        super().__init__(width)

        self.frame_count = 0
        self.car = None
        self.car1 = None
        self.end = None
        self.car_list = None
        self.end_list = None
        self.los_list = None
        
    def setup(self):

        # Add car and endpoint to list
        self.end_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()
        self.los_list = arcade.SpriteList()

        car = arcade.Sprite("../Concept Art/Blocks/car.png", 1)
        car.center_x = 50
        car.center_y = 50
        print(car.center_x)
        print(car.center_y)
        car.angle = 0 
        self.car = car
        self.car_list.append(car)

        end = arcade.Sprite("../Concept Art/Blocks/end.png", 1)
        end.center_x = 50
        end.center_y = 400
        self.end = end
        self.end_list.append(end)

        los = arcade.Sprite("../Concept Art/Blocks/start.png", 1)
        self.los = los
        self.los_list.append(los)

        print("los_center_x", los.center_x)
        print("los_center_y", los.center_y)
        print("car_top", car.top)
        print("car_bottom", car.bottom)
        print("car_left", car.left)
        print("car_right", car.right)
        print("sprite_top_halved", car.top / 2)
        print(" ")
        print("los_top",    los.top)
        print("los_bottom", los.bottom)
        print("los_left",   los.left)
        print("los_right",  los.right)
        print("sprite_top_halved", los.top / 2)
        print("points", los.points)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        self.end_list.draw()
        self.car_list.draw()
        self.los_list.draw()
    
    def on_update(self, delta_time=0.50):
        """All the logic to move, and the game logic goes here. """
        self.frame_count += 1
        self.initial_speed = 1

        for car in self.car_list:
        
            start_x = car.center_x
            start_y = car.center_y

            self.los.points[4] = car.points[2]
            self.los.points[6] = car.points[1]

            self.los_list.update()

            dest_x = self.end.center_x
            dest_y = self.end.center_y
            
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            if self.frame_count % 1 == 0:
                
                car.angle = math.degrees(angle)

                car.change_x = math.cos(angle) * self.initial_speed
                car.change_y = math.sin(angle) * self.initial_speed

        self.car_list.update()


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()