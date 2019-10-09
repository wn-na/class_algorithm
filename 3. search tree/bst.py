class node:
    def __init__(self, val = None):
        self.val = val
        self.right = self.left = None

    def __eq__(self, second):
        if second is None:
            return self.right == None and self.left == None and self.val == None
        return self.right == second.right and self.left == second.left and self.val == second.val
    
    def __str__(self):
        return str(self.val)

class node_bst:
    def __init__(self):
        self.head = node()
    
    def __str__(self):
        return str(self.val)

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            t = self.head
            while t != None:
                if val < t.val:
                    if t.left == None:
                        t.left = node(val)
                        break
                    t = t.left
                else:
                    if t.right == None:
                        t.right = node(val)
                        break
                    t = t.right
            
    def depth(self):
        return self.__treeDeep(self.head)
            
    def __treeDeep(self, t):
        if t == None:
            return 0
        return 1 + max(self.__treeDeep(t.right), self.__treeDeep(t.left))
    
    def print(self):
        t = self.head
        if t == None:
            print("No Node in BST")
            return
        val = []
        tree = [t]
        deep = self.depth()
        while tree:
            next_level = []
            for n in tree:
                if n == None:
                    continue
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

            val.append([str(n) for n in tree])
            tree = next_level
            
        for i in range(len(val)):
            print(val[i])

    def search(self, val):
        t = self.head
        if t.val == val:
            return t
        while t != None:
            if val < t.val:
                t = t.left
            elif val > t.val:
                t = t.right
            else:
                return t
        return None

    def __parentsearch(self, val):
        t = self.head
        if t.val == val:
            return None
        while t != None:
            if val < t.val:
                if t.left.val == val:
                    return t
                t = t.left
            elif val > t.val:
                if t.right.val == val:
                    return t
                t = t.right
        return None

    def delete(self, val):
        if self.search(val) == None:
            print(val)
            return None
        self.__treeDelete(self.search(val), self.__parentsearch(val))

    def __treeDelete(self, r, p):
        if r == self.head:
            self.head = self.__deleteNode(self.head)
        elif r == p.left:
            p.left = self.__deleteNode(r)
        else:
            p.right = self.__deleteNode(r)

    def __deleteNode(self, r):
        if r.left == None and r.right == None:
            r.val = None
            return None
        elif r.left == None and r.right != None:
            return r.right
        elif r.left != None and r.right == None:
            return r.left
        else:
            s = r.right
            while s.left != None:
                parent = s
                s = s.left
            r.val = s.val
            if s == r.right:
                r.right = s.right
            else:
                parent.left = s.right

            return r
