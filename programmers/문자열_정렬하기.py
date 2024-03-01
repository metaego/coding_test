# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    return sorted([int(chr) for chr in my_string if chr.isnumeric()])


print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))

######################################################
# 다른 사람 풀이 1
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))



# 다른 사람 풀이 2
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])