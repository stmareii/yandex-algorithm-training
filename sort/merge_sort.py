import sys


def merge(l, r):
    i = 0
    j = 0
    res = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
    res.extend(l[i:])
    res.extend(r[j:])
    return(res)

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    return merge(left, right)


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    read = list(map(int, sys.stdin.read().split()))
    n = read[0]
    a = read[1:1+n]

    res = merge_sort(a)
    print(" ".join(map(str, res)))


if __name__ == '__main__':
    main()
