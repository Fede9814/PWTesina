import arcade
from map import *
from Screen import *
from car import *
from Collision import *

window = window()
window.set_update_rate(1/120)
window.setup()

arcade.run()