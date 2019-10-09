import selectionsort
import bubblesort
import insertionsort
import heapsort
import mergesort
import quicksort
import radixsort
import countingsort
import random
import newinsertionsort

def testSort(random_max, arr_size_min, arr_size_max, select_func, desc_sort = False):
    try:
        random_case = [random.randint(0, random_max) for i in range(random.randint(arr_size_min, arr_size_max))]
        arr_size = len(random_case)
        Flag = False
        test = []

        for num in range(arr_size):
            test = random_case[:]
            select_func(test, desc_sort)
        random_case.sort(reverse=desc_sort)

        for num in range(arr_size):
            if random_case[num] != test[num]:
                Flag = True
                break
        print("== {0}.{1} (Type : {2}) function result ==".format(select_func.__module__, select_func.__name__, "DESC" if desc_sort else "ASC"))
        print("test case: random(0 to {0}), array size : {1}".format(random_max, arr_size))
        #print(random_case)
        #print(test)
        if Flag:
            print(">> !!! fail")
            return False
        else:
            print(">> Success")
            return True
    except:
        print(">> error")
        return False


if __name__ == "__main__":
    # insertion sort
    testSort(1000,10,20,insertionsort.sort)
    testSort(1000,10,20,insertionsort.sort, True)

    # insertion sort by new array
    testSort(1000,10,20,newinsertionsort.sort)
    testSort(1000,10,20,newinsertionsort.sort, True)

    # bubble sort
    testSort(1000,10,20,bubblesort.sort)
    testSort(1000,10,20,bubblesort.sort, True)

    # selection sort
    testSort(1000,10,20,selectionsort.sort)
    testSort(1000,10,20,selectionsort.sort, True)

    # quick sort
    testSort(1000,10,20,quicksort.sort)
    testSort(1000,10,20,quicksort.sort, True)

    # merge sort
    testSort(1000,10,20,mergesort.sort)
    testSort(1000,10,20,mergesort.sort, True)

    # heap sort
    testSort(1000,10,20,heapsort.sort)
    testSort(1000,10,20,heapsort.sort, True)

    # counting sort
    testSort(780,10,20,countingsort.sort)
    testSort(780,10,20,countingsort.sort, True)

    # radix sort
    testSort(1000,10,20,radixsort.sort)
    testSort(1000,10,20,radixsort.sort, True)
