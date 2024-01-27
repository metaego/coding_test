# https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    if angle < 90 :
        return 1
    elif angle ==  90 :
        return 2
    elif angle < 180 :
        return 3
    else :
        return 4

##################################
# 다른 사람 풀이 
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

   
print(solution(40)) # 1
print(solution(70)) # 1
print(solution(90)) # 2
print(solution(95)) # 3
print(solution(180)) # 4