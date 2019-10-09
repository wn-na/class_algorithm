import linearselect
import select
import random

def testSelect(random_max, arr_size_min, arr_size_max, select_func):
    try:
        random_case = [random.randint(0, random_max) for i in range(random.randint(arr_size_min, arr_size_max))]
        arr_size = len(random_case)
        Flag = False
        test = []

        for num in range(arr_size):
            test_case = random_case[:]
            test.append(select_func(test_case, 0, arr_size, num))
        random_case.sort()

        for num in range(arr_size):
            if random_case[num] != test[num]:
                Flag = True
                break

        print("== {0}.{1} function result ==".format(select_func.__module__, select_func.__name__))
        print("test case: random(0 to {0}), array size : {1}".format(random_max, arr_size))
        if Flag:
            print(">> !!! fail")
            return False
        else:
            print(">> Success")
            return True
    except:
        print(">> error")
        return False



if __name__ == '__main__':
    testSelect(3424, 10, 200, select.select)
    testSelect(4358, 10, 250, linearselect.select)
