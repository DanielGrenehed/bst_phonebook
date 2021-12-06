import re

class Contact() :
    def __init__(self, name, number=""):
        self.name = name
        self.number = number
        if not self.isValid():
            self.validateNumber()

    def __eq__(self, other):
        if other == None: return False
        return self.name.lower() == other.name.lower()

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    def __str__(self):
        return "(" + self.name + ", " + self.number + ")"

    def isValid(self):
        res = re.search("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$", self.number)
        return res != None

    def validateNumber(self):
        res = ""
        found = re.findall("[0-9 ()+.-]", self.number)
        for s in found:
            res += s
        self.number = res

if __name__ == "__main__" :
    c = Contact("test", "v+12 +4a3.2 4-12")
    print(c)
    print(c.isValid())