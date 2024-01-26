# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    import math
    answer = math.ceil(n / slice)
    return answer 

print(solution(7, 10))
print(solution(4, 12))

###############################
# 다른 사람 풀이
def solution(slice, n):
    return ((n - 1) // slice) + 1