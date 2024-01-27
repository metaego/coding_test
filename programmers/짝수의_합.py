# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    answer = 0
    for num in range(n, 1, -1):
        if num % 2 == 0:
            answer += num
    return answer

print(solution(10))
print(solution(4))


#################################
# 다른 사람 풀이_1
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])


# 다른 사람 풀이_2
def solution(n):
    return 2*(n//2)*((n//2)+1)/2