import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    s = input()
    tokens = s.split()
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b
    }
    temp = 0
    operand1 = 0
    operand2 = 0

    for i in tokens:
        if i not in ops:
            stack.append(i)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            temp = ops[i](int(operand1), int(operand2))
            stack.append(temp)
    
    print(stack[0])


if __name__ == '__main__':
    main()
