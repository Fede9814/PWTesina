import arcade
from map import *
from screen import *
from car import *

window = window()
window.set_update_rate(1/120)
window.setup()

arcade.run()