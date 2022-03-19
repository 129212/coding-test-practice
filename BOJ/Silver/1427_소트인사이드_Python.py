from sys import stdin

def sort_inside() :
    number = []
    N = int(stdin.readline())
    
    while N > 0 :
        temp = N % 10
        N //= 10
        number.append(temp)
    number.sort(reverse=True)
    for n in number :
        print(n, end='')

sort_inside()