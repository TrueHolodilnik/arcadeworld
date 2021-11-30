import arcade
import random

from .Animal import Animal

class Antelope(Animal):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(4, 4, id, x, y, prevx, prevy, wsize, world, type)
        self.SetMul(2)

    def draw(self):
        return arcade.load_texture("venv/Textures/antelope.png", 0, 0, 18, 18)

    def collision(self, target):
        ch = random.randint(0, 1)
        if ch == 1:
            self.SetX(target.GetPrevX())
            self.SetY(target.GetPrevY())
            self.GetWorld().to_log("Antelope has escaped the danger")
            return
        self.col(target)

