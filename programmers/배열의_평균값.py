# https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    return sum(numbers)/len(numbers)


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))


#############################################
# 다른 사람 풀이
import numpy as np
def solution(numbers):
    return np.mean(numbers)