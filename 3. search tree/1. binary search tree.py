class Node:
    def __init__(self, val = None):
        self.val = val
        self.right = self.left = None

    def __eq__(self, second):
        if second is None:
            return self.right == None and self.left == None and self.val == None
        return self.right == second.right and self.left == second.left and self.val == second.val
    
    def __str__(self):
        return str(self.val)
    
def treeSearch(t, x):
    if t == None or t.val == x:
        return t
    if x < t.val:
        return treeSearch(t.left, x)
    else:
        return treeSearch(t.right, x)

def treeParentSearch(t, x):
    if t == None or (t.right != None and t.right.val == x) or (t.left != None and t.left.val == x):
        return t
    if x < t.val:
        return treeParentSearch(t.left, x)
    else:
        return treeParentSearch(t.right, x)


def treeInsert(t,x):
    if t == None:
        if hasattr(t, 'val'):
            t.val = x
            return t
        return Node(x)
    if x < t.val:
        t.left = treeInsert(t.left, x)
        return t
    else:
        t.right = treeInsert(t.right, x)
        return t

def treeDeep(t):
    if t == None:
        return 0
    return 1 + max(treeDeep(t.right), treeDeep(t.left))

def treePrint(t):
    if t == None:
        return
    val = []
    tree = [t]
    deep = treeDeep(t)
    while tree:
        val.append([str(n) for n in tree])
        next_level = []
        for n in tree:
            if n == None:
                continue
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        tree = next_level
        
    for i in val:
        print(i)

def treeDelete(t, r, p):
    if r == t:
        t = deleteNode(t)
    elif r == p.left:
        p.left = deleteNode(r)
    else:
        p.right = deleteNode(r)

def deleteNode(r):
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
         
# do not use command 'is', use '=='
if __name__ == "__main__":
    k = Node() # why if k = None and try Insert => return None
    li = [30, 20,25,40,10,35]
    for i in li:
        treeInsert(k, i)

    print("=" * 50)
    treePrint(k)

    li = [20,25,40,30,10,35]
    for i in li:
        t  = treeSearch(k, i)
        q = treeParentSearch(k, i)
        treeDelete(k, t, q)
    
        print("=" * 50)
        treePrint(k)
        
    print("=" * 50)
    if k == None:
        print("공백")
    else:
        treePrint(k)
