# https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    cnt = 0
    while hp > 0:
        if hp >= 5:
            cnt += hp // 5
            hp = hp % 5
        elif hp >= 3:
            cnt += hp // 3
            hp = hp % 3
        else:
            cnt += hp // 1
            hp = hp % 1
    return cnt


print(solution(23))
print(solution(24))
print(solution(999))



#######################
# 다른 사람 풀이
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)