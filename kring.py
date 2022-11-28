import math


# 3 функции для перевода

def means(w):
  if w == 'a': return [0,0,0,0,0,1]
  if w == 'A': return [0,0,0,0,0,-1]
  if w == 'b': return [0,0,0,0,1,0]
  if w == 'B': return [0,0,0,0,-1,0]
  if w == 'c': return [0,0,0,1,0,0]
  if w == 'C': return [0,0,0,-1,0,0]
  if w == ' ': return [0,0,0,0,0,0]



def multi(l1,l2): # умножение нормальных форм
  return [l1[0] + l2[0] + l1[5]*l2[4], l1[1] + l2[1] + l1[5]*l2[3],l1[2] + l2[2] + l1[4]*l2[3], l1[3]+l2[3],l1[4]+l2[4],l1[5]+l2[5]]

def trans(w): #нормальная форма по строке
  ll = [0,0,0,0,0,0]
  for i in range(len(w)):
    ll = multi(ll,means(w[i]))
  return ll



def sym_invr(T12,T13,T23, t3,t2,t1): #инволюция из симметрий на Z^3
  if t1<0:
    return sym_invr(-T12, -T13,T23, t3,t2,-t1)
  elif t2<0:
    return sym_invr(-T12,T13,-T23, t3,-t2,t1)
  elif t3<0:
    return sym_invr(T12,-T13,-T23, -t3,t2,t1)
  else: 
    return [T12,T13,T23,t3,t2,t1]


def invr(T12,T13,T23, t3,t2,t1): #еще инволюции, чтобы прям все сделать неотрицательным
  [T12,T13,T23,t3,t2,t1] = sym_invr(T12,T13,T23, t3,t2,t1)
  if T12<0:
    return invr(t2*t1-T12,T13,T23, t3,t1,t2)
  elif T23<0:
    return invr(T12,T13,t3*t2-T23, t2,t3,t1)
  elif T13<0:
    return invr(T12,t3*t1-T13,T23, t1,t2,t3)
  else:
    return [T12,T13,T23,t3,t2,t1]

def sin(k):
  if k>=0: return 0
  else: return 1


def ll(T12,T13,T23,t3,t2,t1): #длина с подвохом

  L = sym_invr(T12,T13,T23,t3,t2,t1)

  [T12,T13,T23,t3,t2,t1] = L

  M = 2*(abs(T12)+abs(T13)+abs(T23)+abs(t1)+abs(t2)+abs(t3))
  m = 10000
  if (T12>=0 and T13>=0 and T23>=0):
    for a in range(M+3):
      for b in range(M+3):
        for c in range(M+3):
          if ((t1 + a)*(t2+b) >= T12) and ((t1 + a)*(t3+c)  >= T13) and ((t2 + b)*(t3+c)  >= T23):
            if a+b+c < m:
              m = a+b+c
              A = a
              B = b
              C = c
    return [t3+t2+t1+2*m, [A,B,C]]
  else: 
    for a in range(M+3):
      for b in range(M+3):
        for c in range(M+3):
          if ((t1 + a)*(t2+b) -t1*t2*sin(T12) >= abs(T12)) and ((t1 + a)*(t3+c) - t1*t3*sin(T13) >= abs(T13)) and ((t2 + b)*(t3+c) - t2*t3*sin(T23)  >= abs(T23)):
            if a+b+c < m:
              m = a+b+c
              A = a
              B = b
              C = c
    return [t3+t2+t1+2*m, [A,B,C]]

def l(T12,T13,T23,t3,t2,t1): #длина

  L = sym_invr(T12,T13,T23,t3,t2,t1)

  [T12,T13,T23,t3,t2,t1] = L

  M = 2*math.ceil(math.sqrt((abs(T12)+abs(T13)+abs(T23))))
  m = 10000
  if (T12>=0 and T13>=0 and T23>=0):
    for a in range(M+3):
      for b in range(M+3):
        for c in range(M+3):
          if ((t1 + a)*(t2+b) >= T12) and ((t1 + a)*(t3+c)  >= T13) and ((t2 + b)*(t3+c)  >= T23):
            if a+b+c < m:
              m = a+b+c
    return t3+t2+t1+2*m
  else: 
    for a in range(M+3):
      for b in range(M+3):
        for c in range(M+3):
          if ((t1 + a)*(t2+b) -t1*t2*sin(T12) >= abs(T12)) and ((t1 + a)*(t3+c) - t1*t3*sin(T13) >= abs(T13)) and ((t2 + b)*(t3+c) - t2*t3*sin(T23)  >= abs(T23)):
            if a+b+c < m:
              m = a+b+c
    return t3+t2+t1+2*m




