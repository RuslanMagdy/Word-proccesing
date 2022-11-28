def recur_word(v):
    n = len(v)

    l = [v]

    for i in range(1, n):
        l.append(v[i:] + v[:i])

    return l


def check_power(w, k):
    n = len(w)

    if n % k == 0:
        v = ''
        for i in range(k):
            v = v + w[:(n // k)]
        if w == v:
            return True
    else:
        return False


def total_power(w):
    n = len(w)

    if n == 1:
        return [False, 0, 0]

    if n == 2:
        if w[0] == w[1]:
            return [True, 2, w[0]]

    for i in range(2, n // 2 + 2):
        if check_power(w, i):
            return [True, i, w[:(n // i)]]
    return [False, 0, 0]


def forward_acces(s):
    if s == 't' or s == 'T':
        return ['z', 'Z']
    if s == 'z' or s == 'Z':
        return ['t', 'T']


def check_incl(v, w):
    n = len(w)
    m = len(v)

    for i in range(n - m + 1):
        if v == w[i:i + m]:
            return True
    return False


def cons(l, n):
    if n == 1:
        return l
    M = len(l[0])
    ll = []
    for i in l:
        for s in forward_acces(i[M - 1]):
            w = i + s
            ll.append(w)
    return cons(ll, n - 1)


def balanced_res(n):
    if n % 3 == 2:
        return -1
    else:
        return n%3

def sigma(n, i):
    n = balanced_res(n)
    i = balanced_res(i)
    if n == 0:
        return ''
    if i == 0:
        if n == 0:
            return ''
        elif n > 0:
            return 'z'
        else:
            return 'Z'
    elif i > 0:
        if n > 0:
            return 'Tzt'
        else:
            return 'TZt'
    else:
        if n > 0:
            return 'tzT'
        else:
            return 'tZT'


def cleaner_ext(w):
    if w == '':
        return ''
    if len(w) == 1:
        return w
    for i in range(len(w) - 1):
        if w[i:i + 2] == 'tT' or w[i:i + 2] == 'Tt' or w[i:i + 2] == 'zZ' or w[i:i + 2] == 'Zz':
            return cleaner_ext(w[:i] + w[i + 2:])
    return w



def app_rel(w, v):
    if w == v: return w
    if w == '':
        return ''
    if len(w) == 1:
        return w
    for i in range(len(w) - 1):
        if w[i:i + 2] == 'tt':
            return app_rel(w[:i] + 'T' + w[i + 2:], '-1')
        if w[i:i + 2] == 'zz':
            return app_rel(w[:i] + 'Z' + w[i + 2:], '-1')
        if w[i:i + 2] == 'ZZ':
            return app_rel(w[:i] + 'z' + w[i + 2:], '-1')
        if w[i:i + 2] == 'TT':
            return app_rel(w[:i] + 't' + w[i + 2:], '-1')
    return app_rel(cleaner_ext(w), w)



def epimorph(w):
  v = ''
  for i in w:
    if i == 't':
      v = v + sigma(1,-1)
    elif i == 'T':
      v = v + sigma(-1,-1)
    else: v = v + i
  return app_rel(v,'-1')


def rel(n, m, i):
    W = sigma(-n - 1, i - 1) + sigma(-1, i) + sigma(n + 1, i - 1) + sigma(-m, i - 2) + sigma(-1, i - 1) + sigma(m,i - 2) + sigma(-n, i - 1) + sigma(1, i) + sigma(n, i - 1) + sigma(-m, i - 2) + sigma(1, i - 1) + sigma(m, i - 2)

    w = app_rel(W, -1)

    return w

print(rel(0,1,1))

print(epimorph(rel(0,1,1)))

def invertib(w):
  W = ''
  for i in w:
    if i == 't':
      W = 'T' + W
    if i == 'T':
      W = 't' + W
    if i == 'z':
      W = 'Z' + W
    if i == 'Z':
      W = 'z' + W
  return W


def conj_w(w,v):
  return app_rel(cleaner_ext(invertib(v)+w+v),'')

def halve(w):
  L = []
  W = recur_word(w)
  l = len(w)
  for i in W:
    L.append(i[:(l//2)])
  return L
def halves(w):
  return halve(w)+halve(invertib(w))

def acted_gen(s,w):

  if len(w) <= 1:
    return w
  
  if s == 't':
    return str((int(w[0])+1)%3)+w[1:]
  if s == 'T':
    return str((int(w[0])-1)%3)+w[1:]
  
  if s == 'Z':
    if w[0] == '0':
      return '0'+acted_gen('T', w[1:])
    if w[0] == '1':
      return w
    if w[0] == '2':
      return '2'+acted_gen('Z', w[1:])
    
  if s == 'z':
    if w[0] == '0':
      return '0'+acted_gen('t', w[1:])
    if w[0] == '1':
      return w
    if w[0] == '2':
      return '2'+acted_gen('z', w[1:])

  if s == 'Z':
    if w[0] == '0':
      return '0'+acted_gen('T', w[1:])
    if w[0] == '1':
      return w
    if w[0] == '2':
      return '2'+acted_gen('Z', w[1:])
  

def acted_elem(g,w):
  Q = len(g)
  if Q <= 1:
    return acted_gen(g,w)
  return acted_elem(g[:(Q-1)],acted_gen(g[Q-1],w))


def tre(w):
  return w+w+w

def find_decomp(w):
  W = tre(w)

  D = len(w)

  for i in range(0,len(W)-D -1):
    print(invertib(W[i:i+D//2])[::-1], W[i+D//2:D+i])
    if invertib(W[i:i+D//2])[::-1] == W[i+D//2:D+i]:
      return [i,"kek", W[i:i+D//2]]



QQQ = [[5, 64, 32], [6, 128, 80], [7, 256, 184], [8, 512, 408], [9, 1024, 872], [10, 2048, 1824], [11, 4096, 3768], [12, 8192, 7712], [13, 16384, 15680],[14,32768, 31736], [15,65536,64024],[16,131072, 128856]]


for i in range(len(QQQ)-1):
  print((QQQ[i+1][1]-QQQ[i+1][2])/(QQQ[i][1]-QQQ[i][2]))




  
L = cons(['t', 'T', 'z','Z'],3)

W = halves('tzTZTztz')
print(W)



C = 0

for i in L:
  K = C
  for g in W:
    if g in i[:-1]:
      C = C+1
      print(i)
      break
  if K == C:
    print(i,-1)

print(len(L),C,len(L)-C)
      
