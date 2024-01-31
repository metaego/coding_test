# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    answer = [0, 0]
    for num in num_list:
        if num % 2:
            answer[1] += 1
        else:
            answer[0] += 1
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))


#########################
# 다른 사람 풀이
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
