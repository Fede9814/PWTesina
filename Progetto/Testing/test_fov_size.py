import numpy
import math
import arcade

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Rectangle Example"

# Size of the rectangle
RECT_WIDTH = 50
RECT_HEIGHT = 50

age_range =             [20, 40, 60, 80]
#questo è ok
Speed_range =           [1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
#questo è ok
μ_global_range =        [0.1, 0.8]
#questo è ok
reaction_time_range =   [1.5, 3.0, 4.5]
#questo è fisso
fixed_value =           250

age = numpy.random.choice(
#questo è ok
age_range, p=[0.22, 0.54, 0.10, 0.14])
#questo è ok
Speed = numpy.random.choice(
Speed_range, p=[0.05, 0.10, 0.35, 0.35, 0.10, 0.05])
#questo è ok
reaction_time = numpy.random.choice(
reaction_time_range, p=[0.8, 0.18, 0.02])
#questo è ok
μ_value = numpy.random.choice(
μ_global_range, p=[0.01, 0.99])
#questo è ok
skill_factor = 0#fov calculations

if age == 20 or age == 80:
    skill_factor = 0.6
elif age == 40:
    skill_factor = 0.0
elif age == 60:
    skill_factor = 0.2
#print("Skill", skill_factor)

if skill_factor == 0.6:
    R_dist = ((math.pow(Speed, 2.0) *
                    reaction_time)/(3.6 - skill_factor))

#print("R_dist", R_dist)
elif skill_factor == 0.0:
    R_dist = ((math.pow(Speed, 2.0) * reaction_time)/(3.6 + skill_factor))

#print("R_dist", R_dist)
elif skill_factor == 0.2:
    R_dist = ((math.pow(Speed, 2.0) * reaction_time)/(3.6 - skill_factor))
    print("R_dist", R_dist)

B_dist = ((math.pow(Speed, 2.0) /(fixed_value * μ_value)))
print("B_dist",B_dist)

FOV_length = R_dist + B_dist

print(FOV_length)


def on_draw(delta_time):

    arcade.start_render()
    arcade.draw_line(270,0,270,600, arcade.color.WINE)
    arcade.draw_line(330,0,330,600, arcade.color.WINE)
    hitbox_list = arcade.SpriteList()
    car_list = arcade.SpriteList()
    car = arcade.Sprite("../Concept Art/Blocks/car.png", 1, center_x=300, center_y=300)
    hitbox = arcade.Sprite("../Concept Art/hitbox.png", FOV_length, center_x=300, center_y=300)
    hitbox_list.append(hitbox)
    hitbox_list.draw()


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 80)

    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()