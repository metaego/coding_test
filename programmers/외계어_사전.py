# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    answer = 2
    for word in dic:
        if set(word) == set(spell):
            answer = 1
    return answer

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))

###############################################################################
# 다른 사람 풀이
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2