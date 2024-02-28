# https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    max_num = [array[0], 0]
    for idx, num in enumerate(array):
        if num > max_num[0]:
            max_num[0] = num
            max_num[1] = idx 
    return max_num


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))

########################################
# 다른 사람 풀이
def solution(array):
    return [max(array), array.index(max(array))]
