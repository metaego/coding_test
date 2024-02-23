# https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    return sum([int(chr) for chr in my_string if chr in '123456789'])

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))


##########################################
# 다른 사람 풀이 1
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())