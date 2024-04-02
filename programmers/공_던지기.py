# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    max_num = max((k-1) * 2, len(numbers))
    min_num = min((k-1) * 2, len(numbers))
    
    idx = max_num % min_num 
    return numbers[int(max_num // min_num) if idx == 0 else idx] 
     

print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))

######################################################
# 다른 사람 풀이
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]