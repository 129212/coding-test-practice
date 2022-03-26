from sys import stdin

def queue() :
    queue = []
    start = 0
    end = 0

    # 입력과 동시에 작업하고 출력함
    N = int(stdin.readline())
    for _ in range(N) :
        c = stdin.readline().split()
        if c[0] == "push" : 
            queue.append(int(c[1]))
            end += 1
        elif c[0] == "pop" : 
            # pop(0)은 삭제 후 list의 인덱스를 옮기는 과정에서 O(n)의 시간이 걸린다.
            if start < end : 
                print(queue[start])
                start += 1
            else : print(-1)
        elif c[0] == "size" : 
            print(end - start)
        elif c[0] == "empty" :
            if start < end : print(0)
            else : print(1)
        elif c[0] == "front" : 
            if start < end : print(queue[start])
            else : print(-1)
        elif c[0] == "back" :
            if start < end : print(queue[end - 1])
            else : print(-1)

queue()