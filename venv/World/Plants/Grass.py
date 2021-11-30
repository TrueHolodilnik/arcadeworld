import arcade

from .Plant import Plant

class Grass(Plant):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(0, 0, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/grass.png", 0, 0, 18, 18)