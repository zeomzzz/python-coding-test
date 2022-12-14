# 풀이 1 : for문

n, m = map(int, input().split())
cards = list(map(int, input().split()))
lst = []

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            sum = cards[i] + cards[j] + cards[k]

            if sum > m :
                continue
            else :
                lst.append(sum)

print(max(lst))


# 풀이 2 : itertools

import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))
lst = []

for i in itertools.combinations(cards, 3) :
    if sum(i) > m :
        continue
    else :
        lst.append(sum(i))

print(max(lst))


# 풀이 3 : 브루트 포스 알고리즘

n, m = map(int, input().split())
cards = list(map(int, input().split()))
x = 0

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            sum = cards[i] + cards[j] + cards[k]

            if sum <= m :
                x = max(x, sum)

print(x)
