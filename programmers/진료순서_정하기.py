# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    emergency_desc = sorted(emergency, reverse=True)
    answer = []
    for num in emergency:
        answer.append(emergency_desc.index(num) +1)
    return answer


print(solution([2, 100]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))