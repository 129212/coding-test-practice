from sys import stdin

def Coordinate_compression() :
    coordinate = []
    coor_dict = {}

    N = int(stdin.readline())
    coordinate = list(map(int, stdin.readline().split()))
    print(coordinate)

    temp = coordinate
    print(f"temp : {temp}")

    coordinate = list(set(coordinate))
    coordinate.sort()
    print(coordinate)
    for i, coor in enumerate(coordinate) :
        coor_dict[coor] = i
    print(coor_dict)
    
    for t in temp :
        print(coor_dict[t], end=' ')

Coordinate_compression()