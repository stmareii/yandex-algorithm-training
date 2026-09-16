import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    heap = []

    n = int(input())
    for _ in range(n):
        c = input()
        command = c.split()
        match command:
            case ['0', val]:
                heap.append(int(val))
                ind = len(heap) - 1
                while (heap[ind] > heap[(ind-1) // 2] and (ind != 0)):
                    heap[ind], heap[(ind-1) // 2] = heap[(ind-1) // 2], heap[ind]
                    ind = (ind-1) // 2

            case ['1']:
                heap[-1], heap[0] = heap[0], heap[-1]
                print(heap.pop())

                if not heap:
                    continue
                ind = 0
                while True:
                    left = 2 * ind + 1
                    right = 2 * ind + 2
                    l = ind
                    if left < len(heap) and heap[left] > heap[l]:
                        l = left
                    if right < len(heap) and heap[right] > heap[l]:
                        l = right
                    if l != ind:
                        heap[ind], heap[l] = heap[l], heap[ind]
                        ind = l
                    else:
                        break
                

if __name__ == '__main__':
    main()
