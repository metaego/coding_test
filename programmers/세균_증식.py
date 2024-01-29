# https://school.programmers.co.kr/learn/courses/30/lessons/120910

def solution(n, t):
    return n * 2 ** t

print(solution(2, 10))
print(solution(7, 15))

############################
# 다른 사람 풀이 
def solution(n, t):
    return n << t