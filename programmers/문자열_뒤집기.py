# https://school.programmers.co.kr/learn/courses/30/lessons/120822

def solution(my_string):
    return my_string[::-1]


# print(solution("jaron"))
# print(solution("bread"))

############################
# 다른 사람 풀이
def solution(my_string):
    return ''.join(list(reversed(my_string)))
