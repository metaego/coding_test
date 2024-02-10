# https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]


print(solution([1,2,3,4,5]))
print(solution([0, 31, 24, 10, 1, 9]))


####################################
# 다른 사람 풀이
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]