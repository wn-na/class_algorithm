import bst
import random

if __name__ == "__main__":
    k = bst.node_bst()
    numlist = [i for i in range(300)]
    random.shuffle(numlist)
    li = numlist[:50]
    for i in li:
        k.insert(i)

    print("=" * 50)
    k.print()

    print("=" * 50)
    print(k.depth())

    for i in li:
        k.delete(i)
        
    print("=" * 50)
    k.print()
    
    random.shuffle(li)
    for i in li:
        k.insert(i)
        
    print("=" * 50)
    k.print()

    print("=" * 50)
    q = k.search(li[4])
    print(q, q.left, q.right)
