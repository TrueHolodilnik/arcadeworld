import arcade

from .Plant import Plant

class Hogweed(Plant):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(10, 0, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/hogweed.png", 0, 0, 18, 18)

    def action(self, symbol):
        if (self.GetWorld().GetCrByCoords(self.GetX() + 1, self.GetY()) != None and self.GetWorld().GetCrByCoords(self.GetX() + 1, self.GetY()).GetType() != "cybersheep"): self.GetWorld().remove(self.GetWorld().GetCrByCoords(self.GetX() + 1, self.GetY()).GetID(), self.GetType(), self.GetWorld().GetCrByCoords(self.GetX() + 1, self.GetY()).GetType())
        if (self.GetWorld().GetCrByCoords(self.GetX() - 1, self.GetY()) != None and self.GetWorld().GetCrByCoords(self.GetX() - 1, self.GetY()).GetType() != "cybersheep"): self.GetWorld().remove(self.GetWorld().GetCrByCoords(self.GetX() - 1, self.GetY()).GetID(), self.GetType(), self.GetWorld().GetCrByCoords(self.GetX() - 1, self.GetY()).GetType())
        if (self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() + 1) != None and self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() + 1).GetType() != "cybersheep"): self.GetWorld().remove(self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() + 1).GetID() , self.GetType(), self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() + 1).GetType())
        if (self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() - 1) != None and self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() - 1).GetType() != "cybersheep"): self.GetWorld().remove(self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() - 1).GetID() , self.GetType(), self.GetWorld().GetCrByCoords(self.GetX(), self.GetY() - 1).GetType())