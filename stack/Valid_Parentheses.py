import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    a = input()
    dct = {")": "(", "}": "{", "]": "["} #если скобка в ключах то она закрывающая
    #потому что в стек только открывающие скобки идут

    stack = []
    for i in a: 
        if i not in dct:
            stack.append(i)
        else:
            if not stack or stack.pop() != dct[i]:
                print("no")
                return
    if not stack:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()