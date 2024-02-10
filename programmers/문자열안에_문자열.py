# https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    return 1 if str2 in str1 else 2

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))


###########################
# 다른 사람 풀이 1
def solution(str1, str2):
    return 1 + int(str2 not in str1)