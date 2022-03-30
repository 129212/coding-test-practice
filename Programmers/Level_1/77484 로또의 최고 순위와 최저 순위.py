def solution(lottos, win_nums):
    answer = []
    zero_cnt = 0
    cnt = 0
    degree = 7
    
    for i in lottos :
        if i == 0 :
            zero_cnt += 1
        else :
            for j in win_nums :
                if i == j :
                    cnt += 1

    for i in range(2) :
        if i == 0 :
            if zero_cnt + cnt <= 1 :
                answer.insert(0, 6)
            elif zero_cnt + cnt > 1 :
                answer.insert(0, degree - (zero_cnt + cnt) )
        if i == 1 :
            if cnt <= 1 :
                answer.insert(1, 6)
            elif cnt > 1 :
                answer.insert(1, degree - (cnt))
    
    return answer