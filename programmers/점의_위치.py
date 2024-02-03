# https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        else:
            return 4
    else:
        if dot[1] > 0:
            return 2
        else:
            return 3
        
print(solution([2, 4]))
print(solution([-7, 9]))


###########################
# 다른 사람 풀이 
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]