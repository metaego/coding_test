# https://school.programmers.co.kr/learn/courses/30/lessons/120814
import math

def solution(n):
    answer = math.ceil(n / 7)
    return answer

print(solution(7))
print(solution(1))
print(solution(15))


##################################
# 다른 사람 풀이_1

def solution(n):
    return (n - 1) // 7 + 1