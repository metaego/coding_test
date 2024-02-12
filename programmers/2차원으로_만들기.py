# https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    import numpy as np
    answer = np.array(num_list).reshape(-1, n).tolist()
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))



###########################################
# 다른 사람 풀이 1
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer


# 다른 사람 풀이 2
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]