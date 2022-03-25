from sys import stdin

def dungchi() :
    dungchi = []

    # 입력받기
    N = int(stdin.readline().split()[0])
    for i in range(N) :
        dungchi.append(list(map(int, stdin.readline().split())))
    print(dungchi)

    # 몸무게와 키 둘 다 큰 사람이 없다면 1등, 있다면 그 수만큼 + 1
    # dungchi 원소들의 마지막에 등수를 추가한다.
    for i in range(len(dungchi)) :
        rank = 1
        for j in range(len(dungchi)) :
            if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1] :    # 덩치가 큰 경우
                rank += 1
        dungchi[i].append(rank)
    print(dungchi)
    
    # 덩치등수(dungchi[2]) 출력하기
    for dc in dungchi :
        print(dc[2], end=' ')

dungchi()