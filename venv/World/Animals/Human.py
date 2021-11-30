import arcade

from .Animal import Animal

class Human(Animal):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        self.aturns = 0
        super().__init__(5, 4, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/asdf.png", 0, 0, 18, 18)

    def action(self, key):
        if key == 65361: self.x = self.x - 1*self.mul
        elif key == 65362: self.y = self.y + 1*self.mul
        elif key == 65363: self.x = self.x + 1*self.mul
        elif key == 65364: self.y = self.y - 1*self.mul
        elif key == 98 and self.aturns == 0:
            self.aturns = 10
            self.SetMul(2)

        if (self.aturns > 0): self.aturns = self.aturns - 1; print("CD: ", self.aturns)
        if (self.aturns < 5) and (self.aturns > 0): self.SetMul(1); print("Ab disact")

        if self.x >= self.GetWSize(): self.x = 0
        elif self.y >= self.GetWSize(): self.y = 0
        elif self.x < 0: self.x = self.GetWSize() - 1
        elif self.y < 0: self.y = self.GetWSize() - 1

    def GetAT(self): return self.aturns
    def SetAT(self, at): self.aturns = at
