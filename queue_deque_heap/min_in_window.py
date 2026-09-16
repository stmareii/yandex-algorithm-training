import sys
from collections import deque

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    deq_min = deque()  

    for i in range(n):
        x = arr[i]

        while deq_min and deq_min[-1] > x:  # было 3 -> пришла 2 и убрала 3. 
            deq_min.pop()

        deq_min.append(x)
        if i < k -1:
            continue
    
        print(deq_min[0])
        #левая граница i-k + 1
        y = arr[i - k + 1]
        if y == deq_min[0]:
            deq_min.popleft()

      


if __name__ == '__main__':
    main()
