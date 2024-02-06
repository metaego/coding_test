# https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    cnt, num = 0, 1
    while num * num <= n:
        if n % num == 0:
            cnt += 2
        num += 1

    if (num-1) * (num-1) == n:
        cnt -= 1
    return cnt

print(solution(20))
print(solution(100))