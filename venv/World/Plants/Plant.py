import arcade
import random
from ..Creature import Creature

class Plant(Creature):

    def __init__(self, power, initiative, id, x, y, prevx, prevy, wsize, world, type):
        self.mul = 1
        super().__init__(power, initiative, id, x, y, prevx, prevy, wsize, world, type)

    def collision(self, target):
        pass

    def action(self, symbol):
        self.spawn()

    def draw(self):
        pass

    def spawn(self):
        ch = random.randint(0, 3)
        if (ch == 1 and self.GetLT() > 5) and (self.GetWorld().GetCSize() < self.GetWSize()*self.GetWSize()*1.5):
            arr = [0, 0]
            arr = self.GetWorld().get_nf_coords(self.GetX(), self.GetY())
            if arr[0] == -1: return
            if arr[0] < 0 or arr[1] < 0 or arr[0] > self.GetWSize() - 1 or arr[1] > self.GetWSize() - 1: return
            self.GetWorld().add(self.__class__(self.GetWorld().GetID(arr), arr[0], arr[1], arr[0], arr[1], self.GetWorld().size,self.GetWorld(), self.GetType()))
            self.GetWorld().to_log("Spawned " + self.GetType() + " on: " + str(arr[0]) + " " + str(arr[1]))
