# https://school.programmers.co.kr/learn/courses/30/lessons/120864

def solution(my_string):
    total = 0
    for chr in my_string:
        if chr.isdigit():
            total += int(chr)
    return total

print(solution("aAb1B2cC34oOp"))