

import sys
from menu import Menu
    
if __name__ == "__main__":
    menu = Menu()
    for i in range(len(sys.argv)-1):
        menu.loadFile(sys.argv[i+1])
    menu.loop()
