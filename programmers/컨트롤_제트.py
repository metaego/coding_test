# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    temp_chr = ''
    total = 0
    for chr in list(s):
        if chr in '-1234567890':
            temp_chr += chr
        elif chr == ' ':
            total += int(temp_chr)
            before_num = int(temp_chr)
            temp_chr = ''
        elif chr == 'Z':
            total -= before_num
            temp_chr = '0'
    total += int(temp_chr)
    return total


print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))