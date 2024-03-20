# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    result = set()
    temp_set = set()
    for chr in s:
        if chr not in result:
            result.add(chr)
        else:
            temp_set.add(chr)
    
    result = result - temp_set
    return ''.join(sorted(result))

print(solution('abcabcadc'))
print(solution('abdc'))
print(solution('hello'))

#################################
# 다른 사람 풀이
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer