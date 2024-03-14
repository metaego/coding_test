# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

def solution(my_string):
    answer = []
    for chr in list(my_string):
        if chr not in answer:
            answer.append(chr)
    return ''.join(answer)


print(solution("people"))
print(solution("We are the world"))