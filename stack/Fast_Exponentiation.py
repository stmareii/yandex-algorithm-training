import sys

def foo(a,n):
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / foo(a, -n)
    if n % 2 == 0:
        return foo(a*a, n // 2)
    else:
        return a * foo(a, n - 1)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    a = float(input())
    n = int(input())
    print(foo(a,n))

    #тут была проверка сложности алгоритма на обычных операциях
    # if n % 2 == 0:
    #     res = (a**2)**(n/2)
    # else:
    #     res = a * a**(n-1)
    # print(res)
    # print(a**n)




if __name__ == '__main__':
    main()
