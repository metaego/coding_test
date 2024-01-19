# https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    array = sorted(array)
    return array[len(array) // 2]

# 다른 사람 풀이
def solution(array):
    return sorted(array)[len(array) // 2]