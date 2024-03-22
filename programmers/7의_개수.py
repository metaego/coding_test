# https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    cnt = 0
    for num in array:
        cnt += str(num).count('7')
    return cnt

print(solution([7, 77, 17]))
print(solution([10, 29]))

######################
# 다른 사람 풀이 1
def solution(array):
    return str(array).count('7')

# 다른 사람 풀이 2
def solution(array):
    return ''.join(map(str, array)).count('7')