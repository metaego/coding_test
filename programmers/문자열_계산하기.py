# https://school.programmers.co.kr/learn/courses/30/lessons/120902

def solution(my_string):
    lst = my_string.split()
    total = 0
    operation = '+'
    for chr in lst:
        if chr.isdigit():
            chr = operation + chr
            total += int(chr)
        else:
            operation = chr
    return total

print(solution("3 + 4"))

##################################
# 다른 사람 풀이
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))