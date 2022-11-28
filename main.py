import kring

# все команды из библиотеки пишешь как  kring.function


  
w = input()

W = kring.trans(w)

print(kring.otchet(W[0],W[1],W[2],W[3],W[4],W[5]))


L = list(map(int, input().split()))

L = kring.multi(L,[0,0,0,-1,0,0,0])

print(L)

print(kring.invr(L[0],L[1],L[2],L[3],L[4],L[5]))

print(kring.l(L[0],L[1],L[2],L[3],L[4],L[5]))



print(kring.otchet(0,6,3,1,2,2))


