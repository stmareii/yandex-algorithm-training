import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    q = []
    while True:
        command = input()
        c = command.split()
        match c:
            case ['push', val]:
                q.append(val)
                print('ok')
            case ['pop']:
                if q:
                    print(q.pop(0))
                else:
                    print('error')

            case ['front']:
                if q:
                    print(q[0])
                else:
                    print('error')

            case ['size']:
                print(len(q))

            case ['clear']:
                q.clear()
                print('ok')
            
            case ['exit']:
                print("bye")
                break
            


if __name__ == '__main__':
    main()