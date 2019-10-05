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
    if t is None or t.val == x:
        return t
    if x < t.val:
        return treeSearch(t.left, x)
    else:
        return treeSearch(t.right, x)

def treeParentSearch(t, x):
    if t is None or (t.right is not None and t.right.val == x) or (t.left is not None and t.left.val == x):
        return t
    if x < t.val:
        return treeParentSearch(t.left, x)
    else:
        return treeParentSearch(t.right, x)


def treeInsert(t,x):
    if t is None:
        return Node(x)
    if x < t.val:
        t.left = treeInsert(t.left, x)
        return t
    else:
        t.right = treeInsert(t.right, x)
        return t

def treeDeep(t):
    if t is None:
        return 0
    return 1 + max(treeDeep(t.right), treeDeep(t.left))

def treePrint(t):
    if t is None:
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
    if r.left is None and r.right is None:
        r.val = None
        return None
    elif r.left is None and r.right is not None:
        return r.right
    elif r.left is not None and r.right is None:
        return r.left
    else:
        s = r.right
        while s.left is not None:
            parent = s
            s = s.left
        r.val = s.val
        if s == r.right:
            r.right = s.right
        else:
            parent.left = s.right

        return r
         
if __name__ == "__main__":
    k = Node(30)
    li = [20,25,40,10,35]
    for i in li:
        treeInsert(k, i)

    print("=" * 50)
    treePrint(k)

    t  = treeSearch(k, 20)
    q = treeParentSearch(k,20)
    treeDelete(k, t, q)
    
    print("=" * 50)
    treePrint(k)
    
    t  = treeSearch(k, 30)
    q = treeParentSearch(k,30)
    treeDelete(k, t, q)
    
    print("=" * 50)
    treePrint(k)
