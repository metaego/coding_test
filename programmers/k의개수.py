# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    cnt = 0
    for num in range(i, j+1):
        cnt += list(str(num)).count(str(k))
    return cnt


print(solution(1,13,1))
print(solution(10,50,5))
print(solution(3,10,2))

###########################
# 다른 사람 풀이
def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))