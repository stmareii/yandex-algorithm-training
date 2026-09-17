import sys
import random

def partition(arr, l, r, x):
    while l <= r:
        while l <= r and arr[l] < x:
            l+=1
        while r>=0 and arr[r] >= x:
            r-=1
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
    return l, r



def quicksort(arr, l, r):
    if l >= r:
        return
    x = arr[random.randint(l,r)]
    
    left, right = partition(arr, l, r, x)
    
    
    quicksort(arr, l, right)
    quicksort(arr, left, r)



def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    read = sys.stdin.read().split()
    if not read:
        return
    
    n = int(read[0])

    if n == 0:
        print()
        return
    
    arr = [int(x) for x in read[1:n+1]]
    
    quicksort(arr, 0, n-1)

    print(*arr)


if __name__ == '__main__':
    main()