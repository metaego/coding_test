# https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    return 1 if 2 * max(sides) < sum(sides) else 2

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))