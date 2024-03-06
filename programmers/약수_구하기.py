# https://school.programmers.co.kr/learn/courses/30/lessons/120897

def solution(n):
    return  [num for num in range(1, n+1) if n % num == 0]

print(solution(24))
print(solution(29))