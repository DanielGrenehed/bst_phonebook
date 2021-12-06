
from contact import Contact
import os

def writeToFile(l, filename):
    with open(filename, 'w') as file:
        for contact in l:
            file.write(contact.name + "\n" + contact.number + "\n\n")


def readContactsFromFile(filename):
    contacts = []
    with open(filename, 'r') as file:
        ret = file.tell()
        file.seek(0, os.SEEK_END)
        eof = file.tell()
        file.seek(ret, os.SEEK_SET)
        while file.tell() != eof:
            name = file.readline().strip()
            if name :
                number = file.readline().strip()
                contacts.append(Contact(name, number))
    return contacts