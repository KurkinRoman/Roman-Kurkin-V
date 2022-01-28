def func():         #Задача №3
    a = int(input())
    b = int(input())
    if a % 2 == 0:
        a -= 1
    if b % 2:
        b -= 1
    for i in range(a, b, -2):
        print(i)
func()

def func_fib():     #Задача №9
    fib1 = fib2 = 1
    n = int(input())
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
func_fib()