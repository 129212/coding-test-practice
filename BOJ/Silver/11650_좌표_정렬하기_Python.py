from sys import stdin

def sort_coordinate() :
    coordinate= []
    N = int(stdin.readline())

    for _ in range(N) :
        temp = list(stdin.readline().split())
        coordinate.append(temp)
    coordinate.sort(key= lambda x: (x[0], x[1]))
    # print("-----")
    for coor in coordinate :
        print(coor[0], coor[1], sep=' ')

sort_coordinate()