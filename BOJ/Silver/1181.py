def sort_word(N) :
    input_word = []
    word_dict = {}
    answer = []
    len_max = 0

    for i in range(N) :
        input_word.append(str(input()))
    print(input_word)

    input_word = list(set(input_word))
    print("set : ", input_word)
 
    N = len(input_word)
    for i in range(N) :
        word_dict[i] = len(input_word[i])
    print(word_dict)

    word_dict = list(sorted(word_dict.items(), key= lambda x: x[1]))
    print(word_dict)

    len_max = word_dict[-1][1]
    print(f"len_max: {len_max}")

    len_count = [0 for _ in range(len_max)]
    print(len_count)

    for i in range(N) :

        index = word_dict[i][0]
        answer.append(input_word[index])

    

    return answer

N = int(input())
print(sort_word(N))
