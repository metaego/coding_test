# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    array_cnt, array_num = [], []

    for num in list(set(array)):
        array_cnt.append(array.count(num)) 
        array_num.append(num)

    if array_cnt.count(max(array_cnt)) > 1:
        return -1
    else: 
        idx = array_cnt.index(max(array_cnt))
        return array_num[idx]


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))

#############################################
# 다른 솔루션_1
def solution(array):
    # 배열의 각 숫자의 빈도수를 세기
    frequency = {}
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # 빈도수가 가장 높은 숫자 찾기
    max_freq = max(frequency.values())
    
    # 빈도수가 가장 높은 숫자들을 모두 찾기
    mode_candidates = [num for num, freq in frequency.items() if freq == max_freq]
    
    # 최빈값이 여러 개인 경우 -1 반환, 아니면 최빈값 반환
    return -1 if len(mode_candidates) > 1 else mode_candidates[0]

# 다른 솔루션_2: Counter() 함수 사용
from collections import Counter

def solution(array):
    # 배열의 각 숫자의 빈도수를 세기
    counter = Counter(array)
    
    # 빈도수가 가장 높은 숫자 찾기
    max_freq = max(counter.values())
    
    # 빈도수가 가장 높은 숫자들을 모두 찾기
    mode_candidates = [num for num, freq in counter.items() if freq == max_freq]
    
    # 최빈값이 여러 개인 경우 -1 반환, 아니면 최빈값 반환
    return -1 if len(mode_candidates) > 1 else mode_candidates[0]
