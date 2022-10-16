# K번째 수
# 80점

import sys
sys.stdin = open("../input.txt", "rt")

T = int(input())
inputCase = []

for i in range(T):
    inputCase.append([list(map(int, input().split())) for _ in range(2)])

for i in range(T):
    n = inputCase[i][0][0]
    s = inputCase[i][0][1]
    e = inputCase[i][0][2]
    k = inputCase[i][0][3]


    result = inputCase[i][1][s-1:e]
    result.sort()
    print("#{} {}".format(i+1, result[k-1]))