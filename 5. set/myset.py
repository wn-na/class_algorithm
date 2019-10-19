class element:
    def __init__(self, x = None, near = None, front = None):
        self.key, self.next, self.front = x, near, front

class mySet:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def make_set(self, x):
        if self.head == None:
            self.head = element(x)
            self.head.front = self.head
            self.tail = self.head
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = element(x)
            tmp.next.front = self.head
            self.tail = tmp.next

    def find_set(self, x):
        tmp = self.head
        while tmp != None:
            if tmp.key == x:
                return True
            else:
                tmp = tmp.next
        return False

    def print(self):
        tmp = self.head
        print(f"head : {id(self.head)}, tail : {id(self.tail)}")
        while tmp != None:
            print(f"set key : {tmp.key}, address : {id(tmp)}, next : {id(tmp.next)}, front : {id(tmp.front)}")
            tmp = tmp.next

    def union(self, newset):
        tmp = newset.head
        while tmp != None:
            self.make_set(tmp.key)
            tmp = tmp.next           
