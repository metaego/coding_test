# https://school.programmers.co.kr/learn/courses/30/lessons/120862

def solution(numbers):
    max_num = numbers[0] * numbers[1]
    for idx, num1 in enumerate(numbers):
        for num2 in numbers[idx+1:]:
            if (num1 * num2) > max_num:
                max_num = num1 * num2
    return max_num

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))

#########################################
# 다른 사람 풀이 
def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])