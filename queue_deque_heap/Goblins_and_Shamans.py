import sys
from collections import deque

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    count = 0
    bdeq = deque()
    edeq = deque()


    while n > count:
        req = input()
        req = req.split()
        match req:
            case ['+', val]:
                edeq.append(val)
                count+=1
            case ['*', val]:
                edeq.appendleft(val)
                count+=1
            case ['-']:
                print(bdeq.popleft()) #номер гоблина который пошел (1 в очереди)
                count+=1

        if len(bdeq) < len(edeq):
            bdeq.append(edeq.popleft())
        elif len(bdeq) > len(edeq) + 1:
            edeq.appendleft(bdeq.pop())



if __name__ == '__main__':
    main()
