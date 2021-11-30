import arcade

from .Animal import Animal

class Sheep(Animal):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(4, 4, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/sheep.png", 0, 0, 18, 18)