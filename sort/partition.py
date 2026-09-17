import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    read = sys.stdin.read().split()
    n = int(read[0])

    if n == 0:
        print(0)
        print(0)
        return
    x = int(read[n+1])
    
    count = 0
    for i in range(1, n+1):
        if int(read[i]) < x:
            count += 1
    
    res = n - count
    print(count)
    print(res)


if __name__ == '__main__':
    main()