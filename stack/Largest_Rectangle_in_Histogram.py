import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    s = list(map(int, input().split()))
    n = s[0]
    height = s[1:] #высоты слева направо
    height.append(0)
    width = 1
    stack = []
    res = [-1 for i in range(n)]
    area = 0

    for idx, v in enumerate(height):
        while stack and height[stack[-1]] > v:
            top = height[stack.pop()]
            #правая гр - i, левая - stack[-1] после pop
            left = stack[-1] if stack else -1
            right = idx
            w = (right-1) - (left + 1) + 1
            area = max(area, w * top)

            
        stack.append(idx)
    
    print(area)

if __name__ == '__main__':
    main()
