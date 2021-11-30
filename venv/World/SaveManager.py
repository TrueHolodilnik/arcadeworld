import xml.etree.cElementTree as ET
from time import gmtime, strftime
from tkinter import filedialog
from tkinter import *
from .Animals.Animal import Animal
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
from xml.dom import minidom

class SaveManager:

    def __init__(self, creatures, size, log, is_dead):
        self.creatures = creatures
        self.size = size
        self.log = log
        self.is_dead = is_dead

    def save(self):
        root = ET.Element("world")
        crs = ET.SubElement(root, "creatures")
        crs.set('amount', str(len(self.creatures)))
        crs.set('size', str(self.size))
        crs.set('log', str(self.log))
        crs.set('is_dead', str(self.is_dead))

        for i in range(len(self.creatures)):
            cr = ET.SubElement(crs, "c" + str(i))
            if self.creatures[i].GetType() == "human": cr.set('aturns', str(self.creatures[i].GetAT()))
            if isinstance(self.creatures[i], Animal): cr.set('mul', str(self.creatures[i].GetMul()))
            cr.set('power', str(self.creatures[i].GetPower()))
            cr.set('init', str(self.creatures[i].GetInit()))
            cr.set('id', str(self.creatures[i].GetID()))
            cr.set('x', str(self.creatures[i].GetX()))
            cr.set('y', str(self.creatures[i].GetY()))
            cr.set('prevx', str(self.creatures[i].GetPrevX()))
            cr.set('prevy', str(self.creatures[i].GetPrevY()))
            cr.set('wsize', str(self.creatures[i].GetWSize()))
            cr.set('ltime', str(self.creatures[i].GetLT()))
            cr.set('type', str(self.creatures[i].GetType()))

        mydata = ET.tostring(root).decode()
        myfile = open("savedgame_" + strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + "_.xml", "w")
        myfile.write(mydata)

    def load(self, world):
        rt = Tk()
        rt.filename = filedialog.askopenfilename(initialdir="C:/Users/Holodilnik/PycharmProjects/arcade_tutorial/", title="Select file", filetypes=(("save files", "*.xml"), ("all files", "*.*")))
        tree = minidom.parse(str(rt.filename))
        rt.destroy()

        w = tree.getElementsByTagName('world')
        crs = tree.getElementsByTagName('creatures')
        amount = int(crs[0].attributes['amount'].value)
        size = int(crs[0].attributes['size'].value)
        log = crs[0].attributes['log'].value
        is_dead = bool(crs[0].attributes['is_dead'].value)

        creatures = []
        for i in range(amount):
            cr = tree.getElementsByTagName("c" + str(i))
            if cr[0].attributes['type'].value == "human":
                c = Human(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "human")
                c.SetMul(int(cr[0].attributes['mul'].value))
                c.SetAT(int(cr[0].attributes['aturns'].value))
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "wolf":
                c = Wolf(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "wolf")
                c.SetMul(int(cr[0].attributes['mul'].value))
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "antelope":
                c = Antelope(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "antelope")
                c.SetMul(int(cr[0].attributes['mul'].value))
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "cybersheep":
                c = Cybersheep(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "cybersheep")
                c.SetMul(int(cr[0].attributes['mul'].value))
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "fox":
                c = Fox(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "fox")
                c.SetMul(int(cr[0].attributes['mul'].value))
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "sheep":
                c = Sheep(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "sheep")
                c.SetMul(int(cr[0].attributes['mul'].value))
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "turtle":
                c = Turtle(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "turtle")
                c.SetMul(int(cr[0].attributes['mul'].value))
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "grass":
                c = Grass(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "grass")
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "guarana":
                c = Guarana(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "guarana")
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "hogweed":
                c = Hogweed(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "hogweed")
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "mlecz":
                c = Mlecz(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "mlecz")
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)
            elif cr[0].attributes['type'].value == "wolfberry":
                c = Guarana(int(cr[0].attributes['id'].value), int(cr[0].attributes['x'].value), int(cr[0].attributes['y'].value), int(cr[0].attributes['prevx'].value), int(cr[0].attributes['prevy'].value), int(cr[0].attributes['wsize'].value), world, "wolfberry")
                c.SetLT(int(cr[0].attributes['ltime'].value))
                creatures.append(c)


        world.SetCRS(creatures)
        world.SetLog(log)
        world.SetSize(size)
        world.SetDead(is_dead)