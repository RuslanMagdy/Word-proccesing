w = input()

W = kring.trans(w)

print(kring.otchet(W[0],W[1],W[2],W[3],W[4],W[5]))



L = list(map(int, input().split()))

print(kring.invr(L[0],L[1],L[2],L[3],L[4],L[5]))

print(kring.l(L[0],L[1],L[2],L[3],L[4],L[5]))

#print(sear.sertree(sear.neard(3,3,1,0,0,0),3,3,1,0,0,0))

for n in range(0,4):
  for m in range(0,n+1):
    for k in range(0,m+1):
      for T1 in range(-3,4):
        for T2 in range(-3,4):
          for T3 in range(-3,4):
            if kring.isdeadend(T1,T2,T3,k,m,n) == True:
              print(kring.otchet(T1,T2,T3,k,m,n))







L = list(map(int, input().split()))

L = kring.multi(L,[0,0,0,-1,0,0,0])

print(L)

print(kring.invr(L[0],L[1],L[2],L[3],L[4],L[5]))

print(kring.l(L[0],L[1],L[2],L[3],L[4],L[5]))



w = input()



W = kring.trans(w)

print(kring.otchet(W[0],W[1],W[2],W[3],W[4],W[5]))






L = list(map(int, input().split()))

L = kring.multi(L,[0,0,0,-1,0,0,0])

print(L)

print(kring.invr(L[0],L[1],L[2],L[3],L[4],L[5]))

print(kring.l(L[0],L[1],L[2],L[3],L[4],L[5]))



print(kring.otchet(0,6,3,1,2,2))







for a1 in Alf:
  for a2 in Alf:
    for a3 in Alf:
      for a4 in Alf:
        for a5 in Alf:
          for a6 in Alf:
            for a7 in Alf:
              i = i + 1
              print(i)
              ww = kring.trans(a1+a2+a3+a4+a5+a6+a7)
              if ww == [0,6,3,1,2,2]:
                print(a1+a2+a3+a4+a5+a6+a7)

















for n in range(0,4):
  for m in range(0,4):
    for k in range(0,4):
      for T1 in range(0,4):
        for T2 in range(0,4):
          for T3 in range(0,4):
            L = kring.otchet(T1,T2,T3,k,m,n)
            for i in range(2,8):
              if L[1] > L[i]+1:
                print(i)
                print(L)