from sys import stdin

def statistics_func() :
    number = []
    count_dict = {}

    N = int(stdin.readline())
    for _ in range(N) :
        number.append(int(stdin.readline()))
    
    # 산술평균
    avg = sum(number) / len(number)

    # 중앙값
    number.sort()
    mean = number[ len(number) // 2 ]

    # 최빈값
    # 최빈값이 여러 개 일 때는 최빈값 중 두 번째로 작은 값을 출력한다.
    if len(number) == 1 :
        mode = number[0]
    else :
        for i in range(len(number)) :
            idx = number[i]
            if idx not in count_dict.keys() :
                count_dict[idx] = 1
            else :
                count_dict[idx] += 1
        count_dict = sorted(count_dict.items(), key= lambda x: (x[1], -x[0]))
        if count_dict[-1][1] == count_dict[-2][1] :
            mode = count_dict[-2][0]
        else :
            mode = count_dict[-1][0]

    # 범위
    ran = max(number) - min(number)

    # print("------")
    print(round(avg))
    print(round(mean))
    print(mode)
    print(ran)

    return ;

statistics_func()