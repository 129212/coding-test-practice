def Josephus () :
  N, K = map(int, input().split())
  here = K - 1  # current index
  answer = []

  que = list(range(1, N +1))

  while que :
    if len(que) == 1 :
      answer.append(que[0])
      break
    answer.append(str(que.pop(here)))
    here -= 1
    here += K
    while (here >= len(que)) :
          here -= len(que)

  print("<", end="")
  for a in answer :
    if a != answer[-1] :
      print(a, end=", ")
    else :
      print(a, end="")
  print(">")

Josephus()