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
        self.end = None
        self.car_list = None
        self.end_list = None
        self.move = None
        
    def setup(self):

        # Add car and endpoint to list
        self.end_list = arcade.SpriteList()
        self.car_list = arcade.SpriteList()
        self.x = arcade.SpriteList()

        car = arcade.Sprite("../Concept Art/Blocks/car.png", 1)
        car.center_x = 400
        car.center_y = 50
        car.angle = 0 
        car.collision_radius = 20
        self.car = car
        self.car_list.append(car)

        punto_a = self.car.points[1]
        punto_b = self.car.points[3]

        punto_a_x = punto_a[0]
        punto_a_y = punto_a[1]
        punto_b_x = punto_b[0]
        punto_b_y = punto_b[1]

        punto_c_x = (punto_a_x + punto_b_x)/2
        punto_c_y = (punto_a_y + punto_b_y)/2

        car = arcade.Sprite("../Concept Art/Blocks/start.png", 1)
        car.angle = 0 
        self.x1 = car
        self.x1.center_x = punto_c_x
        self.x1.center_y = punto_c_y
        self.x.append(car)

        end = arcade.Sprite("../Concept Art/Blocks/end.png", 1)
        end.center_x = 50
        end.center_y = 400
        self.end = end
        self.end_list.append(end)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        self.end_list.draw()
        self.x.draw()
        self.car_list.draw()
        
        punto_a = self.car.points[1]
        punto_b = self.car.points[3]

        punto_a_x = punto_a[0]
        punto_a_y = punto_a[1]
        punto_b_x = punto_b[0]
        punto_b_y = punto_b[1]

        punto_c_x = (punto_a_x + punto_b_x)/2
        punto_c_y = (punto_a_y + punto_b_y)/2

        arcade.draw_point(punto_c_x, punto_c_y, arcade.color.BLUE, 5)      
        
    
    def on_update(self, delta_time=0.50):
        
        self.initial_speed = 1
            
        start_x = self.car.center_x
        start_y = self.car.center_y

        dest_x = self.end.center_x
        dest_y = self.end.center_y
        
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        
        for cars in self.end_list:
            if arcade.check_for_collision(self.x1, cars):
                self.move = False
                break
            else:
                self.move = True
        print(self.move)
        if self.move == True:
            
            self.car.angle = math.degrees(angle)

            self.car.change_x = math.cos(angle) * self.initial_speed
            self.car.change_y = math.sin(angle) * self.initial_speed

            punto_a = self.car.points[1]
            punto_b = self.car.points[3]

            punto_a_x = punto_a[0]
            punto_a_y = punto_a[1]
            punto_b_x = punto_b[0]
            punto_b_y = punto_b[1]

            punto_c_x = (punto_a_x + punto_b_x)/2
            punto_c_y = (punto_a_y + punto_b_y)/2

            self.x1.center_x =  punto_c_x
            self.x1.center_y = punto_c_y

            self.x1.angle = self.car.angle


            self.car_list.update()
        self.x.update()

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