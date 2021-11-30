import arcade
import random
from ..Creature import Creature

class Animal(Creature):

    def __init__(self, power, initiative, id, x, y, prevx, prevy, wsize, world, type):
        self.mul = 1
        super().__init__(power, initiative, id, x, y, prevx, prevy, wsize, world, type)

    def collision(self, target):
        self.col(target)

    def action(self, symbol):
        self.move(-1)

    def draw(self):
        pass

    def move(self, forced):
        dir = random.randint(0, 3)
        if forced != -1: dir = forced
        self.SetPrevX(self.GetX())
        self.SetPrevY(self.GetY())
        if (dir == 0) and (self.GetX() < self.GetWSize() - 1*self.mul):
            self.SetX(self.GetX() + 1*self.mul)
        elif (dir == 1) and (self.GetX() > 0 + self.mul - 1):
            self.SetX(self.GetX() - 1*self.mul)
        elif (dir == 2) and (self.GetY() < self.GetWSize() - 1*self.mul):
            self.SetY(self.GetY() + 1*self.mul)
        elif (dir == 3) and (self.GetY() > 0 + self.mul - 1):
            self.SetY(self.GetY() - 1*self.mul)

    def col(self, target):
        if (target.GetType() == self.GetType()):
            if (self.GetLT() > 5) and (self.GetWorld().GetCSize() < self.GetWSize()*self.GetWSize()*1.5):
                arr = [0, 0]
                arr = self.GetWorld().get_nf_coords(self.GetX(), self.GetY())
                if arr[0] == -1: return
                if arr[0] < 0 or arr[1] < 0 or arr[0] > self.GetWSize() - 1 or arr[1] > self.GetWSize() - 1: return
                self.GetWorld().add(self.__class__(self.GetWorld().GetID(arr), arr[0], arr[1], arr[0], arr[1], self.GetWorld().size, self.GetWorld(), self.GetType()))
                self.GetWorld().to_log("Spawned " + self.GetType() + " on: " + str(arr[0]) + " " + str(arr[1]))
        elif (target.GetPower() > self.GetPower()):
            self.GetWorld().remove(self.GetID(), target.GetType(), self.GetType())
        else:
            self.GetWorld().remove(target.GetID(), self.GetType(), target.GetType())

    def SetMul(self, m): self.mul = m

    def GetMul(self): return self.mul