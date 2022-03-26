from sys import stdin

def card2() :
    card = []
    start = 0

    # 입력받기
    N = int(stdin.readline())
    card = [i for i in range(1, N +1)]

    end = N
    while (end - start) > 1 :   # 카드가 한 장 남으면 탈출
        start += 1
        if (end - start) > 1 : 
            card.append(card[start])
            start += 1
            end += 1
        else : 
            break

    print(card[start])

card2()