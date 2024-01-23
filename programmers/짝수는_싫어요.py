# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    answer = []
    for num in range(1, n+1):
        if num % 2 == 1:
            answer.append(num)
    return answer


print(solution(10))
print(solution(15))


###############################
# 다른 사람 풀이_!
def solution(n):
    return [i for i in range(1, n+1, 2)]



# 다른 사람 풀이_2
def solution(n):
    return [x for x in range(n + 1) if x % 2]


# 다른 사람 풀이_3
def solution(n):
    return list(range(1, n+1, 2))