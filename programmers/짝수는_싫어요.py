# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    answer = []
    for num in range(1, n+1):
        if num % 2 == 1:
            answer.append(num)
    return answer


print(solution(10))
print(solution(15))