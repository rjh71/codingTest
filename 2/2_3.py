# K번째 큰 수
# 20점

import sys
sys.stdin = open("../input.txt", "rt")

n, k = map(int, input().split())
card = list(map(int, input().split()))

result = []

for i in range(n):
    for j in range(i+1, n):
        for t in range(j+1, n):
            result.append(card[i]+card[j]+card[t])

result.sort()
result.reverse()
print(k)
print(result[k-1])