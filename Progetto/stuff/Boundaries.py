import arcade
import os
import Screen as s
import keyboard

"""window = s.Screen_Class.createWindow()"""

"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 0
PLAYER_JUMP_SPEED = 20

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 500
PLAYER_START_Y = 500


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.foreground_list = None
        self.background_list = None
        self.dont_touch_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Where is the right edge of the map?
        self.end_of_map = 0

        # Level
        self.level = 1

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

    def setup(self, level):
        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.foreground_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        # --- Load in a map from the tiled editor ---

        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for pick-up
        coins_layer_name = 'Coins'
        # Name of the layer that has items for foreground
        foreground_layer_name = 'Foreground'
        # Name of the layer that has items for background
        background_layer_name = 'Background'
        # Name of the layer that has items we shouldn't touch
        dont_touch_layer_name = "Don't Touch"

        # Map name
        map_name = "Test_II.tmx"

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = my_map.map_size.width * GRID_PIXEL_SIZE

        # -- Background
        self.background_list = arcade.tilemap.process_layer(my_map,
                                                            background_layer_name,
                                                            TILE_SCALING)

        # -- Foreground
        self.foreground_list = arcade.tilemap.process_layer(my_map,
                                                            foreground_layer_name,
                                                            TILE_SCALING)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(my_map,
                                                      platforms_layer_name,
                                                      TILE_SCALING)

        # -- Coins
        self.coin_list = arcade.tilemap.process_layer(my_map,
                                                      coins_layer_name,
                                                      TILE_SCALING)

        # -- Don't Touch Layer
        self.dont_touch_list = arcade.tilemap.process_layer(my_map,
                                                            dont_touch_layer_name,
                                                            TILE_SCALING)

        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.background_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()
        self.dont_touch_list.draw()
        self.player_list.draw()
        self.foreground_list.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.BLACK, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
            # Add one to the score
            self.score += 1

        # Track if we need to change the viewport
        changed_viewport = False

        # Did the player fall off the map?
        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True
            arcade.play_sound(self.game_over)

        # Did the player touch something they should not?
        if arcade.check_for_collision_with_list(self.player_sprite,
                                                self.dont_touch_list):
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True
            arcade.play_sound(self.game_over)

        # See if the user got to the end of the level
        if self.player_sprite.center_x >= self.end_of_map:
            # Advance to the next level
            self.level += 1

            # Load the next level
            self.setup(self.level)

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True

        # --- Manage Scrolling ---

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed_viewport = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed_viewport = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed_viewport = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed_viewport = True

        if changed_viewport:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame()
    window.setup(window.level)
    arcade.run()


if __name__ == "__main__":
    main()

"""# Draw a grid
# Draw vertical lines every 120 pixels
for x in range(0, 601, 120):
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)

# Draw horizontal lines every 200 pixels
for y in range(0, 601, 200):
    arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 2)

# Draw a point
arcade.draw_text("draw_point", 3, 405, arcade.color.BLACK, 12)
arcade.draw_point(60, 495, arcade.color.RED, 10)

# Draw a set of points
arcade.draw_text("draw_points", 123, 405, arcade.color.BLACK, 12)
point_list = ((165, 495),
              (165, 480),
              (165, 465),
              (195, 495),
              (195, 480),
              (195, 465))
arcade.draw_points(point_list, arcade.color.ZAFFRE, 10)

# Draw a line
arcade.draw_text("draw_line", 243, 405, arcade.color.BLACK, 12)
arcade.draw_line(270, 495, 300, 450, arcade.color.WOOD_BROWN, 3)

# Draw a set of lines
arcade.draw_text("draw_lines", 363, 405, arcade.color.BLACK, 12)
point_list = ((390, 450),
              (450, 450),
              (390, 480),
              (450, 480),
              (390, 510),
              (450, 510)
              )
arcade.draw_lines(point_list, arcade.color.BLUE, 3)

# Draw a line strip
arcade.draw_text("draw_line_strip", 483, 405, arcade.color.BLACK, 12)
point_list = ((510, 450),
              (570, 450),
              (510, 480),
              (570, 480),
              (510, 510),
              (570, 510)
              )
arcade.draw_line_strip(point_list, arcade.color.TROPICAL_RAIN_FOREST, 3)

# Draw a polygon
arcade.draw_text("draw_polygon_outline", 3, 207, arcade.color.BLACK, 9)
point_list = ((30, 240),
              (45, 240),
              (60, 255),
              (60, 285),
              (45, 300),
              (30, 300))
arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)

# Draw a filled in polygon
arcade.draw_text("draw_polygon_filled", 123, 207, arcade.color.BLACK, 9)
point_list = ((150, 240),
              (165, 240),
              (180, 255),
              (180, 285),
              (165, 300),
              (150, 300))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

# Draw an outline of a circle
arcade.draw_text("draw_circle_outline", 243, 207, arcade.color.BLACK, 10)
arcade.draw_circle_outline(300, 285, 18, arcade.color.WISTERIA, 3)

# Draw a filled in circle
arcade.draw_text("draw_circle_filled", 363, 207, arcade.color.BLACK, 10)
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN)

# Draw an ellipse outline, and another one rotated
arcade.draw_text("draw_ellipse_outline", 483, 207, arcade.color.BLACK, 10)
arcade.draw_ellipse_outline(540, 273, 15, 36, arcade.color.AMBER, 3)
arcade.draw_ellipse_outline(540, 336, 15, 36,
                            arcade.color.BLACK_BEAN, 3, 45)

# Draw a filled ellipse, and another one rotated
arcade.draw_text("draw_ellipse_filled", 3, 3, arcade.color.BLACK, 10)
arcade.draw_ellipse_filled(60, 81, 15, 36, arcade.color.AMBER)
arcade.draw_ellipse_filled(60, 144, 15, 36,
                           arcade.color.BLACK_BEAN, 45)

# Draw an arc, and another one rotated
arcade.draw_text("draw_arc/filled_arc", 123, 3, arcade.color.BLACK, 10)
arcade.draw_arc_outline(150, 81, 15, 36,
                        arcade.color.BRIGHT_MAROON, 90, 360)
arcade.draw_arc_filled(150, 144, 15, 36,
                       arcade.color.BOTTLE_GREEN, 90, 360, 45)

# Draw an rectangle outline
arcade.draw_text("draw_rect", 243, 3, arcade.color.BLACK, 10)
arcade.draw_rectangle_outline(295, 100, 45, 65,
                              arcade.color.BRITISH_RACING_GREEN)
arcade.draw_rectangle_outline(295, 160, 20, 45,
                              arcade.color.BRITISH_RACING_GREEN, 3, 45)

# Draw a filled in rectangle
arcade.draw_text("draw_filled_rect", 363, 3, arcade.color.BLACK, 10)
arcade.draw_rectangle_filled(420, 100, 45, 65, arcade.color.BLUSH)
arcade.draw_rectangle_filled(420, 160, 20, 40, arcade.color.BLUSH, 45)

# Load and draw an image to the screen
# Image from kenney.nl asset pack #1
arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_orange.png")
scale = .6
arcade.draw_scaled_texture_rectangle(540, 120, texture, scale, 0)
arcade.draw_scaled_texture_rectangle(540, 60, texture, scale, 45)"""

"""# Finish the render.
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()"""