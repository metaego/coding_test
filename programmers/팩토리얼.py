# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    num, total = 1, 1
    while total < n:
        num += 1
        total *= num
    return num -1 if total > n else num


print(solution(3628800))
print(solution(7))