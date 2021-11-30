import arcade

from .Plant import Plant

class Guarana(Plant):

    def __init__(self, id, x, y, prevx, prevy, wsize, world, type):
        super().__init__(0, 0, id, x, y, prevx, prevy, wsize, world, type)

    def draw(self):
        return arcade.load_texture("venv/Textures/guarana.png", 0, 0, 18, 18)

    def collision(self, target):
        if isinstance(target, Plant): return
        target.SetPower(target.GetPower() + 3)
        self.GetWorld().to_log("Guarana has increased strength of " + target.GetType())