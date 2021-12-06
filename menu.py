from contact import Contact
import rw
from aatree import AATree

class Menu():
    def __init__(self):
        self.Tree = AATree()
        self.run = True

    def loadFile(self, filename = None):
        if filename == None:
            filename = input("File to load: ").strip()
        l = rw.readContactsFromFile(filename)
        for item in l:
            self.Tree.insert(item)

    def saveFile(self, filename = None):
        if filename == None:
            filename = input("File to save to: ").strip()
        l = self.Tree.getSortedList()
        rw.writeToFile(l, filename)

    def help(self, null = None):
        for item in self.menuItems():
            print(item[0])
    
    def clearTree(self, null = None):
        self.Tree = AATree()

    def insert(self, name = None):
        if name == None:
            name = input("Contact name: ").strip()
        number = input("number: ").strip()
        self.Tree.insert(Contact(name, number))

    def delete(self, name = None):
        if name == None:
            name = input("Contact name: ").strip()
        self.Tree.delete(Contact(name))

    def search(self, name = None):
        if name == None:
            name = input("Contact name: ").strip()
        s = self.Tree.search(Contact(name))
        if s == None:
            print("Could not find "+name+" in tree.")
        else:
            print(s.name + ": " + s.number)
    
    def print(self, null = None):
        self.Tree.print()
    
    def ltree(self, null = None):
        l = self.Tree.getSortedList()
        for item in l:
            print(item.name + " : " + item.number)

    def quit(self, null = None):
        self.run = False

    def menuItems(self):
        return [("insert", self.insert),
        ("update", self.insert),
        ("delete", self.delete),
        ("remove", self.delete),
        ("search", self.search),
        ("find", self.search),
        ("load", self.loadFile),
        ("save", self.saveFile),
        ("print", self.print),
        ("list", self.ltree),
        ("clear", self.clearTree),
        ("quit", self.quit),
        ("exit", self.quit),
        ("help", self.help), ]

    def show(self):
        c = input("\033[1;31;40m$\033[0m ").lower().strip()
        ap = c.find(" ")
        arg = c[ap:].strip() if ap != -1 else None
        c = c[:ap] if ap != -1 else c
        for item in self.menuItems():
            if c == item[0]:
                item[1](arg)
                return

    def loop(self):
        while self.run:
            self.show()

if __name__ == "__main__":
    menu = Menu()
    menu.loop()