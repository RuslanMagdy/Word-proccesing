from Tree_new import Tree

import math


def l(k, m, n):
    x = 4 * abs(k) + abs(n) + abs(m)
    for s in range(0, abs(k) + 5):
        for t in range(0, abs(k) + 5):
            if ((k * n * m <= 0 and s + t < x and (s + abs(n)) * (t + abs(m)) - abs(n) * abs(m) >= abs(k)) or (k * n * m >= 0 and s + t < x and (s + abs(n)) * (t + abs(m)) >= abs(k))):
                x = s + t

    return (abs(n) + abs(m) + 2 * x)


def wa(k, m, n):
    return l(k, m, n + 1)


def wb(k, m, n):
    return l(k + n, m + 1, n)


def wa1(k, m, n):
    return l(k, m, n - 1)


def wb1(k, m, n):
    return l(k - n, m - 1, n)


def ws1(k, m, n):
    q = []
    if wa(k, m, n) < l(k, m, n):
        q.append([k, m, n + 1])
    if wb(k, m, n) < l(k, m, n):
        q.append([k + n, m + 1, n])
    if wa1(k, m, n) < l(k, m, n):
        q.append([k, m, n - 1])
    if wb1(k, m, n) < l(k, m, n):
        q.append([k - n, m - 1, n])
    return q


def ws(k, m, n):
    q = 0
    if wa(k, m, n) < l(k, m, n):
        q = q + 1
    if wb(k, m, n) < l(k, m, n):
        q = q + 1
    if wa1(k, m, n) < l(k, m, n):
        q = q + 1
    if wb1(k, m, n) < l(k, m, n):
        q = q + 1
    return q

def make(a, b, c, fun, full_tree) -> None:
  t = Tree(None, a, b, c,full_tree)
  toVis = [] # type: list(Tree)

  toVis.append(t)

  while toVis != []:
    current = toVis.pop(0)

    if isinstance(current, Tree):
      if (current.has_sons(full_tree) is False) and (current.a != 0 or current.b != 0 or current.c != 0):
        for i in fun(current.a, current.b, current.c):
          New = Tree(current, i[0], i[1], i[2], full_tree)

          toVis.append(New) 
  full_tree.append(toVis)
  return full_tree
    
  



def print_tree(full_tree: list):
    for tree in full_tree:
        print(tree.__str__())
        print("\n")
    print("\n")


def thr(h):
  x = 0
  for k in range(-4*h +2, 4*h+3):
    for m in range(-h-2,h+2):
      for n in range(-h-2,h+2):
        if l(k,m,n)==h:
          t = make(k, m, n, ws1,[])
          x = x + len(Tree.get_sons_from_depth(h,t))
          t = []
  return x

def com(k):
  for h in range(19, 19 + k+1):
    t = make(h, 0, 0, ws1,[])
    print( len(Tree.get_sons_from_depth(l(h,0,0),t)),"amount of geowords for pow of commutator:",h)
    t = []

def com1(k):
    t = []
    t = make(k, 0, 0, ws1,[])
    return len(Tree.get_sons_from_depth(l(k,0,0),t))

def com2(k,j):
    t = []
    t = make(k, 0, 0, ws1,[])
    return Tree.get_sons_from_depth(j,t)

def com3(k,m,n):
    t = []
    t = make(k, m, n, ws1,[])
    return Tree.get_sons_from_depth(l(k,m,n),t)



commm = [1,4,12,48,8,80,20,264,72,12,420,112,28,1088,352,96,16,1584,540,144,44,1912,1360,440,120,20,2748,1936,660,176,44]

gammal = [1, 4, 12, 36, 104, 260, 624, 1332, 2684, 5284, 10064, 18724, 34140, 62420]

gamma = [1, 4, 12, 36, 100, 260, 612, 1332, 2628, 5284, 9964, 18724, 33892, 62420, 112940, 207548, 379124, 706020, 1321068, 2508132, 4792012, 9269588]

f = [0, 4, 6, 8, 8, 10, 10, 12, 12, 12, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 20, 20, 20, 20, 20, 22, 22, 22, 22,22]

wwwww = [0.25, 0.333, 0.3333, 0.36, 0.384615, 0.42483660, 0.459, 0.50684931, 0.497350492, 0.5303091, 0.5321512, 0.552460757, 0.5429669977, 0.55268284, 0.54416327, 0.54744094, 0.5369876, 0.534, 0.526,0.523]


for k in range(-5,0):
  print([k,-1,1], l(k,-1,1), wa(k,-1,1), wb(k,-1,1), wa1(k,-1,1),wb1(k,-1,1))



























  