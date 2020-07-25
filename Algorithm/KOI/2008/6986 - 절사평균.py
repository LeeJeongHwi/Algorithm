from sys import stdin
stdin = open("input.txt","r")
n,k = map(int,stdin.readline().split())
#점수의 개수 n / 제외되는 점수의 개수 k
scores = [float(stdin.readline()) for _ in range(n)]
scores.sort()
# print(scores)
def trim_mean(n,k):
    result = sum(scores[k:n-k])/(n-(k*2))
    result += 1e-9
    print("{:.2f}".format(round(result,2)))
def corrected_mean(n,k):
    # print(scores[k],scores[n-k-1])
    for i in range(0,k):
        scores[i] = scores[k]
    # print(scores)
    for i in range(n-1,n-k-1,-1):
        scores[i] = scores[n-k-1]
    # print(scores)
    result = sum(scores)/(n)
    result += 1e-9
    print("{:.2f}".format(round(result,2)))
trim_mean(n,k)
corrected_mean(n,k)
#컴퓨터의 오차 때문에 1e-9를 더해줘야함