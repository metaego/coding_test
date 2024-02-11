# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def fac(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n * fac(n-1)

def solution(balls, share):
    return int(fac(balls)/(fac(balls-share) * fac(share)))

print(solution(3, 2))
print(solution(5, 3))

##########################
# 다른 사람 풀이_1
import math

def solution(balls, share):
    return math.comb(balls, share)

# 다른 사람 풀이 2
def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result