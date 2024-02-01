# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''
    for string in my_string:
        answer += string * n
    return answer


print(solution("hello", 3))


###########################
# 다른 사람 풀이 1
def solution(my_string, n):
    return ''.join(i*n for i in my_string)