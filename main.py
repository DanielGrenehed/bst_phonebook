from binarysearchtree import BinarySearchTree
from contact import Contact
    
if __name__ == "__main__":
    btr = BinarySearchTree(Contact("daniel", "2411"))
    btr.insert(Contact("joel", "14513"))
    btr.insert(Contact("andrea", "3401"))
    print()
    btr.print()
    
    btr.insert(Contact("daniel", "0704203371"))
    btr.insert(Contact("bert", "423"))
    print()
    btr.print()
    print()
    btr.printWithStructure()

