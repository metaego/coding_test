# https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    cnt = 0
    for char in s2:
        if char in s1:
            cnt += 1
    return cnt

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))

####################
# 다른 사람 풀이 1
def solution(s1, s2):
    return len(set(s1)&set(s2))

