# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    capital = 'abcdefghijklmnopqrstuvwxyz'
    answer = ""
    for num in str(age):
        answer += ''.join(capital[int(num)])
    return answer

print(solution(23))
print(solution(51))
print(solution(100))