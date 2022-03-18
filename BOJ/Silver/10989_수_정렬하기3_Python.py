from sys import stdin

def number_sort3() :
    number = []

    N = int(stdin.readline())
    for _ in range(N) :
        number.append(int(stdin.readline()))
    
    number.sort()

    print("------")
    for n in number :
        print(n)

number_sort3()