# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    array.sort()
    min_v = [array[0], abs(array[0]- n)]
    for num in array:
        if min_v[1] > abs(num - n):
            min_v[1] = abs(num - n)
            min_v[0] = num
    return min_v[0]

print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))

#######################################
# 다른 사람 풀이
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer