import hashtable
import random


def testhash(data, hashtype = None):
    h = hashtable.hashtable()
    if hashtype is not None:
        h.opentype = hashtype

    for i in data:
        h.insert(i, random.randint(0, 100))

    print("=" * 30)
    for i in h:
        print(i)
    print("=" * 30)
    print(h.search(data[3]))
    print(h.search(200))
    
    print(h[data[7]])
    h[101] = 45
    print(h[1])
    print(h.search(101))
    
    print("=" * 30)
    print(h.delete(data[3]))
    print(h.delete(200))
    
    print("=" * 30)
    h.print()
    print("=" * 30)

def testchainhash(data):
    h = hashtable.hashtable()
    
    for i in data:
        h.chainedinsert(i, random.randint(0, 100))
        
    print("=" * 30)
    for i in h:
        print(i)
    print("=" * 30)
    print(h.chainedsearch(data[3]))
    print(h.chainedsearch(200))

    print(h[data[7]])
    h[101] = 4
    print(h[data[7]])
    print(h.chainedsearch(101))
    print("=" * 30)
    print(h.chaineddelete(data[3]))
    print(h.chaineddelete(200))
    
    print("=" * 30)
    h.print()
    print("=" * 30)

if __name__ == "__main__":
    data = list(set([random.randint(0,100) for i in range(12)]))
    print("======= hashtable.LINEAR =======")
    testhash(data)
    print("======= hashtable.DOUBLE =======")
    testhash(data, hashtable.OPENTYPE.DOUBLE)
    print("======= hashtable.QUADRATIC =======")
    testhash(data, hashtable.OPENTYPE.QUADRATIC)
    data = [random.randint(0,100) for i in range(20)]
    print("======= chainhashtable =======")
    testchainhash(data)
