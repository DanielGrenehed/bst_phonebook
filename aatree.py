from gqueue import Queue

# Implementation of an ArneAnderssonTree
# https://en.wikipedia.org/wiki/AA_tree

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 1
    
    def isLeaf(self):
        return self.left == None and self.right == None


def skew(T):
    if T == None: return None
    elif T.left == None: return T
    elif T.left.level == T.level:
        L = T.left
        T.left = L.right
        L.right = T
        return L
    else:
        return T

def split(T):
    if T == None: return None
    elif T.right == None or T.right.right == None: 
        return T
    elif T.level == T.right.right.level:
        R = T.right
        T.right = R.left
        R.left = T
        R.level += 1
        return R
    else: 
        return T

def insert(data, T):
    if T == None:
        return Node(data)
    elif data < T.data:
        T.left = insert(data, T.left)
    elif data > T.data:
        T.right = insert(data, T.right)
    elif T.data == data:
        T.data = data
    T = skew(T)
    T = split(T)
    return T

def delete(data, T):
    if T == None:
        return T
    elif data > T.data :
        T.right = delete(data, T.right)
    elif data < T.data :
        T.left = delete(data, T.left)
    else:
        if T.isLeaf(): return None
        elif T.left == None:
            L = successor(T)
            T.right = delete(L.data, T.right)
            T.data = L.data
        else:
            L = predecessor(T)
            T.left = delete(L.data, T.left)
            T.data = L.data
    T = levelDown(T)
    T = skew(T)
    T.right = skew(T.right)
    if T.right != None:
        T.right.right = skew(T.right.right)
    T = split(T)
    T.right = split(T.right)
    return T

def levelDown(T):
    llevel = T.left.level if T.left != None else T.level
    rlevel = T.right.level if T.right != None else T.level
    tobe = min(llevel, rlevel) + 1
    if tobe < T.level :
        T.level = tobe
        if tobe < T.right.level:
            T.right.level = tobe
    return T

def successor(T):
    if T.right != None:
        suc = T.right
        while suc.left != None:
            suc = suc.left
        return suc
    return None

def predecessor(T):
    if T.left != None:
        pred = T.left
        while pred.right != None:
            pred = pred.right
        return pred

def search(data, T):
    if T == None:
        return None
    elif data < T.data:
        return search(data, T.left)
    elif data > T.data:
        return search(data, T.right)
    else:
        return T.data

def addToList(l, T):
    if T == None:
        return l
    if T.left != None:
        l = addToList(l, T.left)
    l.append(T.data)
    if T.right != None:
        l = addToList(l, T.right)
    return l


class AATree():
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None

    def insert(self, data):
        self.root = insert(data, self.root)

    def print(self):
        q = Queue()
        q.Enqueue(self.root)
        q.Enqueue(None)
        out = ""
        while q.Length() != 0:
            n = q.Dequeue()
            if n != None :
                out += str(n.data) + " "
                if n.left != None:
                    q.Enqueue(n.left)
                if n.right != None:
                    q.Enqueue(n.right)
            else:
                if q.Length() == 0 :
                    break
                out += "\n"
                q.Enqueue(None)
        print(out)

    def delete(self, data):
        self.root = delete(data, self.root)

    def search(self, data):
        return search(data, self.root)

    def getSortedList(self):
        l = []
        return addToList(l, self.root)


if __name__ == "__main__":
    T = AATree()
    arr = [2, 4, 1, 5, 3, 50, 20, 0, -1, 43, -3, 42, 12, 41, -23, 34, -12, -52]
    for i in arr : T.insert(i)
    T.print()

    T.delete(1)
    T.print()
    print(T.search(20))
    print(T.getSortedList())
