import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    s = input()
    cities = list(map(int, s.split()))
    stack = []
    ans = [-1 for _ in range(n)]
    for idx, v in enumerate(cities):
        while stack and cities[stack[-1]] > v:
            popped_idx = stack.pop()
            ans[popped_idx] = idx

        stack.append(idx)
    print(' '.join(map(str,ans)))

if __name__ == '__main__':
    main()
