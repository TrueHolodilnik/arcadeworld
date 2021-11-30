import arcade

from .Plant import Plant

class Mlecz(Plant):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(0, 0, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/mlecz.png", 0, 0, 18, 18)

    def action(self, symbol):
        self.spawn()
        self.spawn()
        self.spawn()