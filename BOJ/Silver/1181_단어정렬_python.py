def sort_word() :
    word = []
    answer = []
    len_max = 0

    # 단어 N개 입력받기
    N = int(input())
    for i in range(N) :
        word.append(str(input()))
    # print(word)

    # 중복된 단어 제거
    word = list(set(word))
    # print("set : ", word)
 
    # 1. 길이가 짧은 것부터 정렬
    # 키: 단어, 값: 단어 길이 -> dictionary 생성
    N = len(word)
    word.sort(key=len)
    # print(word)

    # 2. 길이가 같으면 사전 순으로 정렬
    # 같은 길이의 단어가 몇 개인지 체크 -> 가장 긴 단어의 길이만큼 0값을 가진 리스트 생성
    # index: 단어 길이, 값: 같은 길이의 단어 개수
    len_max = len(word[-1])
    # print(f"len_max: {len_max}")

    len_list = [0 for _ in range(len_max)]
    # print(len_list)

    for i in range(N) :
        index = len(word[i]) -1
        len_list[index] += 1
    # print(len_list)

    # 길이가 같은 단어들을 슬라이싱해서 정렬 후 새 리스트에 담기
    start_index = 0
    next_index = 0
    for i in range(len(len_list)) :
        if len_list[i] == 0 :
            pass
        elif len_list[i] == 1 :
            answer.append(word[start_index])
            start_index += 1
        elif len_list[i] > 1 :
            next_index = start_index + len_list[i]
            temp = word[start_index : next_index]
            # print(f"temp: {temp}")
            temp.sort()
            # print(f"sorted_temp : {temp}")
            answer[start_index : next_index] = temp[:]
            start_index = next_index
        # print(f"i: {i}, answer : {answer}, start_index: {start_index}")'''

    # 출력
    for word in answer :
        print(word)

    return ;

sort_word()