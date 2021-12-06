class QueueNode():
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def Enqueue(self, data):
        node = QueueNode(data, None)
        if self.head == None :
            self.head = node
            self.tail = node
        else :
            self.tail.setNext(node)
            self.tail = node
        self.length += 1

    def Dequeue(self):
        if self.head == None :
            return None
        else :
            result = self.head.getData()
            self.head = self.head.getNext()
            self.length -= 1
            return result
    
    def Length(self):
        return self.length


if __name__ == "__main__":
    q = Queue()

    q.Enqueue("Hello")
    q.Enqueue("World")

    while q.Lenght() != 0 :
        print(q.Dequeue())