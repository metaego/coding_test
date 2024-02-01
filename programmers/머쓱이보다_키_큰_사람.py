# https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    for student_height in array:
        if student_height > height:
            answer += 1
    return answer


print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))

##############################
# 다른 사람 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)