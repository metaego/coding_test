# https://school.programmers.co.kr/learn/courses/30/lessons/120854

def solution(strlist):
    answer = []
    for string in strlist:
        answer.append(len(string))
    return answer



print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))


####################################
# 다른 사람 풀이 1
def solution(strlist):
    answer = list(map(len, strlist))
    return answer


# 다른 사람 풀이 2
def solution(strlist):
    return [len(str) for str in strlist]
