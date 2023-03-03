# n=(input()).split(' ')
# m=0
# for i in range(int(n[0])):
#     num=(max(int(x) for x in [(x) for x in (input().split(' '))]))%int(n[1])
#     m+= num*num
# print(m%(int(n[1])))

from itertools import product

K, M = map(int,input().split())

N = (list(map(int, input().split()))[1:] for _ in range(K))

max_lst = []
for item in product(*N):
    S = 0
    for val in item:
        S += val**2
    S_max = S % M
    max_lst.append(S_max)
    
print(max(max_lst))
