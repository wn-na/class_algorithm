import myset

if __name__ == "__main__":
    set1 = myset.mySet()
    set1.make_set('a')
    set1.make_set('b')
    set1.make_set('c')
    
    set2 = myset.mySet()
    set2.make_set('d')
    set2.make_set('e')
    set2.make_set('f')
    set2.make_set('g')
    set2.make_set('h')

    set1.print()
    set2.print()
    print(set1.find_set('c'))
    print(set1.find_set('e'))

    set2.union(set1)
    set2.print()
