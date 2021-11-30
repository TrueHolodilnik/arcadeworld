import arcade
import random
from tkinter import *
from .SaveManager import SaveManager
from .Creature import Creature
from .Animals.Human import Human
from .Animals.Wolf import Wolf
from .Animals.Sheep import Sheep
from .Animals.Fox import Fox
from .Animals.Turtle import Turtle
from .Animals.Antelope import Antelope
from .Animals.Cybersheep import Cybersheep
from .Plants.Grass import Grass
from .Plants.Mlecz import Mlecz
from .Plants.Guarana import Guarana
from .Plants.Wolfberry import Wolfberry
from .Plants.Hogweed import Hogweed

ISIZE = 22
MARGIN = 1

class GWorld(arcade.Window):

    def add(self, Creature):
        self.creatures.append(Creature)

    def remove(self, id, t1, t2):
        for i in range(len(self.creatures) - 1):
            if self.creatures[i].GetID() == id:
                self.creatures.remove(self.creatures[i])
                self.to_log("Creature " + t1 + " destroyded " + t2)
                if (t2 == "human"): self.is_dead = True
                return

    def init_creatures(self):

        cr = Human(0, int(self.size / 2), int(self.size / 2), int(self.size / 2), int(self.size / 2), self.size, self, "human")
        self.add(cr)

        arr = [0, 0]
        for i in range(4):
            arr = self.get_rf_coords()
            cr = Wolf(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "wolf")
            self.add(cr)
            self.to_log("Spawned wolf on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Sheep(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "sheep")
            self.add(cr)
            self.to_log("Spawned sheep on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Fox(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "fox")
            self.add(cr)
            self.to_log("Spawned fox on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Turtle(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "turtle")
            self.add(cr)
            self.to_log("Spawned turtle on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Antelope(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "antelope")
            self.add(cr)
            self.to_log("Spawned antelope on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Grass(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "grass")
            self.add(cr)
            self.to_log("Spawned grass on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Mlecz(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "mlecz")
            self.add(cr)
            self.to_log("Spawned mlecz on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Guarana(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "guarana")
            self.add(cr)
            self.to_log("Spawned guarana on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Wolfberry(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "wolfberry")
            self.add(cr)
            self.to_log("Spawned wolfberry on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Hogweed(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "hogweed")
            self.add(cr)
            self.to_log("Spawned hogweed on: " + str(arr[0]) + " " + str(arr[1]))

            arr = self.get_rf_coords()
            cr = Cybersheep(self.GetID(arr), arr[0], arr[1], arr[0], arr[1], self.size, self, "cybersheep")
            self.add(cr)
            self.to_log("Spawned cybersheep on: " + str(arr[0]) + " " + str(arr[1]))

    def to_log(self, str):
        self.log = self.log + str + "\n"

    def __init__(self, size):
        super().__init__(1280, 720, "Virtual World")

        self.size = size;
        self.creatures = []
        self.log = " "
        self.is_dead = False

        self.grid = []
        for row in range(size + 1):
            self.grid.append([])
            for column in range(size + 1):
                self.grid[row].append(0)

        self.delta = False

        self.init_creatures()

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        if self.delta:
            for row in range(self.size + 1):
                for column in range(self.size + 1):
                    self.grid[row][column] = 0

        for row in range(self.size):
            for column in range(self.size):
                texture = arcade.load_texture("venv/Textures/earth.png", 0, 0, 18, 18)

                # Do the math to figure out where the box is
                x = (MARGIN + ISIZE) * column + MARGIN + ISIZE // 2
                y = (MARGIN + ISIZE) * row + MARGIN + ISIZE // 2

                # Draw the box
                arcade.draw_xywh_rectangle_textured(x, y, ISIZE, ISIZE, texture)

        for i in range(len(self.creatures) - 1):
            # Figure out what color to draw the box
            texture = self.creatures[i].draw()

            # Do the math to figure out where the box is
            x = (MARGIN + ISIZE) * (self.creatures[i].GetX()) + MARGIN + ISIZE // 2
            y = (MARGIN + ISIZE) * (self.creatures[i].GetY()) + MARGIN + ISIZE // 2

            # Draw the box
            arcade.draw_xywh_rectangle_textured(x, y, ISIZE, ISIZE, texture)

            if self.delta:
                self.grid[self.creatures[i].GetX()][self.creatures[i].GetY()] = 1


        arcade.draw_text("World size: " + str(self.size) + ". B - ability, S/L - save/load", 720, 685, arcade.csscolor.WHITE, 16)
        arcade.draw_text("Log: " + self.log, 720, 10, arcade.csscolor.WHITE, 12)
        if self.is_dead: arcade.draw_text("lol, you died" , 720, 665, arcade.csscolor.WHITE, 16)

    def on_mouse_press(self, x, y, button, modifiers):
        column = (x // (ISIZE + MARGIN)) - 1
        row = (y // (ISIZE + MARGIN)) - 1

        print("spawn: ", row, column)

        if row > self.size or column > self.size: return

        master = Tk()

        cr = None

        arr = [row, column]

        def end(creat):
            self.add(creat)
            self.to_log("Spawned sheep on: " + str(arr[1]) + " " + str(arr[0]))
            master.destroy()

        def sheep():
            cr = Sheep(self.GetID(arr), column, row, column, row, self.size, self, "sheep")
            end(cr)

        def wolf():
            cr = Wolf(self.GetID(arr), column, row, column, row, self.size, self, "wolf")
            end(cr)

        def antelope():
            cr = Antelope(self.GetID(arr), column, row, column, row, self.size, self, "antelope")
            end(cr)

        def cybersheep():
            cr = Cybersheep(self.GetID(arr), column, row, column, row, self.size, self, "cybersheep")
            end(cr)

        def fox():
            cr = Fox(self.GetID(arr), column, row, column, row, self.size, self, "fox")
            end(cr)

        def turtle():
            cr = Turtle(self.GetID(arr), column, row, column, row, self.size, self, "turtle")
            end(cr)

        def human():
            cr = Human(self.GetID(arr), column, row, column, row, self.size, self, "human")
            end(cr)

        def grass():
            cr = Grass(self.GetID(arr), column, row, column, row, self.size, self, "grass")
            end(cr)

        def guarana():
            cr = Guarana(self.GetID(arr), column, row, column, row, self.size, self, "guarana")
            end(cr)

        def hogweed():
            cr = Hogweed(self.GetID(arr), column, row, column, row, self.size, self, "hogweed")
            end(cr)

        def mlecz():
            cr = Mlecz(self.GetID(arr), column, row, column, row, self.size, self, "mlecz")
            end(cr)

        def wolfberry():
            cr = Wolfberry(self.GetID(arr), column, row, column, row, self.size, self, "wolfberry")
            end(cr)

        b = Button(master, command=human)
        b.config(text="Human", width="15", height="3")
        b.pack()

        b = Button(master, command=sheep)
        b.config(text = "Sheep", width="15", height="3")
        b.pack()

        b = Button(master, command=wolf)
        b.config(text="Wolf", width="15", height="3")
        b.pack()

        b = Button(master, command=antelope)
        b.config(text="Antelope", width="15", height="3")
        b.pack()

        b = Button(master, command=cybersheep)
        b.config(text="Cybersheep", width="15", height="3")
        b.pack()

        b = Button(master, command=fox)
        b.config(text="Fox", width="15", height="3")
        b.pack()

        b = Button(master, command=turtle)
        b.config(text="Turtle", width="15", height="3")
        b.pack()

        b = Button(master, command=grass)
        b.config(text="Grass", width="15", height="3")
        b.pack()

        b = Button(master, command=guarana)
        b.config(text="Guarana", width="15", height="3")
        b.pack()

        b = Button(master, command=hogweed)
        b.config(text="Hogweed", width="15", height="3")
        b.pack()

        b = Button(master, command=mlecz)
        b.config(text="Mlecz", width="15", height="3")
        b.pack()

        b = Button(master, command=wolfberry)
        b.config(text="Wolfberry", width="15", height="3")
        b.pack()

        master.mainloop()

        pass

    def on_key_press(self, symbol: int, modifiers: int):
        self.log = " "
        for i in range(len(self.creatures) - 1):
            if (i > (len(self.creatures) - 1)): i = len(self.creatures) - 1
            self.creatures[i].IncrLT()
            self.creatures[i].action(symbol)
        r = len(self.creatures) - 1
        for i in range(r):
            for j in range(r):
                if (i > (len(self.creatures) - 1)): i = len(self.creatures) - 1
                if (j > (len(self.creatures) - 1)): j = len(self.creatures) - 1
                if (self.creatures[i].GetX() == self.creatures[j].GetX()) and (self.creatures[i].GetY() == self.creatures[j].GetY()) and (self.creatures[i].GetID() != self.creatures[j].GetID()):
                    self.creatures[i].collision(self.creatures[j])
                    r = len(self.creatures) - 1
                    break
        if symbol == 115:
            sm = SaveManager(self.creatures, self.size, self.log, self.is_dead)
            sm.save()
        self.delta = True

        if symbol == 108:
            sm = SaveManager(self.creatures, self.size, self.log, self.is_dead)
            sm.load(self)


    def get_rf_coords(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        while (not self.IsCoordsFree(x, y)):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
        arr = [0, 0]
        arr[0] = x
        arr[1] = y
        return arr

    def IsCoordsFree(self, x, y):
        if self.grid[x][y] == 1:
            return False
        return True

    def GetID(self, arr):
        return random.randint(0,100) + random.randint(1,100) * arr[0] * arr[1];

    def get_nf_coords(self, xx, yy):
        x = xx + 1
        y = yy + 1
        it = 0
        while (not self.IsCoordsFree(x, y)):
            r = random.randint(1,8)
            if (r == 1): x = x + 1
            elif (r == 2): x = x - 1
            elif (r == 3): y = y - 1
            elif (r == 4): y = y + 1
            elif (r == 5):
                x = x - 1
                y = y - 1
            elif (r == 6):
                x = x - 1
                y = y + 1
            elif (r == 7):
                x = x + 1
                y = y - 1
            elif (r == 8):
                x = x + 1
                y = y + 1
            if ((x < 0) or (y < 0) or (x > self.size - 1) or (y > self.size - 1) or (it > self.size)):
                arr = [0, 0]
                arr[0] = -1
                arr[1] = -1
                return arr
            it = it + 1
        arr = [0, 0]
        arr[0] = x;
        arr[1] = y;
        return arr;

    def GetCrByCoords(self, x, y):
        for i in range(len(self.creatures) - 1):
            if ((self.creatures[i].GetX() == x) and (self.creatures[i].GetY() == y)):
                return self.creatures[i]
        return None

    def GetCSize(self): return len(self.creatures)

    def get_nft_coords(self, xx, yy, ttype, finder):
        nearest = [0, 0]
        path = 999
        for i in range(len(self.creatures) - 1):
            if (self.creatures[i].GetType() == ttype):
                p = max(self.creatures[i].GetX() - finder.GetX(), self.creatures[i].GetY() - finder.GetY())
                if (p < path): nearest[0] = self.creatures[i].GetX(); nearest[1] = self.creatures[i].GetY(); path = p
        if path != 999: return nearest
        else: return None

    def SetCRS(self, creatures): self.creatures = creatures
    def SetLog(self, log): self.log = log
    def SetSize(self, size): self.size = size
    def SetDead(self, dead): self.is_dead = False
