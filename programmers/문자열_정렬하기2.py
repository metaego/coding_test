# https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    return ''.join(sorted(my_string.lower()))

print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))