# https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    answer = ''
    for item in rsp:
        if item == "0":
            answer += "5"
        elif item == "2":
            answer += "0"
        else:
            answer += "2"
    return answer

print(solution("2"))
print(solution("205"))


#########################
# 다른 사람 풀이
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)