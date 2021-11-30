import arcade

from .Animal import Animal

class Wolf(Animal):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(9, 5, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/wolf.png", 0, 0, 18, 18)