N, K = map(int, input().split())
here = K -1  # current index
answer = []

que = list(range(1, N +1))
print(f"que -> {que}")

# for i in range(N) : Index Error -> out of index
while( len(que) != 0 ) :
  answer.append(que[here])
  que.pop(here)
  here -= 1
  print(f"here : {here}")
  print(f"answer -> {answer}")
  print(f"que -> {que}")
  if here < 0 :
    answer.append(que[0])
    break
  elif K > len(que) :
    here = ( K - len(que) ) -1
  elif (here + K) > len(que) :
    here = ( (here) + (K) ) - len(que)
  else :
    here += K 

print("<", end='')
for i in answer :
      print(i, end=', ')
print("\b\b>")