from queue import Queue


class BinarySearchTree() :
    def __init__(self, data, parent = None):
        self.left = None
        self.right = None
        self.height = 1
        self.parent = parent
        self.data = data
        
    def insert(self, data):
        if data == self.data:
            self.data = data
            return
        if data > self.data :
            if self.right == None :
                self.right = BinarySearchTree(data, self)
            else :
                self.right.insert(data)
        else :
            if self.left == None :
                self.left = BinarySearchTree(data, self)
            else :
                self.left.insert(data)

    def delete(self, node):
        pass

    def print(self):
        if self.left != None :
            self.left.print()
        print(self.data)
        if self.right != None :
            self.right.print()

    def printWithStructure(self):
        q = Queue()
        q.Enqueue(self)
        q.Enqueue(None)
        out = ""
        while True :
            curr = q.Dequeue()
            if curr != None :
                out += str(curr.data) + " "
                if curr.left != None :
                    q.Enqueue(curr.left)
                if curr.right != None :
                    q.Enqueue(curr.right)
            else :
                out += "\n"
                if q.Lenght() == 0 :
                    break
                q.Enqueue(None)
        print(out)

    def search(self, data):
        if data == self.data :
            return self.data
        if data < self.data :
            if self.left == None :
                return None
            return self.left.search(data)
        else :
            if self.right == None :
                return None
            return self.right.search(data)


    def heightAndBalance(self):
        lbalance = True
        lheight = -1 
        if self.left != None :
            lheight, lbalance = self.left.heightAndBalance()
        if not lbalance:
            return lheight, lbalance

        rbalance = True
        rheight = -1
        if self.right != None : 
            rheight, rbalance = self.right.heightAndBalance()

        height = max(lheight, rheight)
        balance = abs(lheight - rheight)
        if rbalance :
            return height, balance
        return height, False
        

if __name__ == "__main__":
    pass

