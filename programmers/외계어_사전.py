# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    answer = 2
    for word in dic:
        if sorted(list(word)) in sorted(spell):
            answer = 1
    return answer

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))