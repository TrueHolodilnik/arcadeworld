import arcade

from .Plant import Plant

class Wolfberry(Plant):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(99, 0, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/wolfberry.png", 0, 0, 18, 18)

    def collision(self, target):
        self.GetWorld().remove(target.GetID(), self.GetType(), target.GetType())
        self.GetWorld().remove(self.GetID(), target.GetType(), self.GetType())