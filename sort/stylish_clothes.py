import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    read = list(map(int, sys.stdin.read().split()))
    n1 = read[0]
    n2 = read[1+n1]
    n3 = read[2+n1 + n2]
    n4 = read[3+n1 + n2 +n3]
    #в теории можно попробовать добавить обычный sorted:)
    s1 = sorted(read[1: 1+n1])
    s2 = sorted(read[1+n1+1: 1+n1+1+n2])
    s3 = sorted(read[1+n1+1+n2+1: 1+n1+1+n2+1+n3])
    s4 = sorted(read[1+n1+1+n2+1+n3+1: 1+n1+1+n2+1+n3+1+n4])

    i1, i2, i3, i4 = 0, 0, 0, 0
    res = []
    best_dif = 1000000000000

    while i1 < n1 and i2 < n2 and i3 < n3 and i4 < n4:
        c = [s1[i1], s2[i2], s3[i3], s4[i4]]
        cur_min = min(c)
        cur_max = max(c)
        cur_dif = cur_max - cur_min

        if cur_dif < best_dif:
            best_dif = cur_dif
            res = c[:]
        
        if cur_min == s1[i1]:
            i1 +=1
        elif cur_min == s2[i2]:
            i2+=1
        elif cur_min == s3[i3]:
            i3+=1
        elif cur_min == s4[i4]:
            i4+=1
            
    print(" ".join(map(str, res)))
    


if __name__ == '__main__':
    main()
