def recu_fibo(n):
    if n < 1:
        return 0
    elif n < 3:
        return 1
    else:
        return (recu_fibo(n - 1) + recu_fibo(n - 2))

def fibo_one(n):
    if n < 1:
        return 0
    elif n < 3:
        return 1
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


f = [0] * (20)
def fibo_two(n):
    if f[n] != 0:
        return f[n]
    else:
        if n == 1 or n == 2:
            f[n] = 1
        else:
            f[n] = fibo_two(n - 1) + fibo_two(n - 2)
        return f[n]
            


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, recu_fibo(i), fibo_one(i), fibo_two(i))
