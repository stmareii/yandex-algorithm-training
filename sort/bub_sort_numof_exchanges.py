import sys


def merge(l, r):
    i = 0
    j = 0
    res = []
    count = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
            count += len(l) - i
    res.extend(l[i:])
    res.extend(r[j:])
    return(res, count)

def merge_sort(a):
    if len(a) <= 1:
        return a,0
    mid = len(a) // 2
    
    left, c_l = merge_sort(a[:mid])
    right, c_r = merge_sort(a[mid:])
    

    merged, count = merge(left, right)
    total_count = c_l + c_r + count
    return(merged, total_count)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    read = list(map(int, sys.stdin.read().split()))
    n = read[0]
    if n == 0:
        print(0)
        return

    a = read[1:1+n]
    res, count = merge_sort(a)
    print(count)

if __name__ == '__main__':
    main() 