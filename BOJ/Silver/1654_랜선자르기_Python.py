from sys import stdin

# K 개의 랜선을 N 개로 만들기
def cut_lancable() :
    lancable = []
    answer = []

    # 입력받기
    K, N = map(int, stdin.readline().split())
    for _ in range(K) :
        lancable.append(int(stdin.readline().split()[0]))  # split() 은 리스트로 반환

    # 11개를 만들 수 있는 최댓값부터 시작한다
    max_len = sum(lancable) // N

    start = 1
    end = max_len
    while start <= end :               # K 가 N 개가 될 때까지 이진탐색
        K = 0
        idx = start + ((end - start) // 2)
        for lan in lancable :
            K += (lan // idx)
        if K >= N : 
            answer.append(idx)
            start = idx + 1
        elif K < N : end = idx - 1
    # print("-----")
    print(max(answer))

cut_lancable()