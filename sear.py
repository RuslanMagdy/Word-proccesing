from kring import otchet,ws,l


def searw(T12,T13,T23,t3,t2,t1, w):
  if [T12,T13,T23,t3,t2,t1] == [0,0,0,0,0,0]:
    return w
  else: 
    Alf = ["a", "b", "c","A","B","C"]
    L = otchet(T12,T13,T23,t3,t2,t1)
    for i in range(2,8):
      if L[i]<L[1]:
        w = w + Alf[i-2]
        T = ws(Alf[i-2],T12,T13,T23,t3,t2,t1)
        return searw(T[0],T[1],T[2],T[3],T[4],T[5],w)




def neard(T12,T13,T23,t3,t2,t1):
  cur = []
  Alf = ["a", "b", "c","A","B","C"]
  LL = otchet(T12,T13,T23,t3,t2,t1)
  L = LL[1]
  for i in range(2,8):
    if LL[i]<L:
      cur = cur + [Alf[i-2]]
  return cur
  
def sertree(cur,T12,T13,T23,t3,t2,t1):
  L = [T12,T13,T23,t3,t2,t1]
  if L == [0,0,0,0,0,0]:
    return cur
  for i in range(len(cur)):
    Ll = ws(cur[i],T12,T13,T23,t3,t2,t1)

    cur[i] = [cur[i],neard(Ll[0],Ll[1],Ll[2],Ll[3],Ll[4],Ll[5])]

  return cur
    
    

  