#длина при умножении на образующие 

def wa(k1,k2,k3,t3,t2,t1): 
  L = multi([k1,k2,k3,t3,t2,t1],[0,0,0,0,0,1])
  return l(L[0],L[1],L[2],L[3],L[4],L[5])

def wb(k1,k2,k3,t3,t2,t1): 
  L = multi([k1,k2,k3,t3,t2,t1],[0,0,0,0,1,0])
  return l(L[0],L[1],L[2],L[3],L[4],L[5])

def wc(k1,k2,k3,t3,t2,t1):
  L = multi([k1,k2,k3,t3,t2,t1],[0,0,0,1,0,0])
  return l(L[0],L[1],L[2],L[3],L[4],L[5])

def wa1(k1,k2,k3,t3,t2,t1): 
  L = multi([k1,k2,k3,t3,t2,t1],[0,0,0,0,0,-1])
  return l(L[0],L[1],L[2],L[3],L[4],L[5])

def wb1(k1,k2,k3,t3,t2,t1): 
  L = multi([k1,k2,k3,t3,t2,t1],[0,0,0,0,-1,0])
  return l(L[0],L[1],L[2],L[3],L[4],L[5])

def wc1(k1,k2,k3,t3,t2,t1):
  L = multi([k1,k2,k3,t3,t2,t1],[0,0,0,-1,0,0])
  return l(L[0],L[1],L[2],L[3],L[4],L[5])

# Тоже умножение но без длины

def waa(k1,k2,k3,t3,t2,t1): 
  L = [k1,k2,k3,t3,t2,t1+1]
  return L

def wbb(k1,k2,k3,t3,t2,t1): 
  L = [k1+t1,k2,k3,t3,t2+1,t1]
  return L

def wcc(k1,k2,k3,t3,t2,t1):
  L = [k1,k2+t1,k3+t2,t3+1,t2,t1]
  return L

def waa1(k1,k2,k3,t3,t2,t1): 
  L = [k1,k2,k3,t3,t2,t1-1]
  return L

def wbb1(k1,k2,k3,t3,t2,t1): 
  L = [k1-t1,k2,k3,t3,t2-1,t1]
  return L

def wcc1(k1,k2,k3,t3,t2,t1):
  L = [k1,k2-t1,k3-t2,t3-1,t2,t1]
  return L

def ws(i,k1,k2,k3,t3,t2,t1):
  Alf = ["a", "b", "c","A","B","C"]
  if i == "a":
    return waa(k1,k2,k3,t3,t2,t1)
  if i == "b":
    return wbb(k1,k2,k3,t3,t2,t1)
  if i == "c":
    return wcc(k1,k2,k3,t3,t2,t1)
  if i == "A":
    return waa1(k1,k2,k3,t3,t2,t1)
  if i == "B":
    return wbb1(k1,k2,k3,t3,t2,t1)
  if i == "C":
    return wcc1(k1,k2,k3,t3,t2,t1)

def minv(w):
  w.upper()
  return w[::-1]

#окрестность точки радиуса 1

def otchet(T12,T13,T23,t3,t2,t1):
  return [[T12,T13,T23,t3,t2,t1], l(T12,T13,T23,t3,t2,t1), wa(T12,T13,T23,t3,t2,t1), wb(T12,T13,T23,t3,t2,t1), wc(T12,T13,T23,t3,t2,t1), wa1(T12,T13,T23,t3,t2,t1), wb1(T12,T13,T23,t3,t2,t1), wc1(T12,T13,T23,t3,t2,t1)]
    
