# https://school.programmers.co.kr/learn/courses/30/lessons/120886

# def solution(before, after):
#     if ''.join(reversed(before)) == after: return 1
#     return 0

def solution(before, after):
    return (sorted(before) == sorted(after)) * 1



print(solution('olleh', 'hello'))
print(solution('allpe', 'apple'))