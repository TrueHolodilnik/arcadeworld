import arcade

from .Animal import Animal

class Cybersheep(Animal):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(11, 4, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/cybersheep.png", 0, 0, 18, 18)

    def action(self, symbol):
        nc = self.GetWorld().get_nft_coords(self.GetX(), self.GetY(), "hogweed", self)
        if nc != None:
            if nc[0] > self.GetX(): self.move(0)
            elif nc[0] < self.GetX(): self.move(1)
            elif nc[1] > self.GetY(): self.move(2)
            elif nc[1] < self.GetY(): self.move(3)
            else: self.move(-1)
        else: self.move(-1)