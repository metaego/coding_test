# https://school.programmers.co.kr/learn/courses/30/lessons/120852

def solution(n):
    answer = set()
    num = 2
    while n > 1:
        if n % num == 0:
            answer.add(int(num))
            n /= num
        else:
            num += 1
    return sorted(list(answer))

print(solution(12))
print(solution(17))
print(solution(420))