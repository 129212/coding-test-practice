def solution(progresses, speeds):
    answer = []
    start = 0
    for i in range(start, len(progresses)) :
        while (progresses[i] < 100) :
            for j in range(start, len(progresses)) :
                progresses[j] += speeds[j]
        baepo = 0
        while (start < len(progresses)) and (progresses[start] >= 100) :
            baepo += 1
            start += 1
        if (0 < baepo) :
            answer.append(baepo)
    return answer