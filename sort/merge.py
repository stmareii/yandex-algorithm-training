import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    read = list(map(int, sys.stdin.read().split()))
    n = read[0]
    a = read[1:1+n]
    m = read[1+n]
    b = read[1+n+1:1+n+1+m]

    i = 0
    j = 0
    res = []
    while i < n and j < m:   
        if a[i] <= b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    res.extend(a[i:])
    res.extend(b[j:])
    
    print(" ".join(map(str, res)))


if __name__ == '__main__':
    main()
