
class Contact() :
    def __init__(self, name, number=""):
        self.name = name
        self.number = number

    def __eq__(self, other):
        if other == None: return False
        return self.name.lower() == other.name.lower()

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    def __str__(self):
        return "(" + self.name + ", " + self.number + ")"

