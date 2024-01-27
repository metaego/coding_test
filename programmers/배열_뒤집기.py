# https://school.programmers.co.kr/learn/courses/30/lessons/120821

def solution(num_list):
    answer = []
    for num in num_list[::-1]:
        answer.append(num)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))

#####################################
# 다른 사람 풀이_1
def solution(num_list):
    return num_list[::-1]


# 다른 사람 풀이_2
def solution(num_list):
    num_list.reverse()
    return num_list


# 다른 사람 풀이_3
def solution(num_list):
    result =[]
    while(num_list):
        result.append(num_list.pop())
    return result

