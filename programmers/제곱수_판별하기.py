# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    num = 1
    while num ** 2 < n:
        num += 1
    return 1 if num ** 2 == n else 2

print(solution(144))
print(solution(976))

#############################
# 다른 사람 풀이 1
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2


# 다른 사람 풀이 2
def solution(n):
    if n**(1/2) == int(n**(1/2)) :
        return 1
    else :
        return 2