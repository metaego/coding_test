# https://school.programmers.co.kr/learn/courses/30/lessons/120886

def solution(before, after):
    print(''.join(reversed(before)))
    if ''.join(reversed(before)) == after: return 1
    return 0

print(solution('olleh', 'hello'))
print(solution('allpe', 'apple'))