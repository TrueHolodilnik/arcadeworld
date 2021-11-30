from abc import ABC, abstractmethod

class Creature(ABC):

    def __init__(self, power, initiative, id, x, y, prevx, prevy, wsize, world, type):
        self.power = power
        self.initiative = initiative
        self.id = id
        self.x = x
        self.y = y
        self.prevx = prevx
        self.prevy = prevy
        self.wsize = wsize
        self.ltime = 0
        self.world = world
        self.type = type
        super().__init__()

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, target):
        pass

    @abstractmethod
    def draw(self):
        pass

    def IncrLT(self): self.ltime = self.ltime + 1

    def SetPower(self, pwr): self.power = pwr
    def SetInit(self, init): self.initiative = init
    def SetX(self, x): self.x = x
    def SetY(self, y): self.y = y
    def SetID(self, id): self.id = id
    def SetPrevX(self, x): self.prevx = x
    def SetPrevY(self, y): self.prevy = y
    def SetLT(self, lt): self.ltime = lt

    def GetPower(self): return self.power
    def GetInit(self): return self.initiative
    def GetX(self): return self.x
    def GetY(self): return self.y
    def GetWSize(self): return self.wsize
    def GetID(self): return self.id
    def GetWorld(self): return self.world
    def GetType(self): return self.type
    def GetPrevX(self): return self.prevx
    def GetPrevY(self): return self.prevy
    def GetLT(self): return self.ltime


