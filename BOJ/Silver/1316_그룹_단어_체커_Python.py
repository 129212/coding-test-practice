def group_word_check() :
    word = []
    answer = 0

    N = int(input())
    for _ in range(N) :
        word.append(str(input()))
    
    for w in word :
        word_dict = {}
        c = w[0]
        answer += 1
        for j in w :
            if j in word_dict.keys() :
                answer -= 1
                break
            else :
                if c != j :
                    word_dict[c] = 1
                    c = j
    
    print(answer)
    
    return ;

group_word_check()