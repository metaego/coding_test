# https://school.programmers.co.kr/learn/courses/30/lessons/120815?

def solution(n):
    pizza = 1
    piece = 6
    while ((pizza * piece) % n) != 0 :
        pizza += 1
    return pizza


print(solution(6))
print(solution(10))
print(solution(4))

###############################################
# 다른 사람 풀이_1
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1

# 다른 사람 풀이_2
import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6