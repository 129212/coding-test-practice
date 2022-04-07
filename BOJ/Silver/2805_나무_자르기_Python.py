from sys import stdin

def cut_tree() :
    answer = []

    # 입력받기
    N, M = map(int, stdin.readline().split())
    tree = list(map(int, stdin.readline().split()))

    start = 0
    end = max(tree)
    while start <= end :
        remain = 0
        idx = start + ((end - start) // 2)
        for t in tree :
            if t - idx > 0 :
                remain += (t - idx)
        if remain >= M :
            answer.append(idx)
            start = idx + 1
        else : 
            end = idx - 1
    # print("-----")
    print(max(answer))

cut_tree()