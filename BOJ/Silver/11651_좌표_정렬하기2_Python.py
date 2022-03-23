from sys import stdin

def sort_coordinate2() :
    coordinate = []

    # 입력받기
    N = int(stdin.readline())
    for _ in range(N) :
        coordinate.append(list(map(int, stdin.readline().split())))

    coordinate.sort(key= lambda x: (x[1], x[0]))
    
    for coor in coordinate :
        print(coor[0], coor[1], sep=' ')

sort_coordinate2()