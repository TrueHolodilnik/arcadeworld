import arcade
import random

from .Animal import Animal

class Turtle(Animal):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(2, 1, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/turtle.png", 0, 0, 18, 18)

    def action(self, symbol):
        ch = random.randint(0, 3)
        if ch == 1: self.move(-1)
        else: self.GetWorld().to_log("Turtle decided not to move")

    def collision(self, target):
        if target.GetPower() < 5:
            self.GetWorld().to_log("Turtle has parried attack")
            target.SetX(target.GetPrevX())
            target.SetY(target.GetPrevY())
            return
        self.col(target)

