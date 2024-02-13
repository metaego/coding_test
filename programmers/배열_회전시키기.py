# https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    answer = []
    if direction == "left":
        numbers.append(numbers[0])
        del numbers[0]
        return numbers
    else:
        numbers.insert(0, numbers[-1])
        del numbers[-1]
        return numbers

print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))


######################################################
# 다른 사람 풀이 1
def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0,numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    return numbers


# 다른 사람 풀이 2
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


# 다른 사람 풀이 3
from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)