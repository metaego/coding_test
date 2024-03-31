# https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):
    result = []
    while len(my_str) > 0:
        result.append(my_str[: n])
        my_str = my_str[n:]
    return result

print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))


########################################
# 다른 사람 풀이
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]