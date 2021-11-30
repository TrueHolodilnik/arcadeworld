import arcade
import random

from .Animal import Animal

class Fox(Animal):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(3, 7, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/fox.png", 0, 0, 18, 18)

    def action(self, symbol):
        moved = False
        it = 0
        while not moved:
            dir = random.randint(0, 3)
            if (dir == 0) and (self.GetWorld().IsCoordsFree(self.GetX() + 1, self.GetY())): self.move(dir); moved = True
            elif (dir == 1) and (self.GetWorld().IsCoordsFree(self.GetX() - 1, self.GetY())): self.move(dir); moved = True
            elif (dir == 2) and (self.GetWorld().IsCoordsFree(self.GetX(), self.GetY() + 1)): self.move(dir); moved = True
            elif (dir == 3) and (self.GetWorld().IsCoordsFree(self.GetX(), self.GetY() - 1)): self.move(dir); moved = True
            it = it + 1
            if (it > self.GetWSize()): return