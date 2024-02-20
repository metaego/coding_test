# https://school.programmers.co.kr/learn/courses/30/lessons/120906

def solution(n):
    answer = 0
    for char in str(n):
        answer += int(char)                
    return answer


print(solution(1234))
print(solution(930211))

#########################
# 다른 사람 풀이
def solution(n):
    return sum(int(i) for i in str(n))

